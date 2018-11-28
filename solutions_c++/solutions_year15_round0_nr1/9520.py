#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <fstream>                                                                 
#include <sstream>                                                                 
#include <string>                                                                  
#include <vector>                                                                  
#include <queue>                                                                   
#include <stack>                                                                   
#include <map>                                                                     
#include <set>                                                                     
#include <algorithm>                                                               
                                                                                   

using namespace std;                                                               
                                                                                   
int main(int argc, char * argv[])                                                  
{                              
    freopen(argv[1],"r",stdin);
    freopen(argv[2],"w",stdout);
    ios::sync_with_stdio(false);
    //cout << fixed <<setprecision(7);
    int t;
    cin >> t;
    while(t--) {
        int n;
        string a;
        cin >> n >> a;
        int la = a.size();
//        cout << "n=" << n << " a=" << a << " length(a)=" << la << " " << ((n+1==la)?"match":"mismatch") << endl;
        vector<int> sa;
        for(int i=0;i<la;++i)
        {
//            cout << a[i] << " ";
            sa.push_back(a[i]-'0');
        }
//        cout << endl;
//        cout << " int vector size=" << sa.size() << " " << ((sa.size() == la)?"good":"bad")<< endl;
//        for(int j=0;j<sa.size();++j) { cout << sa[j] << " "; } cout << endl;
        int f=0, m=0;
        for(int k=0;k<sa.size();++k)
        {
          if(sa[k]>0){
            if(m<k) {
                f+=k-m;
                m=k;
            }
            m+=sa[k];
          } 
        }
        static int id=0;
        cout << "Case #" << ++id << ": " << f << endl;
    }
    return 0;
}

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <complex>
#include <iomanip>
using namespace std;

long long ks[110];

int main() {    
    
    freopen("D:\\Desktop\\A-large.in","r",stdin);
    freopen("D:\\Desktop\\practice.out","w",stdout);
    
    int T;
    string str;
    cin>>T;
    
    for(int cases=0;cases<T;cases++){
        
        cin>>str;
        deque<char> dq;
        dq.push_back(str[0]);
        
        for(int i=1;i<str.length();i++){
            if(str[i]>=dq[0])
                dq.push_front(str[i]);
            else
                dq.push_back(str[i]);
        }        
        
        string ret(dq.size(),'0');
        int f=0;
        
        for(int i=0;i<dq.size();i++)
            ret[f++] = dq[i];
        
                        
        cout<<"Case #"<<1+cases<<": "<<ret<<endl;
    }
    return 0;
}

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

int main() {    
    
    freopen("D:\\Desktop\\large.txt","w",stdout);
    freopen("D:\\Desktop\\A-large.in","r",stdin);
    
    
    int T, N, t, mask;
    int all = (1<<10)-1;
    bool found = false;
    
    cin>>T;
    
    for(int i=1;i<=T;i++){
        cin>>N;
        if(N==0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        mask = 0;
        found = false;
        for(int j=N;j<N*100;j+=N){
            t = j;
            while(mask!=all && t!=0){
                mask |= (1<<(t%10));
                t /= 10;
            }
            if(mask==all){
                cout<<"Case #"<<i<<": "<<j<<endl;
                found = true;
                break;
            }
        }        
        if(!found)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    }
    //system("PAUSE");
    return 0;
}

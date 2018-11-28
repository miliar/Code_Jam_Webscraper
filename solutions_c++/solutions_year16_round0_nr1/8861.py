#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <cstdio>
#include <math.h>
#include <time.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
bool flag[10];
int main()
{
   // freopen("A-large.in","r",stdin);
   // freopen("DATA.txt","w",stdout);
    int n; cin>>n;
    for(int i = 0; i < n; i++){
        long long a; cin>>a;
        long long add = a;
    //    cout<<a<<endl;
        cout<<"Case #"<<i+1<<": ";
        if(a==0) cout<<"INSOMNIA"<<endl;
        else{
            memset(flag,0,sizeof(flag));
            while(1){
                long long temp = a;
                while(temp != 0){
                 //   cout<<temp%10<<endl;
                    flag[  temp%10  ] = 1;
                    temp/=10;
                }
                bool br = true;
                for(int j = 0; j < 10; j++)
                    if(flag[j]==0){
                        br = false;
                        break;
                    }
                if(br) break;
                else a+=add;
            }
            cout<<a<<endl;
        }
    }
    return 0;
}





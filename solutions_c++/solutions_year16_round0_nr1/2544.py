#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<set>
#include<vector>
#include<map>
#include<cassert>
#include<queue>
using namespace std;
long long c[1000005];

int main(){
    
    c[0]=-1;

    for(int i=1;i<=1000000;i++){
        int mask=0;
        for(long long j=1;;j++){
            long long x=i*j;
            long long aux=x;
            while(x!=0){
                mask|=(1<<(x%10));
                x/=10;
            }

            if(mask==(1023)){
                c[i]=aux;
                break;
            }
        }
    }
    
    int tc;cin>>tc;
    for(int caso=1;caso<=tc;caso++){
        int n;
        cin>>n;
        cout<<"Case #"<<caso<<": ";
        if(c[n]==-1)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<c[n]<<endl;
    }
    
    return 0;
}






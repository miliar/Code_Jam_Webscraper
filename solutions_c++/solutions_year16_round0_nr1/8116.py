#include<iostream>
#include<cstdio>
#include<string.h>
#include<algorithm>

using namespace std;

bool check[10];

int main(){

    freopen("A-large.in","r",stdin);
    freopen("o1.out","w",stdout);

    long long int N,tmp,rem,val;
    int T,i,cnt;
    cin>>T;
    for(i=1; i<=T; i++){
        cin>>N;
        if(N==0){
            cout<<"Case #"<<i<<": INSOMNIA\n";
        }
        else{
            val=N;
            memset(check,0,sizeof(check));
            cnt=0;
            while(cnt!=10){
                tmp=N;
                while(tmp){
                    rem=tmp%10;
                    if(check[rem]==0){
                        check[rem]=1;
                        cnt+=1;
                    }
                    tmp/=10;
                }
                if(cnt!=10)
                    N+=val;
            }
            cout<<"Case #"<<i<<": "<<N<<"\n";
        }
    }

    return 0;
}

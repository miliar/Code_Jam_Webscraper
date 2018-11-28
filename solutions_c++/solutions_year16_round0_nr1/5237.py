//HARE KRISHNA
#include<bits/stdc++.h>
using namespace std;

#define ll long long
bool isit[15];
int main(){

    freopen("input1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t,tcase;
    scanf("%d",&t);
    ll n;
    for(tcase=1;tcase<=t;tcase++){


        memset(isit,false,sizeof(isit));
        scanf("%lld",&n);
        printf("Case #%d: ",tcase);
        if(n==0){

            printf("INSOMNIA\n");
        }
        else if(n==1){
            printf("10\n");
        }
        else{
            ll num=n;
            bool mainflag=false;
            while(1){

                bool flag=true;
                for(int k=0;k<=9;k++){
                    if(isit[k]==false){
                        flag=false;
                        break;
                    }
                }
                if(flag){
                        mainflag=true;
                        break;
                }
                if(num>=1000000000000000005)break;
                ll numano=num;
                while(numano){
                    int another=numano%10;
                    isit[another]=true;
                    numano=numano/10;
                }
                num=num+n;
            }
            if(mainflag){

                num=num-n;
                printf("%lld\n",num);
            }
            else{
                printf("INSOMNIA\n");
            }
        }
    }
    return 0;
}

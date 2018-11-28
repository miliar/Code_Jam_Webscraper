#include <bits/stdc++.h>

using namespace std;
#define sd(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sull(x) scanf("%llu",&x)
#define pd(x) printf("%d",x)
#define pull(x) printf("%llu",x)
#define pll(x) printf("%lld",x)

#define pn() printf("\n")
#define loop(i, a, b) for (int i = int(a); i < int(b); i++)
#define MAXN 1000005
#define MOD 1000000007 //10^9 +7
typedef long long int ll;
typedef unsigned long long int ull;

int p[30];
char f(int i){
    return (char)(i+64);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t,n,mx,key,cnt,tmp;
    bool flag;
    sd(t);
    loop(test,1,t+1){

        sd(n);
        loop(i,1,30)p[i]=0;
        loop(i,1,n+1){
            cin>>p[i];
        }
        cout<<"Case #"<<test<<": ";
        flag=false;
        loop(i,1,n+1)if(p[i]!=0)flag=true;
        while(flag){
             mx = -1;
            loop(i,1,n+1){
                mx = max(p[i],mx);
            }
            cnt=0;
            loop(i,1,n+1){
                if(p[i]==mx)cnt++;
            }
            if(cnt>3){
                key=2;
                loop(i,1,n+1){
                    if(p[i]==mx&&key){
                        p[i]--;
                        cout<<f(i);
                        key--;
                    }
                }
                cout<<" ";

            }
            else if(cnt==3){
                key=1;
                loop(i,1,n+1){
                    if(p[i]==mx&&key){
                        p[i]--;
                        cout<<f(i);
                        key--;
                    }
                }
                cout<<" ";
            }
            else if(cnt==2){
                key=2;
                loop(i,1,n+1){
                    if(p[i]==mx&&key){
                        p[i]--;
                        cout<<f(i);
                        key--;
                    }
                }
                cout<<" ";

            }
            else if(cnt==1){
                tmp = 0;
                loop(i,1,n+1)if(p[i]==mx-1)tmp++;
                if(tmp==1){
                    key=1;
                    loop(i,1,n+1){
                        if(p[i]==mx&&key){
                            p[i]--;
                            cout<<f(i);
                            key--;
                        }
                    }
                    cout<<" ";
                }
                else{
                    loop(i,1,n+1){
                        if(p[i]==mx){
                            if(p[i]>1){
                                p[i]=p[i]-2;
                                cout<<f(i)<<f(i);
                            }
                            else{
                                p[i]--;
                                cout<<f(i);
                            }

                        }
                    }
                    cout<<" ";
               }
            }
        flag=false;
        loop(i,1,n+1)if(p[i]!=0)flag=true;

        }
    cout<<endl;
    }



    return 0;
}











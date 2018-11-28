#include<iostream>
#include<cstring>
using namespace std;
int main(){
//freopen ("A-small-attempt0 (2).txt","r",stdin);
freopen ("output.txt","w",stdout);
    int a,b,c,t,i;
    cin>>t;
    for(int it=1;it<=t;it++){
            cout<<"Case #"<<it<<": ";
            int smax;
            cin>>smax;
            getchar();

            int total=0;
            int ans=0;
            for(i=0;i<=smax;i++){
                                int x=getchar()-48;
                                if(total<i)
                                {
                                           ans=ans+i-total;
                                           total=i;
                                }
                                total+=x;
                                }
            cout<<ans<<endl;
            }
    }

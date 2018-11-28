#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin>>T;
    for(int t_c=1;t_c<=T;t_c++){
        long long n;
        cin>>n;
        bool ara[10];

        memset(ara,0,sizeof(ara));
        long long int i;
        for( i=1;i<=1000;i++){
            long long m=n*i;
            while(m>0){
                int a=m%10;
                m/=10;
                ara[a]=1;

            }
            bool flag=1;
            for(int i=0;i<10;i++){
                if(ara[i]==0) flag=0;
            }
            if(flag==1) break;
        }
        if(i>1000) cout<<"Case #"<<t_c<<": INSOMNIA\n";
        else cout<<"Case #"<<t_c<<": "<<i*n<<"\n";
    }
}

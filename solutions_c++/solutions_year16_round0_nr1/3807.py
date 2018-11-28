#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;

bool seen[20];

int main()
{
    freopen("gcj_16_qua_1_in.txt","r",stdin);
    freopen("gcj_16_qua_1_out.txt","w",stdout);
    int t;
    cin>>t;
    for(int qq=1;qq<=t;qq++) {
        cout<<"Case #"<<qq<<": ";
        long long i,j,n,lst,temp;
        cin>>n;
        memset(seen,0,sizeof(seen));
        if(n==0) cout<<"INSOMNIA\n";
        else {
            for(j=1;;j++) {
                temp=n*j;
                while(temp>0) seen[temp%10]=true,temp/=10;
                for(i=0;i<10;i++) if(!seen[i]) break;
                if(i>=10) break;
            }
            cout<<n*j<<"\n";
        }
    }
    return 0;
}

//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,z,n,m,temp=0,now;

    cout<<"Case #1:\n";

    cin>>i>>n>>m;

    for(i=2;i<n;i+=2)
    {
        for(j=i+2;j<n;j+=2)
        {
            for(k=3;k<n;k+=2)
            {
                for(l=k+2;l<n;l+=2)
                {
                    now=0;
                    now=( now | (1LL<<(i-1)));
                    now=( now | (1LL<<(j-1)));
                    now=( now | (1LL<<(k-1)));
                    now=( now | (1LL<<(l-1)));
                    now=( now | (1LL<<(n-1)));
                    now=( now | (1));

                    for(z=0;z<n;z++)
                    {
                        if((1LL<<z) & now) cout<<"1";
                        else cout<<"0";
                    }

                    for(z=2;z<=10;z++) cout<<" "<<z+1;
                    cout<<endl;

                    temp++;

                    if(temp==m) return 0;
                }
            }
        }
    }


}

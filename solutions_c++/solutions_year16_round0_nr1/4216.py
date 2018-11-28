#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define int long long
int dig[15]={0};
void digex(int n)
{
    while(n)
    {
        int d=n%10;
        dig[d]=1;
        n/=10;
    }
}



main() {
	freopen("linp.txt","r",stdin);
	freopen("louts.txt","w",stdout);

    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<z<<": INSOMNIA"<<endl;
            continue;
        }
        int k;
        memset(dig,0,sizeof(dig));
        for(int i=1;;i++)
        {   k=n*i;
            digex(k);
            int flag=0;
            for(int i=0;i<=9;i++)
                if(dig[i]==0)
                {
                    flag=1;
                    break;
                }
            if(flag==0)
            {
                cout<<"Case #"<<z<<": "<<k<<endl;
                break;
            }
        }
    }

	return 0;
}

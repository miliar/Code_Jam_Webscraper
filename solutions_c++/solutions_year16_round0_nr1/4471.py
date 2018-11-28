#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
using namespace std;

int t,n;
bitset<15>viz;

int main()
{
    int i,j,cnt,aux,ok,poz;
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);
    cin>>t;
    for (j=1;j<=t;j++)
    {
        cin>>n;
        cnt=100;poz=0;
        while (cnt && !poz)
        {
            aux=(100-cnt+1)*n;
            while (aux) viz[aux%10]=1,aux/=10;
            ok=1;
            for (i=0;i<=9;i++)
                if (!viz[i])
                    ok=0;
            if (ok==1) poz=(100-cnt+1)*n;
            cnt--;
        }

        if (poz) cout<<"Case #"<<j<<": "<<poz<<"\n";
        else cout<<"Case #"<<j<<": INSOMNIA\n";

        //golire
        for (i=0;i<=9;i++) viz[i]=0;
    }
    return 0;
}


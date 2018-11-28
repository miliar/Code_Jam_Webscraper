#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,j,k,l;
    long long int m;
    int n;
    freopen("1.txt","r",stdin);
     freopen("2.txt","w+",stdout);
    cin>>n;
    for(i=1; i<=n; i++)
    {
        cin>>m;
        map<char,int>maps;
        int val=0;
        cout<<"Case #"<<i<<": ";
        if(m==0)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            for(j=1;; j++)
            {
                long long int p=j;
                long long int l=p*m;
                char x[10000];
                ltoa(l,x,10);
                for(k=0; k<strlen(x); k++)
                {
                    if(maps[x[k]]==0)val++;
                    maps[x[k]]=1;
                    if(val==10)break;
                }
                if(val==10)
                {
                    cout<<l<<endl;
                    break;
                }
            }
        }
    }
    return 0;
}

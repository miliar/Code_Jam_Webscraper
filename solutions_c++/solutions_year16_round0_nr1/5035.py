#include<bits/stdc++.h>
using namespace std;

bool occ[10];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,x;
    bool f;
    cin>>t;
    for(int j = 1; j <= t; j++)
    {
        memset(occ,0,sizeof(occ));
        cin>>n;
        if(!n)
        {
            cout<<"Case #"<<j<<": INSOMNIA\n";
            continue;
        }
        for(int i = 1; i <= 100; i++)
        {
            x = n*i;
            while(x)
            {
                occ[x%10] = 1;
                x /= 10;
            }
            f = 1;
            for(int k = 0; k <= 9; k++)
            {
                if(occ[k] == 0)
                {
                    f = 0;
                    break;
                }
            }
            if(f == 1)
            {
                cout<<"Case #"<<j<<": "<<n*i<<endl;
                break;
            }
        }

    }
    return 0;
}

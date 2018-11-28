#include <bits/stdc++.h>
using namespace std;
typedef long long ll ;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin >> T ;
    for (int t=1;t<=T;t++)
    {
        ll n,no ;
        cin >> n ;
        no= n ;
        if (n==0)
            cout << "Case #" <<t <<": INSOMNIA" << endl ;
        else
        {
            int tab[10]={0};
            int cpt=0 ;
            while (cpt<10)
            {
                ll a=n ;
                while (a!=0 && cpt <10)
                {
                    int x = a%10 ;
                    a/=10;
                    //cout << a << endl ;
                    if (tab[x]==0)
                    {
                        tab[x]++;
                        cpt++ ;
                    }
                }
                if (cpt < 10)
                {
                    n+=no ;
                }
            }
            cout << "Case #" <<t <<": "<< n<< endl ;
        }
    }
    return 0;
}

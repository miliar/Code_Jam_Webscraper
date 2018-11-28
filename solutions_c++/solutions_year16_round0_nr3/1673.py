#include <bits/stdc++.h>

using namespace std;

#define ld long double
#define pld pair<ld,ld>
#define ff first
#define ss second
#define vpld vector<pld>
#define pb push_back
#define LL long long
#define MOD 1000000007
#define rep(i,a,b) for(LL i = a; i<=b ; ++i)

LL isp[200005];

LL divv[22];

LL t;

int main()
{
    LL n = 32;
    LL j = 500;

    LL cnt = 0;
    cin >> t >> n >> j;
    cout << "Case #1:\n";
    for(LL num = (1LL<<31);num < (1LL<<32);++num)
    {
        for(int i = 1; i<=10 ; ++i)divv[i] = 0;

        if((num & (1LL<<31)) && (num%2))
        {
            int fl = 0;

            for( LL base = 2LL; base<=10 ; ++base)
            {
                for(LL divi = 2LL ; divi<=50;++divi)
                {
                LL sum = 0;

                LL prod = 1;

                for(LL bm = 0 ; bm<=31 ; ++bm)
                {
                    if(num & (1LL<<bm))
                    {
                        sum+=prod;
                        sum%=divi;
                    }
                    prod*=base;
                    prod%=divi;
                }
                if(sum == 0)
                {
                    divv[base] = divi; 
                    break;
                }
                }
            }
        }
        int ff = 0;

        for(int base = 2;base<=10;++base)
        {
            if(divv[base]==0)ff=1;
        }

        if(ff)
        {
            continue;
        }

        for(int i =31;i>=0;--i)
        {
            if(num & (1LL<<i))
            {
                cout <<1;
            }
            else
                cout << 0;
        }
        cout <<" ";
        for(int i = 2; i<=10  ;++i)
        {
            cout << divv[i] <<" ";
        }
        cout <<"\n";
        j--;
        if(j==0)break;
    }


    return 0;
}

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


int t;

LL n;

bool chk[21] ;

void process(LL x)
{
    while(x)
    {
        chk[x%10]=1;
        x/=10;
    }
}

int main()
{
    cin >> t;

    rep(tt,1,t)
    {
        
        memset(chk,false,sizeof(chk));

        cin >> n;
        int ff=0;
        if(n==0)
        {
            cout << "Case #"<<tt<<": INSOMNIA\n";
            continue;
        }
        else
        {
            for(LL i = 1; i<=2000000 ;++i)
            {
                process(i*n);
            
            int fl  = 0;

        for(LL i = 0 ; i<=9 ; ++i)
        {
            if(chk[i]==0)fl=1;
        }
        if(fl==0)
        {
            ff=1;
             cout << "Case #"<<tt<<": "<<i*n<<"\n";
             break;
        }
        }
        }

        if(!ff)
             cout << "Case #"<<tt<<": INSOMNIA\n";
        
    }





    return 0;
}
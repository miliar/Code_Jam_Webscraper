#include<bits/stdc++.h>
#define scd(x) scanf("%d",&x)
#define prd(x) printf("%d",x)
#define sclld(x) scanf("%lld",&x)
#define prlld(x) printf("%lld",x)
#define f_in(x) freopen(x,"r",stdin)
#define f_out(x) freopen(x,"w",stdout)

using namespace std;

typedef long long int llt;

vector<bool> digit;

void markDigits(llt n)
{
    int dig;
    while(n!=0)
    {
        dig = n %10;
        digit[dig]=true;
        n = n/10;
    }
}

bool allFound()
{
    for(int i = 0 ; i < 10 ; i++)
    {
        if(digit[i]==false)
            return false;
    }
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    int t;
    llt n;
   // f_in("ip.txt");
    //f_out("out.txt");
    cin>>t;
    for(int j = 1 ; j <= t ; j++ )
    {
        digit.assign(10,false);
        cin>>n;
        cout<<"Case #"<<j<<": ";
        if(n==0)
            cout<<"INSOMNIA";
        else
        {
            for(int i =1 ; n<=1e18 ; i++)
            {
                markDigits(n*i);
                if(allFound())
                {
                    cout<<n*i;
                    break;
                }
            }
        }
        cout<<"\n";
        digits.clear();
    }



    return 0;
}

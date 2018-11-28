#include <iostream>
#include <string.h>
#include <stdio.h>
#define ull unsigned long long
#define ll long long
using namespace std;

ull gcd(ull a,ull b)
{
    if(a%b==0)
        return b;
    else
        return gcd(b,a%b);
}

ll powerCheck(ull num)
{
   // cout<<"Num : "<<num<<endl;
    ull test=1;
    int ans=0;
    while(num>=test)
    {
     //   cout<<test<<endl;
        if(test==num)
            return ans;
        test=test<<1;
        ans++;
    }
    return -1;
}

bool checkPowerDiff(ull b,ull a)
{
    if(a<b && a%2==1)
        return true;
    else
        return false;
}

int main()
{
    int T;
    cin>>T;
    int NT=T;
    while(T--){
    ull a,b;
    bool noSol=false;
    scanf("%lld/%lld",&a,&b);
    if(a==0){
        cout<<"Case #"<<NT-T<<": "<<a<<endl;
        continue;
    }
    //cout<<a<<' '<<b<<endl;
    ull gcdab=gcd(a,b);
    a=a/gcdab;
    b=b/gcdab;
    ll denPower=powerCheck(b);
    //cout<<denPower<<endl;
    if(denPower==-1)
    {
        cout<<"Case #"<<NT-T<<": "<<"impossible"<<endl;
    }
    else
    {
        if(checkPowerDiff(b,a))
        {
            double numAns=(double)b/a;
            ull ansF=0;
            double fAns=1;
            while(fAns<numAns)
            {
                ansF++;
                fAns=fAns*2;
            }
            cout<<"Case #"<<NT-T<<": "<<ansF<<endl;
        }
        else
            cout<<"Case #"<<NT-T<<": "<<"impossible"<<endl;
    }

    }


}

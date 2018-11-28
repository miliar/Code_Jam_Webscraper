
#include <bits/stdc++.h>
using namespace std;
#define ll long long
string decm(int number)
{
    string result = "";

    do
    {
        if ( (number & 1) == 0 )
            result += "0";
        else
            result += "1";

        number >>= 1;
    } while ( number );

    reverse(result.begin(), result.end());
    return result;
}
ll conver(ll num,ll b)
{
    ll bin, dec = 0, rem, base = 1;
    cin >> num;
    bin = num;
    while (num > 0)
    {
        rem = num % 10;
        dec = dec + rem * base;
        base = base * b;
        num = num / 10;
    }
    //cout << "The decimal equivalent of " << bin << " : " << dec << endl;
    return dec;

}   
bool notprime(ll num){

    if(num < 2) return true;
    if(num == 2) return false;
    if(num % 2 == 0) return true;
    for(ll i=3; (i*i)<=num; i+=2){
        if(num % i == 0 ) return true;
    }
    return false;

}
int main ()
{
   // bitset<64> s (std::string("000000"));string st;
    ll t,j,k,l,m,n;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n>>j;
        printf("Case #%lld:\n",k);
        n=pow(2,n-1);ll g=n;
       //m=stoll(decm(n+1));
        //cout<<n<<endl;
       // cout<<m<<endl;
        while(j)
        {
            m=stoll(decm(n+1));
            if(m%10==1&&notprime(conver(m,2))&&notprime(conver(m,3))&&notprime(conver(m,4))&&notprime(conver(m,5))&&notprime(conver(m,6))&&notprime(conver(m,7))&&notprime(conver(m,8))&&notprime(conver(m,9))&&notprime(conver(m,10)))
            {
                cout<<m<<" ";
                for(ll d=2;d<=10;d++)
                {
                    l=conver(m,d);
                    ll q;
                    for(q=2;q<l;q++)
                    {
                        if(l%q==0)
                        {
                            cout<<q<<" ";
                            break;
                        }
                    }
                }
                cout<<endl;
                j--;
            }
            n++;
        }
    }
}
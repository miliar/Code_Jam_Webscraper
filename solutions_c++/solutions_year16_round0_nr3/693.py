#include <iostream>
using namespace std;
string tobin(int k,int d)
{
    string ret="";
    while (d--)
    {
        ret=((k&1)?'1':'0')+ret;
        k>>=1;
    }
    return ret;
}
long long power(int b,int p)
{
    long long ret=1;
    while (p--) ret*=b;
    return ret;
}
int main()
{
    int t,n,j,b,k,i;
    long long d;
    string s;
    cin>>t>>n>>j;
    cout<<"Case #"<<t<<":"<<endl;
    for (k=0;k<j;k++)
    {
        s=tobin(k,n/2-2);
        s='1'+s+'1';
        cout<<s<<s;
        for (b=2;b<=10;b++)
        {
            d=0;
            for (i=0;i<s.size();i++) d+=(s[i]-'0')*power(b,s.size()-1-i);
            cout<<" "<<d;
        }
        cout<<endl;
    }
    return 0;
}

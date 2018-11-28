#include<bits/stdc++.h>
#define ll long long
using namespace std;
bool allplus(string x)
{
    ll len=x.length();
    ll flag=0;
    for(ll i =0; i<len; i++)
    {
        if(x[i]=='+')
            flag=1;
        else
        {
            flag=0;
            break;
        }
    }
    if(flag==1)
        return true;
    else
        return false;
}
bool allminus(string x)
{
    ll len=x.length();
    ll flag=0;
    for(ll i =0; i<len; i++)
    {
        if(x[i]=='-')
            flag=1;
        else
        {
            flag=0;
            break;
        }
    }
    if(flag==1)
        return true;
    else
        return false;
}
int main()
{
    ll t;
    cin>>t;
    for(ll x=1; x<=t; x++ )
    {
        string str;
        cin>>str;
        ll len = str.length();
        if(len == 1 and str == "+")
        {
            cout<<"Case #" << x <<  ": " <<  "0"<<endl;
            continue;
        }
        else if(len == 1 and str == "-")
        {
            cout<<"Case #" << x <<  ": " <<  "1"<<endl;
            continue;
        }
        else if(allplus(str))
        {
            cout<<"Case #" << x <<  ": " <<  "0"<<endl;
            continue;
        }
        else if(allminus(str))
        {
            cout<<"Case #" << x <<  ": " <<  "1"<<endl;
            continue;
        }
        ll count1 =0,flag =0;
        for(ll i =0; i<=len-1; i++)
        {
            if((str[i] == '+' and str[i+1] == '-') || (str[i] == '-' and str[i+1] == '+'))
            {
                //cout<<str[i];
                for(ll k=0; k<=i; k++)
                {
                    if(str[k] == '+')
                    {
                        str[k] = '-';
                    }
                    else
                    {
                        str[k] = '+';
                    }
                }
                count1++;
            }
            else if(allplus(str))
            {
                break;
            }
            else if(allminus(str))
            {
                count1++;
                break;
            }

        }
        cout<<"Case #"<<x<<": "<<count1<<endl;

    }
    return 0;
}

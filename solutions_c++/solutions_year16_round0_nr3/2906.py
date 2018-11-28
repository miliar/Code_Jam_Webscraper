#include<iostream>
#include<cmath>
#include<stdlib.h>
using namespace std;

#define ll unsigned long long

void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}
char* itoa(int num, char* str, int base)
{
    int i = 0;
    bool isNegative = false;

    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }


    if (num < 0 && base == 10)
    {
        isNegative = true;
        num = -num;
    }

    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }


    if (isNegative)
        str[i++] = '-';

    str[i] = '\0';


    reverse(str, i);

    return str;
}

ll mulmod(ll a, ll b, ll mod)
{
    ll x = 0,y = a % mod;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            x = (x + y) % mod;
        }
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}

ll modulo(ll base, ll exponent, ll mod)
{
    ll x = 1;
    ll y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}


bool Miller(ll p,int iteration)
{
    if (p < 2)
    {
        return false;
    }
    if (p != 2 && p % 2==0)
    {
        return false;
    }
    ll s = p - 1;
    while (s % 2 == 0)
    {
        s /= 2;
    }
    for (int i = 0; i < iteration; i++)
    {
        ll a = rand() % (p - 1) + 1, temp = s;
        ll mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1)
        {
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }
        if (mod != p - 1 && temp % 2 == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    ll l=0,n,j1;
    cin>>l;
    cin>>n;
    cin>>j1;

    char a[64];
    ll x[9],out[9],y=0;
    int flag=0;
cout<<"Case #1:\n";
    for(ll i=(pow(2,n-1)+1);i<pow(2,n);i=i+2)
    {

        y=0;
        itoa(i,a,2);
        for(ll j=2;j<=10;j++)
        {
            x[y] = strtoll(a,NULL,j);

            if(Miller(x[y],5))
            {
               break;
            }
            y++;
        }
       
        if(y==9)
        {
            //cout<<a<<" ";
            for(int cnt=0;cnt<9;cnt++)
            {
                flag=0;
                if((x[cnt]%2)==0)
                {
                        //cout<<"2 ";
                        out[cnt]=2;
                        flag=1;
                }
                else
                {
                    for(int d=3;d<=sqrt(x[cnt]);d=d+2)
                    {
                        if((x[cnt]%d)==0)
                        {
                            //cout<<d<<" ";
                            out[cnt]=d;
                            flag=1;
                            break;
                        }
                    }

                }
                if(flag==0)
                {
                	//cout<<"\n";
                	break;
                }
            }
            if(flag!=0)
            {
            	//cout<<"\n";
            	 cout<<a<<" ";
            	for(int cnt1=0;cnt1<9;cnt1++)
            		cout<<out[cnt1]<<" ";
            	//cout<<"HERE"<<j1<<" ";
            	cout<<"\n";
            	j1--;
            }
        }
        if(j1==0)
            break;

    }
    return 0;
}

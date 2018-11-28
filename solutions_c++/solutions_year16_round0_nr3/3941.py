#include<iostream>
#include<stack>
#include<map>
#include<vector>
#include<queue>
#include<set>
#include<algorithm>
#include<string>
#include<iomanip>
#include<stdio.h>
#include<math.h>
#include<ctype.h>
#include<string.h>
#include<cstring>
#include<time.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define pll pair<ll,ll>
#define ppll pair<ll, pair<ll,ll> >
#define inf 1000000007

ll power(ll a, ll b)
{
    if(!b)
        return 1;
    if(b==1)
        return a;
    ll temp=power(a,b/2);
    temp*=temp;
    if(b%2)
        temp*=a;
    return temp;
}

int main()
{
    ll i,j,k,l,temp,num,b,temp1,flag,bin;
    vector<ll> v;
    
    printf("Case #1:\n");
    k=1;
    for(i=0;i<=32767;i++)
    {
        if(k>50)
            break;
        
        temp=32769+i;
        flag=0;
        for(j=2;j<=sqrt(temp);j++)//check for composite number
        {
            if(temp%j==0)
            {
                flag=1;
                break;
            }
        }
        
        if((temp&32769) == 32769 && flag)//check for set bit in first and last position
        {
            temp1=temp;
            num=l=0;
            while(temp1)
            {
                num+=power(10,l)*(temp1%2);
                temp1/=2;
                l++;
            }
            bin=num; //the jamcoin
            
            for(b=2;b<=10;b++)//jamcoins in different bases
            {
                temp1=bin;
                num=l=0;
                while(temp1)
                {
                    num+=power(b,l)*(temp1%10);
                    temp1/=10;
                    l++;
                }
                cout<<num<<" ";
                flag=0;
                for(j=2;j<=sqrt(num);j++)//check for composite number and store divisor
                {
                    if(num%j==0)
                    {
                        flag=1;
                        v.push_back(j);
                        break;
                    }
                }
                if(!flag)
                    break;
            }
            
            if(flag)
            {
                printf("%lld",bin);
                for(j=0;j<v.size();j++)
                    printf(" %lld",v[j]);
                k++;
                printf("\n");
            }
            
            v.clear();
        }
    }
}






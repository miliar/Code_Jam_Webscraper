#include<iostream>
#include<stdio.h>
#include<climits>
#include<cstring>
#include<math.h>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

vector<long long> v;


int ispalindrome(long long n)
{
    long long num,temp,temp1;
    temp=0;
    num=n;
    while(num)
    {
        temp1=num%10;
        temp*=10;
        temp+=temp1;
        num/=10;
    }
    if(n==temp)
        return 1;
    else
        return 0;
}

int main()
{
    int t;
    long long a,b;
    scanf("%d",&t);

    for(int i=1;i<=10000000;i++)
    {
        if(ispalindrome(i))
        {
            long long temp;
            temp=i;
            temp=temp*temp;
            if(ispalindrome(temp))
                v.push_back(temp);
        }
    }
    for(int i=1;i<=t;i++)
    {
        int c=0;
        scanf("%lld %lld",&a,&b);
        for(int j=0;j<v.size();j++)
        {
            if(v[j]>=a&&v[j]<=b)
                c++;
        }
        printf("Case #%d: %d\n",i,c);
    }
    return 0;
}

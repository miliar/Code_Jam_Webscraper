#include<stdio.h>
#include<iostream>
#include<deque>
#include<stdlib.h>
#include<algorithm>
#include<cmath>
#include<stack>
using namespace std;
typedef long long int ll;
bool is_palindrome(ll num)
{
    stack<int> s;
    while(num!=0)
    {
        s.push(num%10);
        num=num/10;
    }
    int digits[s.size()],k=0;
    while(!s.empty())
    {
        digits[k++]=s.top();
        s.pop();
    }
    k--;
    for(int i=0;i<=k/2;i++)
    {
        if(digits[i]!=digits[k-i])
            return false;
        return true;
    }
}
bool is_perfect_square(int num)
{
    for(int i=1;i<=sqrt(num);i++)
    {
        if(i*i==num)
            return true;
    }
    return false;
}
int main()
{
    int test_cases;
    scanf("%d",&test_cases);
    ll a,b,count=0;
    for(int j=0;j<test_cases;j++)
    {
        count=0;
        scanf("%lld%lld",&a,&b);
        for(int i=a;i<=b;i++)
        {
            if(is_palindrome(i))
            {
                if(is_perfect_square(i) && is_palindrome(sqrt(i)))
                {
                    count++;
                }
            }
        }
        printf("Case #%d: %lld\n",j+1,count);
    }
}

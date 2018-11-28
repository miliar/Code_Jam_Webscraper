#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int palindrome(int n);
int main()
{
    int t, i;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        int l, h;
        l = (int)ceil(sqrt(a));
        h = (int)floor(sqrt(b));
        int counter = 0;
        for(int j=l; j<=h; j++)
        {
            int check1 = palindrome(j);
            int temp = j*j;
            int check2 = palindrome(temp);
            if(check1==1 && check2==1)
                counter++;
        }
        printf("Case #%d: %d\n", i, counter);
    }
    return 0;
}

int palindrome(int n)
{
    int temp = n;
    int r, sum = 0;
    while(n)
    {
        r=n%10;
        n=n/10;
        sum=sum*10+r;
    }
    if(temp==sum)
        return 1;
    else
        return 0;
}

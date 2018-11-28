#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;
bool CheckForPalindrome(int x);
int main()
{
    int a,b,t,psCount=0;
    int sqrtB,sqrtA;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>a;
        cin>>b;
        psCount=0;
        sqrtA = (int)sqrt(a);
        if(sqrtA<sqrt(a))
        {
            sqrtA++;
        }
        sqrtB = (int)sqrt(b);
        for(int j=sqrtA;j<=sqrtB;j++)
        {
            if(CheckForPalindrome(j) && CheckForPalindrome(j*j))
            {
                psCount++;
            }
        }
        printf("Case #%d: %d\r\n",i,psCount);
    }
}

bool CheckForPalindrome(int x)
{
    int xRev=0,y;
    y=x;
    while(y!=0)
    {
        xRev = xRev*10 + (y%10);
        y = y/10;
    }
    if(xRev == x)
        return true;
    else
        return false;
}

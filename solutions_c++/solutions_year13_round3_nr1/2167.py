#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int n,count;
char str[1000];

int vowel(char c)
{
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
        return 1;
    return 0;
}

int check(int i,int j)
{
    int consCount=0,x=0;
    for(int k=i; k<j; k++)
    {
        if(!vowel(str[k]) && !vowel(str[k+1]))
            consCount++;
        else
            consCount=0;
        if(consCount >=n-1)
            return 1;
    }
    return 0;
}

int main()
{
    int t,tc;
    cin>>tc;
    for(t=1; t<=tc; t++)
    {
        cin>>str>>n;
        if(n==1)
        {
            count=0;
            int len=strlen(str);
            for(int i=0; i<len; i++)
            {
                for(int j=i; j<len; j++)
                {
                    if(!vowel(str[j]))
                    {
                        count += len -j;
                        break;
                    }
                }
            }
        }
        else
        {
            count=0;
            int len = strlen(str);
            for(int i=0; i<len; i++)
            {
                int temp=0;
                for(int j=i; j<len-1; j++)
                {
                    if(!vowel(str[j]) && !vowel(str[j+1]))
                        temp++;
                    else
                        temp=0;
                    if(temp >= n-1)
                    {
                        count+=len - j - 1;
                        break;
                    }
                }
            }
        }

        printf("Case #%d: %d\n",t,count);
    }
    return 0;
}

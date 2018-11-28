#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen("large.in", "rt", stdin);
    freopen("answer2.txt", "wt", stdout);
    int sum,s,i,count1,p,c[2005];
    char b[2005];
    int t;
    scanf("%d",&t);
    p=t;
    while(t--)
    {
        sum=0;
        count1=0;
        //scanf("\n%d %s",&s,b);
        cin>>s>>b;
        for(i=0;i<=s;i++)
            c[i]=b[i]-'0';
        sum=c[0];
        for(i=1;i<=s;i++)
        {
            if(i>sum)
            {
                count1+=i-sum;
                sum=i+(c[i]);
            }
            else
            {
                sum+=(c[i]);
            }
        }
        printf("Case #%d: %d\n",p-t,count1);

    }
    return 0;
}

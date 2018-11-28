#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    long long t, j=1;

    scanf("%lld", &t);

    while(t--)
    {
        long long smax, ans=0, coun=0;

        string s;

        scanf("%lld", &smax);
        cin>>s;

        for(int i=0; i<=smax; i++)
        {
            if(coun<i)
            {
               ans++;
               coun+=1;
            }
            coun+=(s[i]-'0');
        }
        printf("Case #%lld: %lld\n", j, ans);
        j++;
    }
    return 0;
}

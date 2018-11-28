#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n;
char data[2000];


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--)
    {
        cin>>n;
        cin>>data;


        int ans=0;
        int sum=0;
        for (int i=0;i<=n;++i)
        {
            if (sum<i)
            {
                ans += i-sum;
                sum = i;

            }
            sum +=data[i]-'0';
        }

        printf("Case #%d: %d\n",++cas,ans);
    }




}

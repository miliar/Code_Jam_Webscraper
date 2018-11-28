#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
main()
{
    int t,n,sum,count;
    string s;
    scanf("%d",&t);
    for(int i = 1; i<=t;i++)
    {
        count = 0;
        int flag =1;
        sum = 0;
        scanf("%d",&n);
        cin>>s;
        for(int j = 0; j<=n;j++)
        {
            //cout<<"sum "<<sum<<" count "<<count<<endl;;
            if(sum < j)
            {
                count += j - sum;
                sum += s[j]-'0' + j - sum;
            }
            else sum += s[j] - '0';
        
        }
        printf("Case #%d: %d \n",i,count);
    }
}


#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
    int t,max_level;
    string num;
    long long int sum,require;
  //  scanf("%d",&t);
   cin>>t;
   int test = t;
    while(t--)
    {
        cin>>max_level;
       // cout<<"max_level is "<<max_level<<endl;
        cin>>num;
       // cout<<"Num is : "<<num<<endl;
        sum = 0;
        require = 0;
        for(int i = 0; i <= (max_level); i++)
        {
            if(i > sum && num[i] != '0' )
            {
                require = require + (i - sum);
                sum = sum + (i - sum);
            }
            if(sum >= max_level)
                break;
            sum += num[i] - '0';
 //           printf("%lld %d\n",sum,require);
        }
        printf("Case #%d: %lld\n",(test-t),require);
    }
    return 0;
}


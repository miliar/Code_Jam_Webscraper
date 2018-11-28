#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int return_num_added(int s_max)
{
 string a;
 cin>>a;
 int num_present=a[0]-'0';
 int num_req;
 int num_added=0;
 for(int i=1;i<=s_max;i++)
 {
     num_req=i;
     if(a[i]-'0'==0)
        continue;
        int temp;
     if(num_req>num_present)
     {
         num_added=(num_req-num_present)+num_added;
         temp=num_req-num_present;
         num_present=num_present+temp;
     }
     num_present=num_present+a[i]-'0';
 }
return num_added;

}
int main()
{
    int t;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        int s_max;
        scanf("%d",&s_max);
        int ans;
        ans=return_num_added(s_max);
        printf("Case #%d: %d\n",cas,ans);
        cas=cas+1;
    }
    return 0;
}

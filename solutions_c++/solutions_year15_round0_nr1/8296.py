#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,s,k=1;
    char a[1009];
    cin>>t;
    while(t)
    {
         int stand=0,need=0,diff=0;
         cin>>s>>a;
         stand=a[0]-'0';
         for(int i=1;i<=s;)
         {
             if(stand>=i)
             {
                 stand+=(a[i]-'0');
                 i++;
             }
             else
             {
                 need+=i-stand;
                 diff=i-stand;
                 stand+=diff;
             }
         }
         cout<<"Case #"<<k<<": ";
         cout<<need<<endl;
         k++;
         t--;
    }

return 0;
}

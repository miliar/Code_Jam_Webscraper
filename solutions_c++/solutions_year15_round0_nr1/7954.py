#include<iostream>
using namespace std;
int main()
{
 int test,n,var=1;
 cin>>test;
 while(test){
     cin>>n;
     char a;
     int count=0,ans=0;
     for(int i=0;i<=n;i++)
     {
       cin>>a;
       int temp=a-48;
       if(i>count && temp)
       {
		 ans=ans+i-count;
		 count+=(i-count);
		 }
       count+=temp;
     }
     cout<<"Case #"<<var<<": "<<ans<<"\n";
     test--;
     var++;
 }
 return 0;
}

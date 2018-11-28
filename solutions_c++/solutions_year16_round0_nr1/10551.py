#include<iostream>
using namespace std;

int main()
{
long long int num,n,i,a[10],sum,count,inc,pt,t,p,ans;

cin>>t;
for(p=1;p<=t;p++)
{
for(i=0;i<10;i++)
a[i]=0;
cin>>num;
cout<<"Case"<<" "<<"#"<<p<<":"<<" ";
if(num==0)
cout<<"INSOMNIA"<<endl;
else
{
inc=0;

        do
       {
        count=0;
       pt=++inc*num;
      ans=pt;
         while(pt>0)
           { 
               n=pt%10;
               a[n]=1;
               pt=pt/10;
            }
for(i=0;i<10;i++)
{
if(a[i]==1)
count++;
}

      }while(count<10);
cout<<ans<<endl;
}

}
return 0;
}
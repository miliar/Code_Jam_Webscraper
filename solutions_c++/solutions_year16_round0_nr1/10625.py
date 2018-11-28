#include<iostream>
using namespace std;

int main()
{
long long int nu,n,i,a[10],coun,inc,pt,tc,p,an;

cin>>tc;
for(p=1;p<=tc;p++)
{
for(i=0;i<10;i++)
a[i]=0;
cin>>nu;
cout<<"Case"<<" "<<"#"<<p<<":"<<" ";
if(nu==0)
cout<<"INSOMNIA"<<endl;
else
{
inc=0;

        do
       {
        coun=0;
       pt=++inc*nu;
      an=pt;
         while(pt>0)
           { 
               n=pt%10;
               a[n]=1;
               pt=pt/10;
            }
for(i=0;i<10;i++)
{
if(a[i]==1)
coun++;
}

      }while(coun<10);
cout<<an<<endl;
}

}
return 0;
}
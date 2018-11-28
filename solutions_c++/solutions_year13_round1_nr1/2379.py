#include<iostream.h>
#include<math.h>
int func()
{int r,t,c=0,d;

cin>>r>>t;
d=(pow((r+1),2)-pow(r,2) );
while(d<=t)
{c++;r=r+2 ;t=t-d;d=(pow((r+1),2)-pow(r,2) );}
return c;

}







void main()
{ int n,a[1000],k=0;
cin>>n;
for(int i=0;i<n;i++)
a[k++]=func();

for(int j=0;j<k;j++)
cout<<"Case #"<<j+1<<": "<<a[j]<<endl;
}
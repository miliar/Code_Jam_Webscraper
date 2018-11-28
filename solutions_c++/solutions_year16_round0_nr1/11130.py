#include "iostream"
#include "math.h"
using namespace std;
int a[13]={0},t,ans=0,y=0,k;
long n,r;
void check()
{
for(int i=0;i<10;i++)
cout<<a[i]<<"  ";
cout<<"\n"<<"  "<<n<<"  "<<r<<"  "<<ans<<endl;
} 
void initialize()
{
for(int i=0;i<10;i++)
a[i]=0;
r=0,y=0;
}
void check(int f)
{
switch(f){
case 0:a[0]++;break;
case 1:a[1]++;break;
case 2:a[2]++;break;
case 3:a[3]++;break;
case 4:a[4]++;break;
case 5:a[5]++;break;
case 6:a[6]++;break;
case 7:a[7]++;break;
case 8:a[8]++;break;
case 9:a[9]++;break;
}
}
void breakit(int n)
{
long f=n,a=n;
int i=0,o=0;
while(f>9)
{f/=10;
i++;
}
check(f);
for(int j=i;j>-1;j--){
f=a/pow(10,j);
check(f);
o=pow(10,j);
a=a%o;}
}
void result(int n)
{
for(int i=0;i<10;i++)
{if(a[i]<1)
{ans=0;break;}
else
ans=1;}
if(ans==1)
cout<<"Case #"<<k+1<<": "<<(y+1)*r<<endl;
}
void start(int n)
{//check();
breakit(n);
//check();
result(n);
//check();
if((ans==0)&&(n==n+r))
cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;
else if(ans==0)
{y++;start(n+r);}

//check();
}
int main()
{
cin>>t;
for(k=0;k<t;k++)
{
initialize();
cin>>n;
r=n;
start(n);

}
return 0;
}

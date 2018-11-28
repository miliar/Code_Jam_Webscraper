#include<bits/stdc++.h>
using namespace std;
int ar[10]={0,0,0,0,0,0,0,0,0,0};

int isLeft()
{
for(int i=0;i<10;i++)
{
if(ar[i]==0)
return 1;
}
return 0;
}
void digits(int n)
{
while(n>0)
{
ar[n%10]=1;
n=n/10;
}

}

int main()
{
long long int t,n,i=1;
cin>>t;
while(i<=t)
{
cin>>n;
for(int j=0;j<10;j++)
ar[j]=0;
printf("Case #%lld: ",i);
int p=0;
if(n==0)
cout<<"INSOMNIA\n";
else
{
while(isLeft())
{
p++;
digits(p*n);
}
cout<<p*n<<endl;
}
i++;
}



return 0;
}

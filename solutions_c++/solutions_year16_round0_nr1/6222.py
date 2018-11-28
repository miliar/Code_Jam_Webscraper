#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cassert>

using namespace std;

class checker
{
public:
int n,A[10];
checker(int num)
{
n=num;
for(int i=0;i<10;i++)
A[i]=0;
}
void divider(int nu)
{
if(nu==0)
return;
int k;
k=nu%10;
A[k]=1;
nu=nu/10;
divider(nu);
}
int check(int p,int q)
{
int y=p*q;
divider(y);
for(int i=0;i<10;i++)
{
if(A[i]==0)
return 0;
}
return 1;
}

int finalcheck()
{
int o=n,w=0,e=0;
if(o==0)
return 0;
while(e==0)
{
w++;
e=check(o,w);
}
return o*w;
}

};
int main()
{
FILE *fin=freopen("A-large.in","r",stdin);
assert(fin!=NULL);
FILE *fout=freopen("A-large.out","w",stdout);
int T;
cin>>T;
for(int t=1;t<=T;t++)
{
int no;
cin>>no;
checker c(no);
int s=c.finalcheck();
cout<<"Case #"<<t<<": ";
if (s==0)
cout<<"INSOMNIA"<<endl;
else
cout<<s<<endl;

} 
return 0;
}

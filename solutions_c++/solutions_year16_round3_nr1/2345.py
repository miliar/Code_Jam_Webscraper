#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cassert>
#include<cmath>

using namespace std;

class senate{
public:
int a[27],n;
string c;
senate()
{
cin>>n;
for(int i=1;i<=n;i++)
cin>>a[i];
c="#ABCDEFGHIJKLMNOPQRSTUVWXYZ";
}


void sort()
{
for(int p=1;p<=n-1;p++)             // Loop for Pass
{

for(int j=1;j<=n-1;j++)
{
if(a[j]<a[j+1])
{
int temp=a[j];                      // Interchange Values
a[j]=a[j+1];
a[j+1]=temp;
char t=c[j];
c[j]=c[j+1];
c[j+1]=t;
}
}

}

}

void display()
{
sort();
if(a[1]==0)
return;
if(n>2)
{
if(a[1]==a[2] && a[2]==a[3])
{
cout<<c[1]<<" ";
a[1]--;
display();
}
else if(a[1]==a[2])
{
cout<<c[1]<<c[2]<<" ";
a[1]--;
a[2]--;
display();
}
else
{
cout<<c[1]<<c[1]<<" ";
a[1]-=2;
display();
}
}
else
{
cout<<c[1]<<c[2]<<" ";
a[1]--;
a[2]--;
display();
} 
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
senate s;
cout<<"Case #"<<t<<": ";
s.display();
cout<<endl;
} 
return 0;
}

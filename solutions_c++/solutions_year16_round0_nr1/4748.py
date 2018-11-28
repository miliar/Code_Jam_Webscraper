#include <bits/stdc++.h>

using namespace std;
bool chk(bool a[10])
{int i;
for(i=0;i<10;i++)
{
if(a[i]==false) break;

}
if(i==10) return true;
else return false;

}

int main()
{
int t;
cin >> t;
int y=1;
while(t--)
{
long long int a;

cin >> a;
long long int p=a;
bool c[10];
for(int i=0;i<10;i++)
{
c[i]=false;
}
if(a!=0)
{
do
{
long long int temp=p;
while(p!=0)
{
int k=p%10;
c[k]=true;
p=p/10;
}
p=temp+a;
}while(chk(c)!=true);

cout << "Case #"<<y<<": "<<p-a<<endl;
}


else
cout << "Case #"<<y<<": "<<"INSOMNIA"<<endl;

y++;
}
}

#include<iostream>
using namespace std;
int main()
{
int a[1000000]={1,4,9,121,484};
int T;
cin>>T;
int x=1;
while(T--)
{
int A,B;
cin>>A>>B;
int i;
for(i=0;i<5;i++)
{
if(A>a[i])
continue;
else break;
}
int count=0;
for(int j=i;j<5;j++)
if(a[j]<=B)
count++;
else break;
cout<<"Case #"<<x<<": "<<count<<endl;
x++;
}

return 0;
}

#include<iostream>
using namespace std;
int A[]={1,4,9,121, 484, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 1234567897654321, 1002001, 10201, 100020001, 10000200001, 1000002000001};
int main()
{
int N,TC=1;
cin>>N;
while(N--)
{
int X,Y,cnt=0;
cin>>X>>Y;
for(int i=0;i<17;i++)
{
if(A[i]>=X && A[i]<=Y)
cnt++;
}
cout<<"Case #"<<TC++<<": ";
cout<<cnt<<endl;
}
return 0;
}
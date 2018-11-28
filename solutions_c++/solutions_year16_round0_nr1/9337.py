#include<iostream>
#include<fstream>
using namespace std;
bool ch(bool arr[])
{
for(int i=0;i<10;i++)
{
if(arr[i]==false)
	return false;
}
return true;
}
 void f(bool arr[],long long n)
 {
 while(n!=0)
 {arr[n%10]=true;
 n/=10;
 }
 }
 void res(bool arr[])
 {
 for(int i=0;i<10;i++)
	arr[i]=false;
 }
int main(){
int t;bool arr[10];
res(arr);
ifstream input("input.txt");
input>>t;long long n;
ofstream output("output.txt");
for(int i=1;i<=t;i++)
{
	input>>n;
	if(n==0)
		output<<"case #"<<i<<": INSOMNIA"<<endl;
	else
	{long long k=1;
	while(ch(arr)!=true)
	{f(arr,k*n);
	k++;
	}
output<<"case #"<<i<<": "<<n*(k-1)<<endl;
	}
	res(arr);
}
input.close();
output.close();
}
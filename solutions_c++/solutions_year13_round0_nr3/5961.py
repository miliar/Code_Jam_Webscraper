//Problem C. Fair and Square
#include<iostream>
#include<string>
#include<vector>
using namespace std;
bool isPalin(long long int num)
{
	if(num==0) return false;
	char str[20];
	int i;
	for(i=0; num!=0; num/=10, i++)
	str[i]='0'+num%10;
	for(int j=0; j<i/2; j++)
	if(str[j]!=str[i-1-j])
	return false;
	return true;
}
int main()
{
	int t;
	cin>>t;
	vector<long long int> res;
	for(long long int i=1; i<10000000; i++)
	if(isPalin(i)&&isPalin(i*i))
	res.push_back(i);
	
	for(int tc=1; tc<=t; tc++)
	{
		long long int a,b,cnt=0;
		cin>>a>>b;
		for(int i=0;i<res.size(); i++)
		if(res[i]*res[i]>=a&&res[i]*res[i]<=b)
		cnt++;
		cout<<"Case #"<<tc<<": "<<cnt<<"\n";
	}
}
	

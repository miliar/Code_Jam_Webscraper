#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
string toString(double n)
{
	stringstream ss;
	string str;
	ss<<n;
	ss>>str;
	return str;
}
double toInt(string str)
{
	stringstream ss;
	int n;
	ss<<str;
	ss>>n;
	return n;
}
bool palindromes(double n)
{
	string str=toString(n);
	for(int i=0;i<str.size();i++)
	{
		if(str[i]!=str[str.size()-i-1])return false;
	}
	return true;
}
bool check(long long n)
{
	if(palindromes(n)==true&&palindromes(sqrt(double(n)))==true)
		return true;
	else return false ;
}
int count(int A,int B)
{
	int counter=0;
	for(int i=A;i<=B;i++)
	{
		if(check(i)==true)counter++;
	}
	return counter;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin>>TC;
	for(int T=0;T<TC;T++)
	{
		long long A,B;
		cin>>A>>B;
		cout<<"Case #"<<(T+1)<<": "<<count(A, B)<<endl;
	}
}
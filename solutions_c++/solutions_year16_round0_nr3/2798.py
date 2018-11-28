#include<iostream>
#include<vector>
using namespace std;
long long num;
vector<int> result;
bool check(long long a)
{
	for(long long i=2;i*i<=a;i++)
	{
		if(a%i==0)
		{
			result.push_back(i);
			return false;
		}
	}
	return true;
}
int j;
void convert(long long a)
{
	long long res,mult,cp;
	for(long long i=2;i<=10;i++)
	{
		mult=1;
		res=0;
		cp=a;
		while(cp>0)
		{
			res+=mult*(cp%2);
			cp/=2;
			mult*=i;
		}
		if(check(res))
		{
			result.clear();
			return;
		}
	}
	j--;
	cout<<res;
	for(int i=0;i<result.size();i++)
	{
		cout<<" "<<result[i];
	}
	cout<<"\n";
	result.clear();
}
int n;
void rek(long long pos)
{
	if(pos==n-1)
	{
		convert(num);
		return;
	}
	long long place=1;
	place<<=pos;
	if(num&place)
	{
		num-=place;
	}
	rek(pos+1);
	if(j==0)
	{
		return;
	}
	num+=place;
	rek(pos+1);
}
int main(){
	//cin.tie(NULL);
	//ios::sync_with_stdio(false);
	int t;
	cin>>t>>n>>j;
	num+=1;
	for(int i=1;i<n-1;i++)
	{
		num*=2;
	}
	num*=2;
	num++;
	rek(1);
	return 0;
}

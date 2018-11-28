#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int t;
int A, B;

bool palindrom(int a)
{
	vector<int> tmp;
	while(a!=0)
	{
		tmp.push_back(a%10);
		a/=10;
	}
	for(int i=0; i<tmp.size()/2; i++)
		if(tmp[i]!=tmp[tmp.size()-1-i])
			return false;
	return true;
}

int how_many[1001];
void fill()
{
	how_many[0]=0;
	how_many[1]=1;
	for(int i=2; i<=1000; i++)
	{
		int s=sqrt(i);
		if(s*s==i&&palindrom(s)==true&&palindrom(i)==true)
			how_many[i]=how_many[i-1]+1;
		else
			how_many[i]=how_many[i-1];
	}
}

int main()
{
	fill();
	cin>>t;
	int k=1;
	while(k<=t)
	{
		cin>>A>>B;
		int result=how_many[B]-how_many[A];
		if(how_many[A]!=how_many[A-1])
			result++;
		cout<<"Case #"<<k<<": "<<result<<"\n";	
		k++;
	}
	return 0;
}

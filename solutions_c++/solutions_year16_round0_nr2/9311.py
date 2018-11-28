#include<iostream>
using namespace std;

int mincount(string s,int k,char flip)
{
	if(k<0)
	return 0;
	if(k>=0)
	{
	if(s[k]==flip)
	return mincount(s,k-1,flip);
	else
	{
		if(flip=='+')
		flip='-';
		else
		flip = '+';
		return 1+mincount(s,k-1,flip);
	}
}
}
int main()
{
	freopen ("B-large.in","r",stdin);
    freopen("B-large1.out","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i+1<<": "<<mincount(s,s.size()-1,'+')<<endl;
	}
}

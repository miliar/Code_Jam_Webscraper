#include<bits/stdc++.h>
using namespace std;

int main()
{
freopen ("A-small-attempt0.in","r",stdin);
freopen ("2.txt","w",stdout);
int t;
	int c=1;
cin>>t;
while(t--)
{
	string s;
	cin>>s;
	int n=s.size();
	vector<char> a;
	vector<char>::iterator it;
	int max=INT_MIN;
	for(int i=0;i<n;i++)
	{	
		if(s[i]>=max)
		{
			max=s[i];
			it = a.begin();
			a.insert(it,s[i]);
		}
		else
		{
			a.push_back(s[i]);
		}
	}
	cout<<"Case #"<<c++<<": ";
	for (it=a.begin(); it<a.end(); it++)
    		cout<< *it;
	cout<<endl;
}
return 0;
}

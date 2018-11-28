#include <bits/stdc++.h>
using namespace std;
string::iterator maximum_last(string::iterator first,string::iterator last)
{
	string::iterator res=first;
	for(string::iterator it=first+1;it!= last;it++)
	{
			if(*it>=*res)res=it;
	}
	return res;
}
int main (int argc, char const* argv[])
{
	#ifndef ONLINE_JUDGE
		freopen("in","r",stdin);
		freopen("out","w",stdout);
		freopen("out_err","w",stderr);
	#else
	 //submision online
	#endif
	int t,co(1);cin>>t;
	while (t--)
	{
		string s;
		cin>>s;
		string mid,left,right;
		mid = s.substr(0,1);
		s.erase(s.begin());
		while (!s.empty())
		{
			string::iterator it = maximum_last(s.begin(),s.end());
			int index = it - s.begin();
			if(*it>=mid[0])
			{
				left.push_back(*it);
				right = s.substr(index+1,s.size()-index-1)+right;	
			}else
			{
				right = s.substr(index,s.size()-index)+right;	
			}
			s.erase(it,s.end()); 
			if(s.size()==1)
			{
				if(s[0]>mid[0])left+=s;
				else right = s+right;
				break;
			}
		}
		std::cout << "Case #" <<(co++)<<": "<<left<<mid<<right<<'\n';
	}
	return 0;
}

#include<bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int T;
	cin>>T;
	
	for(int t=1;t<=T;t++)
	{
		string S;
		cin>>S;
		
		long long l = S.length();
		
		list<char> mylist;
		
		mylist.push_back((char)S[0]);
		
		for(int i=1;i<l;i++)
		{
			if(((char)S[i])>=(*(mylist.begin())))
				mylist.push_front((char)S[i]);
			else
				mylist.push_back((char)S[i]);
		}
		
		cout<<"Case #"<<t<<": ";
		
		for (list<char>::iterator it=mylist.begin(); it!=mylist.end(); ++it)
			cout<<*it;
			
		cout<<'\n';
	}
	
	return 0;
}	

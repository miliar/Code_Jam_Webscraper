#include<iostream>
#include<deque>
using namespace std;

int main()
{
int N;
cin>>N;
for(int k=1;k<=N;k++)
{
	string S;
	cin>>S;
	deque<char> st;
	st.push_back(S[0]);
	for(int i=1;i<S.size();i++)
	{
		if(S[i]>=st.front())
		st.push_front(S[i]);
		else
		st.push_back(S[i]);
	}
	cout<<"Case #"<<k<<": ";
	while(!st.empty())
	{
		char a = st.front();
		st.pop_front();
		cout<<a;
	}
	cout<<endl;
}
return 0;
}



#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <stack>
using namespace std;
int main(int argc, char const *argv[])
{
	int T,N;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		stack<int> flip;
		string s;
		cin>>s;
		N=s.size();
		string nS;
		reverse(&s[0],&s[N]);
		//cout<<s<<endl;
		char cur=s[0];
		if(s[0]!='+')flip.push(0);
		for (int i = 1; i < N; ++i)
		{
			if(s[i]!=s[i-1])//change in sign
				flip.push(i);

		}
		cout<<"Case #"<<t+1<<": "<<flip.size()<<endl;
		/*while(!flip.empty())
		{
			cout<<flip.top()<<endl;
			flip.pop();
		}*/
		
	}
	return 0;
}
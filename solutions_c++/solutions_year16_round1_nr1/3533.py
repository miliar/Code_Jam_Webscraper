#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int count=0; count<t; count++){
		cout<<"Case #"<<count+1<<": ";
		deque<char> dq;
		string s;
		cin>>s;
		dq.push_front(s[0]);

		for (int i=1; i<s.size(); i++){
			if (s[i] < dq.front()) dq.push_back(s[i]);
			else dq.push_front(s[i]);
		}
		
		while(!dq.empty()) {
			printf("%c", dq.front());
			dq.pop_front();
		}
		cout<<endl;
	}
	

	return 0;
}
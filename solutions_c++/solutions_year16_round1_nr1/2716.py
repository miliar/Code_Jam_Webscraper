#include <bits/stdc++.h>
#include <deque>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ofstream out("out.txt");
const int maxn = 100005;

deque<char> dep;

int main()
{
	int T;
	cin>>T;
	for(int cas = 1;cas <= T;cas++){
		string s;
		cin>>s;
		dep.push_front(s[0]);
		for(int i = 1;i < s.length();i++){
			if(s[i] >= dep.front())
				dep.push_front(s[i]);
			else dep.push_back(s[i]);
		}
		out<<"Case #"<<cas<<": ";
		while(!dep.empty()){
			out<<dep.front();
			dep.pop_front();
		}
		out<<endl;
	}
}

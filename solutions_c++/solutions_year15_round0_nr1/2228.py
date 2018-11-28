#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

#define FROM_FILE

int T;

void prepare()
{
	ios_base::sync_with_stdio(0);
#ifdef FROM_FILE
	freopen("E:\\in.txt", "r", stdin);
	freopen("E:\\out.txt", "w", stdout);
#endif
}

inline long long getNumber(char ch)
{
	string s("");
	s+=ch;
	return atol(s.c_str());
}

long long solve(string& s)
{
	long long answer = 0;
	long long areStanding = getNumber(s[0]);
	for(int i=1; i<s.size(); ++i)
	{
		long long curr = getNumber(s[i]);
		if(i > areStanding)
		{
			answer+= (i - areStanding);
			areStanding+= (i - areStanding);
		}
		areStanding+=curr;
	}
	return answer;
}




int main()
{
	prepare();
	cin>>T;
	int n;
	string s;
	for(int k=0; k<T; ++k)
	{
		cin>>n;
		cin>>s;
		long long answ = solve(s);
		cout<<"Case #"<<k+1<<": "<<answ<<endl;
	}
	return 0;
}

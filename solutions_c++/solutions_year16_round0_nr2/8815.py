#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long lld;

#define SIZE 100

#define IN freopen("B-large.in","r",stdin);
#define OUT freopen("B-large.out","w",stdout);

int T;

int main()
{
	IN
	OUT
	int i,t;
	string S;

	cin >> T;
	cin.clear();
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	

	for(t=1;t<=T;t++){

		getline(cin, S);
		if(S[S.size()-1] == '\r' || S[S.size()-1] == '\n') {
			S = S.substr(0, S.size()-1);
		}

		// cout << S << endl;
		reverse(S.begin(), S.end());
		// cout << S << endl;

		stack<bool> st;

		for(i=0; i<S.size(); i++) {
			if(S[i] == '+') st.push(true);
			else st.push(false);
			// cout << st.top();
		}

		// cout << endl;

		printf("Case #%d: ",t);

		int ans = 0;
		while(true) {
			bool happy = st.top();

			int cnt = 0;
			while(st.empty() == false && st.top() == happy) {
				st.pop();
				cnt++;
			}

			if(st.empty()) {
				cout << ans + !happy << endl;
				break;
			}

			for(i=0; i<cnt; i++) {
				st.push(!happy);
			}

			ans++;
		}

	}
	return 0;
}

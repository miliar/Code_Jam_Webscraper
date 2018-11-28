// only for small!
#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

/************************/
const int MAXL=20100;
/***********************/

char S[MAXL];

int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		scanf("%s",S);
		int ans=0;
		stack<char> st;
		int L=strlen(S);
		for(int i=0;i<L;i++) {
			if(st.empty() || (st.top()!=S[i] && SZ(st)+1<=L-i-1))
				st.push(S[i]);
			else {
				ans+=(st.top()==S[i]?10:5);
				st.pop();
			}
		}
		printf("Case #%d: ",num_kase);
		printf("%d\n",ans);
	}
	return 0;
}

#include <bits/stdc++.h>
using namespace std;
#define PI 2*acos(0.0)
#define INF 1e8
#define EPSILON 1e-8
#ifdef DEBUG
#define DPRINTF(x) printf x
#else
#define DPRINTF(x) ;
#endif

typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > piii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<bool> vb;
typedef vector<string> vs;

int testNum;
int main () {
	scanf("%d ", &testNum);
	for (int tn=1; tn<=testNum; ++tn) { 
		char input[101];
		gets(input);
		input[unique(input, input+strlen(input))-input] = '\0';
		int ans = strlen(input);
		if (input[ans-1] == '+') --ans;
		printf("Case #%d: %d\n",tn, ans);
	}
	return 0;
}



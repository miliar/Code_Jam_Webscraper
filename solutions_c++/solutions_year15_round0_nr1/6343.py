#include <bits/stdc++.h>
using namespace std;

#define ALL(p) p.begin(),p.end()
#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define MX 1002

char a[MX], b[MX];

int main() {
	// READ("input.cpp");
	// READ("A-Large.in");
	// WRITE("Output.txt");
	int t;
	scanf("%d",&t);
	int max = t;
	while(t--){
		CLR(a);
		CLR(b);
		int smax;
		scanf("%d",&smax);
		scanf("%s",a);
		long long int needed=0,have=0,i=1,diff=0;
		have = a[0]-'0';
		while(i<=smax){
			if (i<=have)
			{
				//more will stand so add a[i] to have
				have+=a[i]-'0';
				i++;
			}else{
				//we will need more to make ishyed ppl stand so increase have and needed by diff
				diff = i - have;
				have += diff;
				needed +=diff;
			}
		}
		printf("Case #%d: %d\n",max-t,needed);
	}
	return 0;
}

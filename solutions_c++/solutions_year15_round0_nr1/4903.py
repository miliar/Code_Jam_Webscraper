#include <cstdio>
int main()
{
	freopen("input-large.txt", "r", stdin);
	freopen("output-large.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		int smax;
		scanf("%d", &smax);
		char temp[smax];
		int ss[smax], ps = 0, fr = 0;
		scanf("%s", temp);
		for(int j=0; j<=smax; j++){
			ss[j] = temp[j]-'0';
		}
		for(int j=0; j<=smax; j++){
			if(ps<j){
				fr += j-ps;
				ss[j] += j-ps;
			}
			ps += ss[j];
		}
		printf("Case #%d: %d\n", i, fr);
	}
	return 0;
}
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
double a[1000], b[1000];

int main()
{
	//freopen("PD.txt", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("PD_b.out", "w", stdout);
	int TN, i, N, ca=1;
	scanf("%d", &TN);
	while(TN--){
		scanf("%d", &N);
		for(i=0;i<N;i++)scanf("%lf", &a[i]);
		for(i=0;i<N;i++)scanf("%lf", &b[i]);
		sort(a, a+N);
		sort(b, b+N);
		int aw=0, bw=0, sa=0, ea=N-1, sb=0, eb=N-1;
		while(sa<=ea){
			if(a[ea]>b[eb]){
				aw++;ea--;eb--;
			}
			else if(a[sa]<b[eb]){
				sa++;eb--;
			}

		}
		sa=0, ea=N-1, sb=0, eb=N-1;
		while(sb<=eb){
			if(b[eb]>a[ea]){
				bw++;ea--;eb--;
			}
			else if(b[sb]<a[ea]){
				sb++;ea--;
			}
			
		}
		printf("Case #%d: %d %d\n", ca++, aw, N-bw);
	}

	return 0;
}
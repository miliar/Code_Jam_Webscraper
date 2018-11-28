#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int N, S[1005], B[1005];

#define MAXN 1000000
#define CMP(a,b) ((a)<(b)) // 把a>b视为逆序，按照a<b排序
typedef long long ll; // 逆序数最大类型
typedef int T; // 比较元素类型

ll mgsort(int n, T a[]) { // 返回逆序数
    static T sav[1005];
    int l = n >> 1, r = n - l, i, j;
    ll ret = (r > 1 ? (mgsort(l, a) + mgsort(r, a + l)) : 0);
    for (i = j = 0; i <= l; sav[i + j] = a[i], i++)
        for (ret += j; j < r && (i == l || CMP(a[l + j], a[i])); sav[i + j] = a[l + j], j++);
    //memcpy(a, sav, sizeof (T) * n); // 同时排序返回，不需排序不要此步
    return ret;
}

ll mgsort2(int n, T a[]) { // 返回逆序数
	//printf("(( %d %d %d ))", a[0], a[1], a[2]);
    static T sav[1005];
    int l = n >> 1, r = n - l, i, j;
    ll ret = (r > 1 ? (mgsort2(l, a) + mgsort2(r, a + l)) : 0);
    for (i = j = 0; i <= l; sav[i + j] = a[i], i++)
        for (ret += j; j < r && (i == l || !CMP(a[l + j], a[i])); sav[i + j] = a[l + j], j++);
    //memcpy(a, sav, sizeof (T) * n); // 同时排序返回，不需排序不要此步
    return ret;
}


int main() {
	int T,Cas=0;
	scanf("%d",&T);
	while (T--) {
		scanf("%d",&N);
		int hd=0, at=-1;
		for (int i=0;i<N;i++) {
			scanf("%d",S+i);
		}
		ll tot=0;
		int l=0,r=N-1;
		for (int SSS=0;SSS<N;SSS++) {
			at=l;
			//puts("0");
			for (int i=l+1;i<=r;i++) {
				if (S[at]>S[i])
					at=i;
			}
			//puts("1");
			int save=S[at];
			if (at-l<=r-at) {
				for (int i=at-1;i>=l;i--)
					S[i+1]=S[i];
				S[l]=save;
				tot+=at-l;
				l++;
			} else {
				for (int i=at;i<r;i++)
					S[i]=S[i+1];
				S[r]=save;
				tot+=r-at;
				r--;
			}
			//printf("%d %d %lld\n", at, save, tot);
		}
		printf("Case #%d: %lld\n",++Cas,tot);
	}
}

/*

1
5
1 8 10 3 7

*/

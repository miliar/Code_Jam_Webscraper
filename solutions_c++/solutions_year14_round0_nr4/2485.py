#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
typedef pair<int,int> par;
double ar[1005],ar2[1005];
int main(){
	int t;
	scanf("%d",&t);
	int T=0;
	while(t--){T++;
		printf("Case #%d: ",T);
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&ar[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&ar2[i]);
		sort(ar,ar+n);
		sort(ar2,ar2+n);
		int p=0;
		for(int i=0;i<n;i++)
			if(ar[i]>ar2[p])p++;
		printf("%d ",p);
		p=0;
		int i;
		for(i=0;i<n;i++){
			for(p;p<n;p++){
				if(ar[i]<ar2[p])break;
				}
			if(p==n)break;
			p++;
			}
		printf("%d\n",n-i);
		}
    return 0;
    }

#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
double a[1010],b[1010];
int dcmp(double x){ 
    if(fabs(x)<1e-9) return 0;
	if(x>0) return 1;
	return -1;
}
int main(){ 
	//freopen("D--large.in","r",stdin);
	//freopen("D--large.out","w",stdout);
    int T,n;
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++){ 
	    scanf("%d",&n);
		for(int i=1;i<=n;i++)
			scanf("%lf",&a[i]);
		for(int i=1;i<=n;i++)
			scanf("%lf",&b[i]);
        sort(a+1,a+1+n);
		sort(b+1,b+1+n);
		int ans1=n,ans2=n;
        for(int i=n,j=1,h=n;i>=1;i--){ 
		    if(dcmp(a[h]-b[i])>0){ 
			    h--;
				continue;
			}else{ 
			    ans1--;
				j++;
			}
		}
		int j=1;
		for(int i=1;i<=n;i++){
			if(j>n) break;
			for(;j<=n;){ 
			    if(dcmp(a[i]-b[j])<0){
					ans2--;
					j++;
					break;
				}else{ 
				    j++;
				}
			}
		}
		printf("Case #%d: %d %d\n",kase,ans1,ans2);
	}
	return 0;
}

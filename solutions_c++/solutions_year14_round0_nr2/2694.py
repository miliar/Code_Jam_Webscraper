#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
typedef pair<int,int> par;
int ar[10];
int main(){
	int t;
	scanf("%d",&t);
	int T=0;
	while(t--){T++;
		double c,f,x,s=2;
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/s,cnt=0;
		while(1){
			cnt+=c/s;
			s+=f;
			if(ans>cnt+x/s)
				ans=cnt+x/s;
			else
				break;
			}
		printf("Case #%d: %.07lf\n",T,ans);
		}
    return 0;
    }

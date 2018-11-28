#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define inf (9999999999999999LL)
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define eps 1e-8
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back	
#define mod 1000000007
#define maxn 10100

using namespace std;

struct point {
	long long x,y;
	point(long long x=0,long long y=0): x(x), y(y) {}
	long long operator%(point p){
		return x*p.y-y*p.x;
	}
	point operator-(point p){
		return point(x-p.x,y-p.y);
	}
	int quad(){
		if(x > 0 && y == 0) return 0;
		if(x > 0 && y > 0) return 1;
		if(x == 0 && y > 0) return 2;
		if(x < 0 && y > 0) return 3;
		if(x < 0 && y == 0) return 4;
		if(x < 0 && y < 0) return 5;
		if(x == 0 && y < 0) return 6;
		return 7;
	}
}

p[3030], u[3030];

int ccw(point a,point b,point c){
	//debug("ccw %lld %lld %lld %lld %lld %lld\n",a.x,a.y,b.x,b.y,c.x,c.y);
	long long ret = (b-a)%(c-a);
	//debug("ret %lld\n",ret);
	if(ret > 0) return 1;
	if(ret == 0) return 0;
	return -1;
}

point p0;

bool comp(point a,point b){

	if(a.quad() != b.quad())
		return a.quad() < b.quad();
		
	 return ccw(p0,a,b) > 0;
	 
}

main(){

		p0 = point(0,0);

		int te;
		scanf("%d",&te);
		for(int t=1;t<=te;t++){

			int n;
			scanf("%d",&n);

			for(int i=0;i<n;i++){
				long long x,y;
				scanf("%lld%lld",&x,&y);
				p[i] = point(x,y);
			}

			printf("Case #%d:\n",t);

			for(int i=0;i<n;i++){

				//debug("i=%d\n",i);
				int ans = n;
				if(n <= 3) ans = 0;

				int q = 0;
				for(int j=0;j<n;j++) if(j != i)
					u[q++] = p[j]-p[i];

				sort(u,u+q,comp);

				

				for(int a=0;a<2;a++){

					int ptr = 0;
					int fim = 0;
					
					//for(int i=0;i<q;i++)
					//debug("(%lld;%lld) ",u[i].x,u[i].y);

					while(ptr < q){

						while(1){
							int next = fim+1;
							if(next == q) next = 0;
							if(next == ptr) break;
							//debug("ccw p0 %d %d = %d\n",ptr,next,ccw(p0,u[ptr],u[next]));
							if(a==0)if(ccw(p0,u[ptr],u[next]) <= 0) break;
							if(a==1)if(ccw(p0,u[ptr],u[next]) >= 0) break;
							fim = next;
						}

						//debug("ptr %d fim %d\n",ptr,fim);

						int z;
						if(fim >= ptr) z = fim-ptr;
						else z = q - ptr + fim;
						ans = min(ans,z);

						if(fim == ptr) fim++;
						if(fim == q) fim = 0;
						ptr++;

					}

					reverse(u,u+q);

				}

				printf("%d\n",ans);

			}

		}

}
				
					

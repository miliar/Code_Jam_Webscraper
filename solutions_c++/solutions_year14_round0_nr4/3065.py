#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int a[2020],n;
int b[2020];
int amark[2020],bmark[2020];
int avalue,bvalue;
int ascore,bscore,checker,r,june,poi;
double in;
void amarkr(){
	ascore=0;
	bscore=0;
	memset(bmark,0,sizeof(bmark));
	for(int i=1;i<=n;i++){
		avalue=a[i];
		checker=1;
		for(int j=1;j<=n;j++){
			if(bmark[j]) continue;
			bvalue=b[j];
			if(bvalue>avalue){
				checker=0;
				bmark[j]=1;
				bscore++;
				break;
			}
		}
		if(checker) ascore++;
	}
}
void damarkr(){
	ascore=0;
	bscore=0;
	int pa,pb;
	memset(bmark,0,sizeof(bmark));
	pa=n;
	pb=n;
	for(int i=1;i<=n;i++){
		avalue=a[pa];
		bvalue=b[pb];
		if(avalue>bvalue){
			pa--;
			pb--;
			ascore++;
			continue;
		}
		else{
			pb--;
		}
	}
}
void solve(){
	june++;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%lf",&in);
		in*=100000;
		a[i]=(int)in;
	}
	for(int i=1;i<=n;i++){
		scanf("%lf",&in);
		in*=100000;
		b[i]=(int)in;
	}
	sort(a+1,a+n+1);
	sort(b+1,b+n+1);
	amarkr();
	poi=ascore;
	damarkr();
	printf("Case #%d: %d ",june,ascore);
	printf("%d\n",poi);
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&r);
	while(r--) solve();
	return 0;
}
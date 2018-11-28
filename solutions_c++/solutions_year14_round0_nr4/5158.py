#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int a[2020],n;
int b[2020];
int wa[2020],wb[2020];
int va,vb;
int sa,sb,ch,r,cnt,tmp;
double in;
void war(){
	sa=0;
	sb=0;
	memset(wb,0,sizeof(wb));
	for(int i=1;i<=n;i++){
		va=a[i];
		ch=1;
		for(int j=1;j<=n;j++){
			if(wb[j]) continue;
			vb=b[j];
			//printf("%d %d\n",va,vb);
			if(vb>va){
				//printf("junewin\n");
				ch=0;
				wb[j]=1;
				sb++;
				break;
			}
		}
		if(ch) sa++;
	}
}
void dwar(){
	sa=0;
	sb=0;
	int pa,pb;
	memset(wb,0,sizeof(wb));
	pa=n;
	pb=n;
	for(int i=1;i<=n;i++){
		va=a[pa];
		vb=b[pb];
		if(va>vb){
			pa--;
			pb--;
			sa++;
			continue;
		}
		else{
			pb--;
		}
	}
}
void solve(){
	cnt++;
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
	//for(int i=1;i<=n;i++) printf("%d ",a[i]); printf("\n");
	//for(int i=1;i<=n;i++) printf("%d ",b[i]); printf("\n");
	war();
	tmp=sa;
	dwar();
	printf("Case #%d: %d ",cnt,sa);
	printf("%d\n",tmp);
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&r);
	while(r--) solve();
	return 0;
}
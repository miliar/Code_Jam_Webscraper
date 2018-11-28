#include <bits/stdc++.h>



using namespace std;





#define fr(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
typedef pair<int,int> pii;
#define F first
#define S second
#define mp make_pair
const int oo = 0x3f3f3f3f;

int t,n,c,v[100100];
bool mk[100100];

int main(){
	scanf("%d",&t);
	fr(cas,1,t+1){
		memset(mk, 0, sizeof mk);
		scanf("%d %d",&n,&c);
		fr(i,0,n){
			scanf("%d",&v[i]);
		}
		sort(v,v+n);
		int pnt2 = n-1;
		int ans = 0;
		fr(i,0,n){
			if(mk[i]) continue;
			while(pnt2 > i && (mk[pnt2] || v[pnt2] + v[i] > c)) pnt2--;
			ans++;
			mk[i] = true;
			if(pnt2 > i && v[pnt2] + v[i] <= c){
				mk[pnt2] = true;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
























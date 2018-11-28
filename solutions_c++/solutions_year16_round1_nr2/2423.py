#include<cstdio>
#include<cstring>
#include<vector>
#include<deque>
#include<algorithm>
#define CL(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(e);i++)
#define x first
#define y second
#define MAX 1005
#define INF 1<<29
#define fuck puts("fuck");

using namespace std;

int T,TC,N;
vector<vector<int> > v,va,vb;
vector<int> vr;

int group(int i){
//	printf("group %d\n",i);
	if (i==2*N-1){

		vector<vector<int> > a=(va.size()>vb.size()?va:vb),b=(va.size()>vb.size()?vb:va) , c;
//		printf("size=%d %d\n",va.size(),vb.size());
		if (abs((int)a.size()-(int)b.size()) != 1) return 0;
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		FOR(ii,0,N){
			vector<int> t;
			FOR(k,0,N) t.pb(a[k][ii]);
			c.pb(t);
		}
//		fuck;
		int dif=0,mis=N-1;
		int ii=0,j=0;
		for(;ii<N && j<N-1;ii++,j++){
			bool ok=true;
			FOR(k,0,N){
//				printf("%d vs %d\n",b[j][k],c[ii][k]);
				if (b[j][k]!=c[ii][k]) mis=ii,ok=false;
			}
//			puts("---");
			if (!ok) j--,dif++;
		}
		vr.clear();
		FOR(k,0,N) vr.pb(c[mis][k]);
//		printf("ii %d j %d dif %d\n",ii,j,dif);
//		printf("return %d\n",ii==N && j==N-1 && dif<=1);
		return (ii==N && j==N-1 && dif==1) || (ii==N-1 && j==N-1 && dif==0);
/*		bool ok = true,found=false;
	
		for(int ii=0,j=0;ii<N-1 && j<N;j++){
//			fuck;


			if (b[ii][0] == a[0][ii]){
				//	fuck;
				FOR(k,0,N){
					//	fuck;
					if (b[ii][k] != a[k][j]) {ok=false; break;}
				}
				ii++;
			} else{
				if (found) ok=false;
				found=true;
				puts("MISSING");
				vr.clear();
				FOR(k,0,N){
					vr.pb(a[k][ii]);
				}
				//	vr = b[ii];
			}
		}
		if (!found){
			vr.clear();
			FOR(k,0,N){
				vr.pb(a[k][N-1]);
			}
			found=true;

		}
*/
//		printf("return %d\n",ok && found);
//		return ok && found;
	}
	//fuck;

	bool flag = true;
	int len=va.size();
	FOR(j,0,len){
		FOR(k,0,N){
//			printf("jk %d %d\n",j,k);
			if ((v[i][0] > va[j][0] && v[i][k] > va[j][k]) || (v[i][0] < va[j][0] && v[i][k] < va[j][k])){

			} else {
				flag = false;
				break;
			}
		}
	}
	//fuck;


	if (flag) {
		va.pb(v[i]);
		//		fuck;
		if (group(i+1)) return true;
		//		fuck;
		va.pop_back();
//		puts("go on");
	}
	vb.pb(v[i]);
	if (group(i+1)) return true;
	vb.pop_back();

	return false;
}

int main(){
	scanf("%d",&T);
	while (T--){
		va.clear();
		v.clear();
		vb.clear();
		vr.clear();
		scanf("%d",&N);
		FOR(i,0,2*N-1){
			vector<int> vt;
			FOR(j,0,N){
				int t;
				scanf("%d",&t);
				vt.pb(t);
			}
			v.pb(vt);
		}
		va.pb(v[0]);
		group(1);
	//	puts("DONE");
		printf("Case #%d:",++TC);
		FOR(i,0,N) printf(" %d",vr[i]);

		/*	FOR(i,1,2*N-1){
			bool flag = true;
			FOR(j,0,i){
			FOR(k,0,N){
			if ((v[i][0] > va[j][0] && v[i][k] > va[j][k]) || (v[i][0] < va[j][0] && v[i][k] < va[j][k])){

			} else {
			flag = false;
			break;
			}
			}
			}
			if (flag) va.pb(v[i]);
			else vb.pb(v[i]);
			}
			sort(va.begin(),va.end());
			sort(vb.begin(),vb.end());
			vector<vector<int> > r,c;
			if (va.size()>vb.size()) r=va,c=vb;
			else r=vb,c=va;
		 */
		//		FOR(i,0,va.size()) {FOR(j,0,N) printf("%d ",va[i][j]); puts("");}


		//		printf("%d %d\n",va.size(),vb.size());
		puts("");
	}
}

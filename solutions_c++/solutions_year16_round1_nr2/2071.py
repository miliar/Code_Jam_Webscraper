#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
#define NAME "~/Desktop/GCJ1A/B-small-attempt0"
#define UsingFile 0
const LL MOD = 1000000007;
const double PI = acos(-1.);
int w[55][55];
vector<int>F[55];
int x[55];
int y[111][55];
int v[111];
int p[55],q[55];
int n;
bool check(int i){
	for(int k=i+1;k<n;k++){
		int pe=0,qe=0;
		for(int l=0;l<F[k].SZ;l++){
			int j=F[k][l];
			if(!pe){
				int fail=0;
				for(int t=0;t<=i;t++){
					if(w[k][t]!=-1&&y[j][t]!=w[k][t])
						fail=1;
				}
				if(!fail){pe=1;continue;}
			}
			if(!qe){
				int fail=0;
				for(int t=0;t<=i;t++){
					if(w[t][k]!=-1&&y[j][t]!=w[t][k])
						fail=1;
				}
				if(!fail){qe=1;continue;}
			}
		}
		if(pe+qe!=F[k].SZ)return false;
	}
	return true;
}
int dfs(int i){	
	int j,k;
	//cout<<i<<"\n";
	//for(j=0;j<n;j++,cout<<"\n")
	//	for(k=0;k<n;k++)cout<<w[j][k]<<" ";
	if(i==n)return 1;
	k=F[i][0];
	//for(j=0;j<n;j++)cout<<y[k][j]<<" ";cout<<"\n";
	int t[55][55];
	memcpy(t,w,sizeof w);
	int fail;
	fail=0;
	p[i]=k;
	for(j=0;j<n;j++){
		if(w[i][j]!=-1&&w[i][j]!=y[k][j]){
	//		cout<<"fail@"<<i<<" "<<j<<"\n";
			fail=1;
		}
		else w[i][j]=y[k][j];
	}
	q[i]=-1;
	if(F[i].SZ>1){
		int kk=F[i][1];
		for(j=0;j<n;j++){
			if(w[j][i]!=-1&&w[j][i]!=y[kk][j])fail=1;
			else w[j][i]=y[kk][j];
		}
		q[i]=kk;
	}
	//for(j=0;j<n;j++,cout<<"\n")
	//	for(k=0;k<n;k++)cout<<w[j][k]<<" ";
	//cout<<check(i)<<" check "<<fail<<"\n";
	if(check(i)&&!fail){
		int ret=dfs(i+1);
		if(ret)return ret;
	}
	k=F[i][0];
	fail=0;
	memcpy(w,t,sizeof w);
	//cout<<i<<"?\n";
	//for(j=0;j<n;j++,cout<<"\n")
	//	for(k=0;k<n;k++)cout<<w[j][k]<<" ";
	k=F[i][0];
	q[i]=k;
	for(j=0;j<n;j++){
		if(w[j][i]!=-1&&w[j][i]!=y[k][j])fail=1;
		else w[j][i]=y[k][j];
	}
	//cout<<"==>\n";
	//for(j=0;j<n;j++,cout<<"\n")
	//	for(k=0;k<n;k++)cout<<w[j][k]<<" ";
	p[i]=-1;
	if(F[i].SZ>1){
		int kk=F[i][1];
		p[i]=kk;
		for(j=0;j<n;j++){
			if(w[i][j]!=-1&&w[i][j]!=y[kk][j])fail=1;
			else w[i][j]=y[kk][j];
		}
	}
	//for(j=0;j<n;j++,cout<<"\n")
	//	for(k=0;k<n;k++)cout<<w[j][k]<<" ";
	//cout<<check(i)<<" check\n";
	if(check(i)&&!fail){
		int ret=dfs(i+1);
		if(ret)return ret;
	}
	return 0;
}
int main(){
    //if(UsingFile)freopen(NAME".in","r",stdin);
    //if(UsingFile)freopen(NAME".out","w",stdout);
    int i,j,k,_T;
    scanf("%d",&_T);
    for(int CA=1;CA<=_T;CA++){
    	scanf("%d",&n);
    	memset(v,0,sizeof v);
    	for(i=0;i<n;i++)F[i].clear();
    	for(i=1;i<2*n;i++){
    		for(j=0;j<n;j++)
    			scanf("%d",&y[i][j]);
    	}
    	for(i=0;i<n;i++){
    		x[i]=-1;
    		for(j=1;j<2*n;j++)if(!v[j]){
    			if(x[i]==-1||x[i]>y[j][i])x[i]=y[j][i];
    		}
    		for(j=1;j<2*n;j++)if(x[i]==y[j][i])
    			F[i].PB(j),v[j]=1;
    	}
    	memset(w,-1,sizeof w);
    	int ret=dfs(0);
    	//for(i=0;i<n;i++)cout<<p[i]<<" ";cout<<"\n";
    	//for(i=0;i<n;i++)cout<<q[i]<<" ";cout<<"\n";
    	cout<<"Case #"<<CA<<":";
    	for(i=0;i<n;i++)if(p[i]==-1)
    		for(j=0;j<n;j++)cout<<" "<<w[i][j];
    	for(i=0;i<n;i++)if(q[i]==-1)
    		for(j=0;j<n;j++)cout<<" "<<w[j][i];
    	cout<<"\n";
    }
    return 0;
}
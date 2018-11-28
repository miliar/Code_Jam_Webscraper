#include<bits/stdc++.h>

#define LL long long
#define MP make_pair
#define PB push_back
#define MAXN 1000000
using namespace std;
vector<int> P;
int n,m;
bool F[MAXN+100];
void sieve(){
	memset(F,1,sizeof(F));
	F[0] = F[1] = 0;
	for(int i=2;i*i<=MAXN;i++)
		if(F[i])
			for(int j=i*i;j<=MAXN;j+=i)
				F[j] = 0;
	P.clear();
	for(int i=2;i<=MAXN;i++)
		if(F[i])
			P.PB(i);
}
int t;
vector<LL> ans[555];
map<LL,bool> mp;
LL RAND(int b){
	LL ret = 1 + (1ll<<(b-1));
	for(int i=1;i<b-1;i++)
		if(rand()%2>0)
			ret+=(1ll<<i);
	return ret;
}
vector<int> R,C,A;
void ADD(vector<int> &A,vector<int> &B){
	int a,b;
	for(int i=0;i<max(A.size(),B.size());i++){
		if(A.size()==i)	A.PB(0);
		a = A[i];
		b = (i<B.size())?B[i]:0;
		a+=b;
		
		if(a>=10){
			if(i+1==A.size())	A.PB(0);
			A[i+1]+=a/10;
		}
		A[i] =a%10;
	}
}
vector<int> CC;
void TIMES(vector<int> &A,int v){
	int a;
	int l = A.size();
	CC.clear();
	for(int i=0;i<l;i++){
		if(i==CC.size())	CC.PB(0);
		a = A[i];
		a*=v;
		a+=CC[i];
		if(a>=10){
			if(i+1==CC.size())	CC.PB(0);
			CC[i+1]+=a/10;
		}
		CC[i] = a%10;
	}
	A = CC;
}

vector<int> findValue(int val,int b){
	R.clear();
	C.clear();
	R.PB(0);	C.PB(1);
	
	for(LL i=0;i<n;i++){
		if(val&(1ll<<i)){
			ADD(R,C);
			//for(int j=0;j<R.size();j++)	cout<<R[j];
			//cout<<" |"<<i<<"| ";
			//for(int j=0;j<C.size();j++)	cout<<C[j];
			//cout<<endl;
		}
		TIMES(C,b);
	}
	reverse(R.begin(),R.end());
	return R;
}

int MODS(vector<int> &A,int v){
	int ret = 0;
	for(int i=0;i<A.size();i++){
		ret = ret*10 + A[i]-0;
		ret%=v;
	}
	return ret;
}
int cek(LL val,int I){
	vector<LL> &V = ans[I];
	V.clear();
	V.PB(val);
	A.clear();
	for(int i=2;i<=10;i++){
		A = findValue(val,i);
		if(A.size()<6){
			int v = 0;
			int c = 1;
			for(int j=0;j<n;j++){
				if(val&(1<<j))	{
					v+=c;
				}
				c*=i;
			}
			if(F[v])	return 0;
		}
		//cout<<val<<" | "<<i<<" : ";
		//for(int j=0;j<A.size();j++)	cout<<A[j];
		//cout<<endl;
		for(int j=0;j<P.size();j++){
			if(MODS(A,P[j])==0){
				V.PB(P[j]);
				break;
			}
		}
	}
	return (V.size()==10);
}

int main(){
	sieve();
	srand(time(NULL));
	scanf("%d",&t);
	for(int z=1;z<=t;z++){
		printf("Case #%d:\n",z);
		scanf("%d%d",&n,&m);
		int M = m;
		for(int i=0;i<=500;i++)	ans[i].clear();
		
		mp.clear();
		for(int i=0;i<m;i=i){
			LL r = RAND(n);
			if(mp.count(r)!=0)	continue;
			mp[r] = 1;
			if(cek(r,i)){
				i++;
			}
		}
		
		for(int i=0;i<m;i++){
			for(LL j=n-1,v=ans[i][0];j>=0;j--){
				printf("%d",(v&(1ll<<j))?1:0);
			}
			for(int j=1;j<ans[i].size();j++){
				printf(" ");
				printf("%d",ans[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
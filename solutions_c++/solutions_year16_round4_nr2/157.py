#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int MN = 200 + 5;

int N,K;
double prob[MN];
double D[MN][2*MN];
double ans;

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	int TC;
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++){
		scanf("%d%d",&N,&K);
		for(int i=0;i<N;i++){
			scanf("%lf",&prob[i]);
		}
		sort(prob,prob+N);
		ans=0;
		for(int st=0;st<N;st++){
			vector<double> probs;
			for(int i=0;i<K;i++)probs.push_back(prob[(st+i)%N]);
			for(int j=0;j<2*MN;j++)D[0][j]=0;
			D[0][MN+1]=probs[0];
			D[0][MN-1]=1-probs[0];
			for(int i=1;i<K;i++)for(int j=0;j<2*MN;j++){
				if(j==0) D[i][j]=(1-probs[i])*D[i-1][j+1];
				else if(j==2*MN-1) D[i][j]=probs[i]*D[i-1][j-1];
				else D[i][j]=probs[i]*D[i-1][j-1] + (1-probs[i])*D[i-1][j+1];
			}
			if(ans<D[K-1][MN])ans=D[K-1][MN];
		}
		printf("Case #%d: %.12lf\n",tc,ans);
	}
	return 0;
}
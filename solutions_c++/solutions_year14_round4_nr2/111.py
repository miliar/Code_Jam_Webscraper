#include <cstdio>
#include <algorithm>
#include <numeric>
using namespace std;
const int NMax=1000;
int A[NMax],N;
int dp1[NMax][NMax],dp2[NMax][NMax];
int main()
{
	int T;
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		scanf("%d",&N);
		for (int i=0;i<N;i++)
			scanf("%d",A+i);
		static pair<int,int> list1[NMax];
		for (int i=0;i<N;i++)
			list1[i]=make_pair(A[i],i);
		sort(list1,list1+N);
		for (int i=0;i<N;i++)
			A[i]=list1[i].second;
		//for (int i=0;i<N;i++)
			//printf("%d ",A[i]);
		//puts("");
		for (int i=N-1;i>=0;i--){
			for (int j=N-1;j>=i;j--){
				if (i==j){
					if (i==N-1){
						dp1[i][j]=0;
						dp2[i][j]=0;
					}else{
						dp1[i][j]=100000000;
						dp2[i][j]=100000000;
					}
				}else{
					int s1=0,s2=0;
					for (int k=i+1;k<N;k++){
						if (A[k]<A[i])
							s1++;
						else
							s2++;
					}
					if (j!=i+1)
						dp1[i][j]=dp1[i+1][j]+s1;
					else{
						int mn=100000000;
						for (int k=i+1;k<N;k++)
							mn=min(mn,dp2[i+1][k]);
						dp1[i][j]=mn+s1;
					}
					if (j!=i+1)
						dp2[i][j]=dp2[i+1][j]+s2;
					else{
						int mn=100000000;
						for (int k=i+1;k<N;k++)
							mn=min(mn,dp1[i+1][k]);
						dp2[i][j]=mn+s2;
					}
				}
				//printf("dp1 %d %d=%d\n",i,j,dp1[i][j]);
				//printf("dp2 %d %d=%d\n",i,j,dp2[i][j]);
			}
		}
		int ret=100000000;
		for (int i=0;i<N;i++)
			ret=min(ret,dp1[0][i]);
		for (int i=0;i<N;i++)
			ret=min(ret,dp2[0][i]);
		printf("Case #%d: %d\n",Case,ret);
	}
	return 0;
}


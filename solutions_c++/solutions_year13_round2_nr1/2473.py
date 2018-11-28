#include<iostream>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

int dp[2000001][101];
const int MAX_DATA=100000000;

int main(){
	
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		int A,N;
		cin>>A>>N;
		vector<int> data(N);
		int md=A;
		for(int i=0;i<N;i++){
			cin>>data[i];
			md+=data[i];
		}
		sort(data.begin(),data.end());
		
		
		for(int i=1;i<=2*md;i++)
			dp[i][0]=MAX_DATA;
		
		dp[A][0]=0;
		for(int i=0;i<N;i++){
			for(int j=1;j<=2*md;j++)
				dp[j][i+1]=MAX_DATA;
			for(int j=1;j<=2*md;j++){
				if(dp[j][i]!=MAX_DATA){
					if(j<=data[i]){
						//tuika
						if(j>1){
//							int k=(data[i]-j)/(j-1);
							int k=0,nd;
							for(nd=j;nd<=data[i];nd=2*nd-1)
								k++;
							if(dp[nd+data[i]][i+1]>dp[j][i]+k)
								dp[nd+data[i]][i+1]=dp[j][i]+k;
						}
						//sakuzyo
						if(dp[j][i+1]>dp[j][i]+1)
							dp[j][i+1]=dp[j][i]+1;
					}else{
						if(dp[j+data[i]][i+1]>dp[j][i])
							dp[j+data[i]][i+1]=dp[j][i];
					//	if(dp[j][i+1]>dp[j][i]+1)
					//		dp[j][i+1]=dp[j][i]+1;
					}
				}
			}
		}
		
		//for(int i=0;i<N+1;i++){
	//		for(int j=1;j<=2*md;j++)
	//			cout<<dp[j][i]<<" ";
	//		cout<<endl<<endl;
	//	}
		
		int result=MAX_DATA;
		for(int j=1;j<=2*md;j++)
			if(dp[j][N]<result)
				result=dp[j][N];
		cout<<"Case #"<<testcase<<": "<<result<<endl;
	}
	return 0;
}

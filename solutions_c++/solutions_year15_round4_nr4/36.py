#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
typedef long long int64;
const int maxn=110;
const int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
const int mod=1000000007;
int powmod(int a, int b) {
	int64 p=a, ans=1;
	for(int i=0;(1<<i)<=b;i++) {
		if(b&(1<<i)) ans=ans*p%mod;
		p=p*p%mod;
	}
	return ans;
}
int gcd(int a,int b) {
	return b?gcd(b,a%b):a;
}
int nrow,ncol;
int mp[100][100];
bool check(int row, int col) {
	/*for(int i=0;i<nrow;i++) {
			for(int j=0;j<ncol;j++)
				printf("%d",mp[i][j]);
			puts("");
		}
		puts("");
		scanf("%*s");*/
	col=(col+ncol)%ncol;
	if(row<0 || row>=nrow || col<0 || col>=ncol || mp[row][col]==0) {
		//printf("XX");
		return true;
		
	}
	int cnt=0;
	for(int dir=0;dir<4;dir++) {
		int row2=row+dx[dir], col2=(col+dy[dir]+ncol)%ncol;
		if(row2>=0 && row2<nrow && col2>=0 && col2<ncol && mp[row2][col2]==0) {
			//printf("XXXZ %d %d",row2,col2);
		return true;
		
	}
		if(mp[row2][col2]==mp[row][col])
			cnt++;
	}
	//printf("cnt=%d\n",cnt);
	return cnt==mp[row][col];
}
int ans2;
void search(int row, int col) {
	if(row>=nrow) {
		ans2++;
		//check(0,0);
		/*for(int i=0;i<nrow;i++) {
			for(int j=0;j<ncol;j++)
				printf("%d",mp[i][j]);
			puts("");
		}
		puts("");*/
		return;
	}
	int row2=row, col2=col+1;
	if(col2>=ncol)
		row2++, col2=0;
	
	mp[row][col]=1;
	if(check(row,col) && check(row-1,col) && check(row,col-1) && check(row,col+1))
		search(row2,col2);
	mp[row][col]=2;
	if(check(row,col) && check(row-1,col) && check(row,col-1) && check(row,col+1))
		search(row2,col2);
	mp[row][col]=0;
}

int64 dp12[maxn],dp3[maxn];
int val[maxn];
int solve(int nrow, int ncol) {
	int cnt=0, sum=0;
	for(int per=1;per<=ncol;per++) if(ncol%per==0) {
		memset(dp12,0,sizeof(dp12));
		memset(dp3,0,sizeof(dp3));
		dp12[0]=dp3[0]=1;
		for(int i=0;i<=nrow;i++) {
			dp12[i]%=mod;
			dp3[i]%=mod;
			
			dp12[i+1]+=dp3[i];
			if(per%3==0)
				dp12[i+2]+=dp3[i]*3;
			if(per%6==0)
				dp12[i+2]+=dp3[i]*6;
			if(per%4==0)
				dp12[i+3]+=dp3[i]*4;
	
			dp3[i+2]+=dp12[i];
		}
		val[per]=(dp12[nrow]+dp3[nrow])%mod;
		//printf("nrow=%d ncol=%d per=%d: %d\n",nrow,ncol,per,val[per]);
	}
	for(int per=1;per<=ncol;per++)
		sum=(sum+int64(val[gcd(per,ncol)]))%mod;
	//	printf("%lld %lld\n",dp12[nrow],dp3[nrow]);
	//}
	int ans=int64(sum)*powmod(ncol,mod-2)%mod;
	//printf("%d\n",);
	return ans;
}
void testcase() {
	int nrow, ncol;
	scanf("%d%d",&nrow,&ncol);
	printf("%d\n",solve(nrow,ncol));
}
int main() {
	//printf("%d\n",powmod(2,6));
	//for(nrow=1;nrow<=10;nrow++) {
	//for(ncol=1;ncol<=15;ncol++) {
		/*nrow=2,ncol=3;
		memset(mp,-1,sizeof(mp));
		for(int i=0;i<nrow;i++)
		for(int j=0;j<ncol;j++)
			mp[i][j]=0;
		ans2=0;
		search(0,0);
		int ans=solve(nrow,ncol);
		printf("%d,%d %d =>%d\n",nrow,ncol,ans,ans2);*/
	
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		testcase();
	}
	scanf("%*s");
	return 0;
}

#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<queue>
#include<list>
#include<vector>
#define LL long long
#define INF 0x7fffffff
#define For(i,a,b) for(int i=a; i<b; ++i)
using namespace std;
typedef pair<int,int> ii;
int main(){
	int T;
	cin>>T;
	for(int c=1; c<=T; ++c){
		int ans1;
		cin>>ans1;
		int num[16];
		For(i,0,16) num[i]=0;
		int arrange1[5][5];
		For(i,0,4) For(j,0,4) cin>>arrange1[i][j];
		
		For(i,0,4) num[arrange1[ans1-1][i]-1] = 1;

		int ans2;
		cin>>ans2;
		int arrange2[5][5];
		For(i,0,4) For(j,0,4) cin>>arrange2[i][j];
		
		int cnt = 0;
		int ans;

		For(i,0,4) if(num[arrange2[ans2-1][i]-1]==1){
			cnt++;
			ans = arrange2[ans2-1][i];
		}

		printf("Case #%d: ", c);
		if(cnt==1) cout<<ans<<endl;
		else if(cnt>1) cout<<"Bad magician!"<<endl;
		else if(cnt==0) cout<<"Volunteer cheated!"<<endl;

	}
	return 0;
}

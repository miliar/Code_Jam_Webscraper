#include<bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef vector< pair<int,int> > vpi;

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout
int dp[1000001];
int reverse(int n){
	while((n%10)==0)n=n/10;
	int rev=0;
	while(n>0){

		rev=rev*10+(n%10);
		n=n/10;
	}
	return rev;
}
int n;
int bfs(){
	queue< pair<int,int> > q;
	q.push(make_pair(1,1));
	int v[1111111];

	memset(v,0,sizeof(v));
	while(!q.empty()){
		int num=q.front().first;
		int cl=q.front().second;
		q.pop();
		if(num==n)return cl;
		if(v[num+1]==0)q.push(make_pair(num+1,cl+1));
		v[num+1]=1;

		int rev=reverse(num);
		if(v[rev]==0)q.push(make_pair(rev,cl+1));
		v[rev]=1;

		//cout<<num-1<<" "<<rev<<endl;
	}
}
int main(){
int t;
scanf("%d",&t);
while(t--){
	scanf("%d",&n);
	gout<<bfs()<<endl;
}
}

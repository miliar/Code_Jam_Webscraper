#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;

const int INF = 999999999;
const int di[] = {-1, 0, 1, 0};
const int dj[] = {0, 1, 0, -1};

struct node{
	long long a, b, c;
	node(){
		a = b = c = 0;
	}
	node(long long x, long long y, long long z){
		a = x;
		b = y;
		c = z;
	}
};

node ans[20][3];

void build(){
	ans[0][0] = node(1, 0, 0);
	ans[0][1] = node(0, 1, 0);
	ans[0][2] = node(0, 0, 1);
	// int i = 0;
	// 	cout<<ans[i][0].a<<" "<<ans[i][0].b<<" "<<ans[i][0].c<<endl;
	// 	cout<<ans[i][1].a<<" "<<ans[i][1].b<<" "<<ans[i][1].c<<endl;
	// 	cout<<ans[i][2].a<<" "<<ans[i][2].b<<" "<<ans[i][2].c<<endl;

	for(int i = 1; i<20; i++){
		ans[i][0].a = ans[i-1][0].a + ans[i-1][1].a;
		ans[i][0].b = ans[i-1][0].b + ans[i-1][1].b;
		ans[i][0].c = ans[i-1][0].c + ans[i-1][1].c;
		ans[i][1].a = ans[i-1][1].a + ans[i-1][2].a;
		ans[i][1].b = ans[i-1][1].b + ans[i-1][2].b;
		ans[i][1].c = ans[i-1][1].c + ans[i-1][2].c;
		ans[i][2].a = ans[i-1][0].a + ans[i-1][2].a;
		ans[i][2].b = ans[i-1][0].b + ans[i-1][2].b;
		ans[i][2].c = ans[i-1][0].c + ans[i-1][2].c;
		// cout<<ans[i][0].a<<" "<<ans[i][0].b<<" "<<ans[i][0].c<<endl;
		// cout<<ans[i][1].a<<" "<<ans[i][1].b<<" "<<ans[i][1].c<<endl;
		// cout<<ans[i][2].a<<" "<<ans[i][2].b<<" "<<ans[i][2].c<<endl;
	}
}

string printa(int n, int i){
	string s, t;
	if(n==0){
		if(i==0) s = "P";
		else if(i==1) s = "R";
		else s = "S";
		return s;
	}
	if(i==0){
		s = printa(n-1, 0);
		t = printa(n-1, 1);
	}else if(i==1){
		s = printa(n-1, 1);
		t = printa(n-1, 2);
	}else{
		s = printa(n-1, 0);
		t = printa(n-1, 2);
	}
	if(s<t) return s+t;
	return t+s;
}

void solvre(){
	int n;
	long long a, b, c;
	cin>>n>>b>>a>>c;

	for(int i = 0; i<3; i++){
		if(ans[n][i].a==a && ans[n][i].b==b && ans[n][i].c==c){
			cout<<printa(n, i);
			printf("\n");
			return;
		}
	}
	printf("IMPOSSIBLE\n");

}

int main(){
	int t;
	scanf("%d", &t);
	build();
	for(int i = 1; i<=t; i++){
		printf("Case #%d: ", i);
		solvre();
	}
}
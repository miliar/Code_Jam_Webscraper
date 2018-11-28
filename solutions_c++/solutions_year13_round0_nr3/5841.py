#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

int A, B;
vector<int> R;

int rev(int n){
	int r = 0;
	while( n ){
		r = r*10 + (n%10);
		n /= 10;
	}
	return r;
}

void gen(){
	int i, t;
	for(i=1; i*i<=1000; i++){
		t = i*i;
		if( t==rev(t) && i==rev(i) )
			R.push_back(t);
	}
}

int solve(){
	int c, i;
	for(i=0, c=0; i<R.size(); i++){
		if( R[i]>=A && R[i]<=B )c++;
		if( R[i]>B )break;
	}
	return c;
}


int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, cs;
	gen();
	scanf("%d", &T);
	for(cs=1; cs<=T; cs++){
		scanf("%d%d", &A, &B);
		printf("Case #%d: %d\n", cs, solve());
	}
	return 0;
}
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int multiply(int a, int b){
	//1=1, 2=i, 3=j, 4=k
	int pos = ((a < 0 && b < 0) || (a > 0 && b > 0)) ? 1 : -1;
	a = max(a,-a);
	b = max(b,-b);
	if(a == 1 && b == 1) return 1*pos;
	if(a == 1 && b == 2) return 2*pos;
	if(a == 1 && b == 3) return 3*pos;
	if(a == 1 && b == 4) return 4*pos;
	if(a == 2 && b == 1) return 2*pos;
	if(a == 2 && b == 2) return -1*pos;
	if(a == 2 && b == 3) return 4*pos;
	if(a == 2 && b == 4) return -3*pos;
	if(a == 3 && b == 1) return 3*pos;
	if(a == 3 && b == 2) return -4*pos;
	if(a == 3 && b == 3) return -1*pos;
	if(a == 3 && b == 4) return 2*pos;
	if(a == 4 && b == 1) return 4*pos;
	if(a == 4 && b == 2) return 3*pos;
	if(a == 4 && b == 3) return -2*pos;
	if(a == 4 && b == 4) return -1*pos;
}

int T,L,X,c[10010];
char ch;

class SegmentTree{
private:
	vector<int> st;
	int left(int p){ return p << 1; }
	int right(int p){ return (p << 1) + 1; }
	int build(int p, int L, int R){
		if(L == R) st[p] = c[L];
		else{
			build(left(p),L,(L+R)/2);
			build(right(p),(L+R)/2+1,R);
			st[p] = multiply(st[left(p)],st[right(p)]);
		}
	}
	int find(int p, int L, int R, int i, int j){
		if( i > R || j < L) return 0;
		if(L >= i && R <= j) return st[p];
		int p1 = find(left(p),L,(L+R)/2,i,j);
		int p2 = find(right(p),(L+R)/2+1,R,i,j);
		if(p1 == 0) return p2;
		if(p2 == 0) return p1;
		return multiply(p1,p2);
	}
public:
	SegmentTree(){
		st.assign(L*X*4,0);
		build(1,0,L*X-1);
	}
	int find(int i, int j){ return find(1,0,L*X-1,i,j); }
};

int main(){
	freopen("codejam3.in","r",stdin);
	freopen("codejam3.out","w",stdout);
	scanf("%d",&T);
	for(int k = 1; k <= T; k++){
		scanf("%d%d\n",&L,&X);
		for(int i = 0; i < L; i++){
			scanf("%c",&ch);
			if(ch == 'i') c[i] = 2;
			if(ch == 'j') c[i] = 3;
			if(ch == 'k') c[i] = 4;
		}
		int cur = L;
		for(int i = 0; i < X-1; i++){
			for(int j = 0; j < L; j++){
				c[cur] = c[j];
				cur++;
			}
		}
		vector<int> iPoints;
		vector<int> kPoints;
		cur = c[0];
		for(int i = 1; i < L*X-1; i++){
			if(cur == 2) iPoints.push_back(i);
			cur = multiply(cur,c[i]);
		}
		cur = c[L*X-1];
		for(int i = L*X-2; i > 0; i--){
			if(cur == 4) kPoints.push_back(i);
			cur = multiply(c[i],cur);
		}
		SegmentTree st;
		bool found = 0;
		for(int i : iPoints){
			for(int j : kPoints){
				if(j<i) continue;
				if(st.find(i,j) == 3) found = 1;
				if(found) break;
			}
			if(found) break;
		}
		printf("Case #%d: %s\n",k,found ? "YES" : "NO");
	}
}
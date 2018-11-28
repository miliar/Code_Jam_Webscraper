# include <bits/stdc++.h>

# define ff first
# define ss second
# define mp(x,y) make_pair(x,y)
# define tr(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
# define MAXN 10009

template<typename A, typename B> inline void amax(A &x, B y) {if(x < y) x = y;}
template<typename A, typename B> inline void amin(A &x, B y) {if(!(x < y)) x = y;}

typedef long long lld;

using namespace std;

/*
1 => 0
i => 1
j => 2
k => 3
-1 => 4
-i => 5
-j => 6
-k => 7
*/

int op[][8] = {
{0, 1, 2, 3, 4, 5, 6, 7},
{1, 4, 3, 6, 5, 0, 7, 2},
{2, 7, 4, 1, 6, 3, 0, 5},
{3, 2, 5, 4, 7, 6, 1, 0},

{4, 5, 6, 7, 0, 1, 2, 3},
{5, 0, 7, 2, 1, 4, 3, 6},
{6, 3, 0, 5, 2, 7, 4, 1},
{7, 6, 1, 0, 3, 2, 5, 4}
};

int T[MAXN*10];
bool bolyamy(int a, int b, int c, vector<int> A){
	int sz = A.size();
	int mnpos = sz+1;
	
	for(int i=0; i<sz; i++){
		if(!i)
			T[i] = A[i];
		else
			T[i] = op[T[i-1]][A[i]];
		
		if(T[i] == a  &&  mnpos == sz+1)
			mnpos = i;
	}
	
	for(int i=sz-1; i>=2; i--)
		if(T[sz-1] == op[T[i-1]][c]  &&  T[i-1] == op[a][b]  &&  mnpos < i-1)
			return 1;
	
	return 0;
}

char Z[2][3];
char S[MAXN];

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	strcpy(Z[0], "NO");
	strcpy(Z[1], "YES");
	
	int t;
	int l;
	lld x;
	vector<int> A;
	int ans;
	
	scanf("%d",&t);
	
	for(int u=0; u<t; u++){
		ans = 0;
		
		scanf("%d %lld",&l,&x);
		scanf("%s",S);
		
		A.resize(l*x);
		
		for(int j=0; j<x; j++)
		for(int i=0; i<l; i++){
			if(S[i] == '0')
				A[i+j*l] = 0;
			else
				A[i+j*l] = S[i] - 'h';
		}
		
		ans |= bolyamy(1, 2, 3, A);
		
		printf("Case #%d: %s\n",u+1,Z[ans]);
	}
}

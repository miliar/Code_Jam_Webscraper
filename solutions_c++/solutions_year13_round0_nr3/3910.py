#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<istream>
#include<algorithm>
#include<vector>
#include<map>
#include<sstream>

using namespace std;

#define ll long long
#define ull unsigned long long
#define pii pair<int,int>
#define pdd pair<double,double>
#define F first
#define S second
#define fr(i,j,k) for(int (i)=(j);(i)<(k);++(i))
#define rep(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define PI acos(-1)
#define db(x) cerr << #x << " = " << x << endl;
#define _ << ", " << 
#define mp make_pair
#define cl(x) memset(x,0,sizeof(x))
#define EPS 1e-9
// #define umap unordered_map

template <class _T> inline string tostr(const _T& a){ ostringstream os(""); os<<a;return os.str();}

bool pal[1010];
bool palsqrt[1010];

int main(){

	int t; int caso =1;
	scanf("%d\n", &t);
	fr(i,0,1001) pal[i] = true;
	fr(i,1,1001){
		string temp = tostr ( i ) ;		 
		for (int j =0; j * 2 < temp.size(); j++){
			if( (j != temp.size() -1 -j) && temp[j] != temp[temp.size() - 1 -j]) 
				pal[i] = false;
		}
	}	
	cl(palsqrt);
	for(int i =1; i * i <= 1000; i++){
		if( pal[i] && pal[ i * i]){
			palsqrt[i*i] = true;
		}
	}
	//fr(i,0,1000) if( pal[i]) cout << i << endl;
	while(t--){
		int a, b, resp =0;
		cin >> a >> b;
		for(int i = a; i<= b; i++){
			if( palsqrt[i]) resp++;
		}
		printf("Case #%d: %d\n", caso++ , resp);
	}

	return 0;
}

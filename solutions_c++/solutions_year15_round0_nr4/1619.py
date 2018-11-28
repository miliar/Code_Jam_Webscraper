#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include<unordered_map>
#include<unordered_set>
using namespace std;

#define mp(a,b) make_pair((a),(b))
#define MS( a ) memset( a,0,sizeof(a))
#define MSV( a,v ) memset( a,v,sizeof(a))
typedef long long ll;
typedef pair<int,int> pii;
#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<pii> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned u32;

bool check(int X, int R, int C){
	if(X==1){
		return true;
	}
	if(X==2){
		if(R*C%2==0){
			return true;
		}
	}
	if(X==3){
		if(R==2&&C==3||R==3&&C==2||R==3&&C==3||R==3&&C==4||R==4&&C==3){
			return true;
		}
	}
	if(X==4){
		if(R==4&&C==3||R==3&&C==4||R==4&&C==4){
			return true;
		}
	}
	return false;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC, T;
	cin>>TC;
	for (T = 1; T <= TC; T++){
		int X,R,C;
		cin>>X>>R>>C;

		printf("Case #%d: ", T);
		if(check(X,R,C)){
			cout<<"GABRIEL"<<endl;
		}else{
			cout<<"RICHARD"<<endl;
		}
	}
}
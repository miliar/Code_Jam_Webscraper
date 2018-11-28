#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define fr(i,a,b) for(auto i=a;i<=b;i++)
#define rfr(i,a,b) for(auto i=b;i>=a;i--)
#define mp make_pair
#define ff first
#define ss second

typedef long long ll;

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	int T,X,R,C;
	cin>>T;

	string a[5][5][5];

	fr(i,1,4){
		fr(j,1,4){
			a[1][i][j]="GABRIEL";
		}
	}
	a[2][1][1]="RICHARD";a[2][1][2]="GABRIEL";a[2][1][3]="RICHARD";a[2][1][4]="GABRIEL";a[2][2][1]="GABRIEL";a[2][2][2]="GABRIEL";a[2][2][3]="GABRIEL";a[2][2][4]="GABRIEL";
	a[2][3][1]="RICHARD";a[2][3][2]="GABRIEL";a[2][3][3]="RICHARD";a[2][3][4]="GABRIEL";a[2][4][1]="GABRIEL";a[2][4][2]="GABRIEL";a[2][4][3]="GABRIEL";a[2][4][4]="GABRIEL";
	a[3][1][1]="RICHARD";a[3][1][2]="RICHARD";a[3][1][3]="RICHARD";a[3][1][4]="RICHARD";a[3][2][1]="RICHARD";a[3][2][2]="RICHARD";a[3][2][3]="GABRIEL";a[3][2][4]="RICHARD";
	a[3][3][1]="RICHARD";a[3][3][2]="GABRIEL";a[3][3][3]="GABRIEL";a[3][3][4]="GABRIEL";a[3][4][1]="RICHARD";a[3][4][2]="RICHARD";a[3][4][3]="GABRIEL";a[3][4][4]="RICHARD";
	a[4][1][1]="RICHARD";a[4][1][2]="RICHARD";a[4][1][3]="RICHARD";a[4][1][4]="RICHARD";a[4][2][1]="RICHARD";a[4][2][2]="RICHARD";a[4][2][3]="RICHARD";a[4][2][4]="RICHARD";
	a[4][3][1]="RICHARD";a[4][3][2]="RICHARD";a[4][3][3]="RICHARD";a[4][3][4]="GABRIEL";a[4][4][1]="RICHARD";a[4][4][2]="RICHARD";a[4][4][3]="GABRIEL";a[4][4][4]="GABRIEL";

	fr(xx,1,T){
		cin>>X>>R>>C;
		cout<<"Case #"<<xx<<": "<<a[X][R][C]<<"\n";
	}
	return 0;
}
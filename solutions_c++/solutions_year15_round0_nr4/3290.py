#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef long long ll;
int x[5][5][5];
void fk(int a,int b,int c) {
	x[a][b][c] =1;
	x[a][c][b] =1;
}
int main() {
	freopen( "in.txt", "r" , stdin);
	freopen( "out.txt", "w" , stdout);

	fk(3,2,3);
	fk(3,4,3);
	fk(3,3,3);
	fk(4,4,3);
	fk(4,4,4);
//	fk(2,2,2);
//	fk(2,1,2);
//	fk(1,1,1);

	int t,n,i,j,cas = 1;
	cin>>t;
	while(t--) {
		int a,b,c;
		cin>>a>>b>>c;
		string s;
		if(a==1||a==2) {
			if(b*c%a==0)s = "GABRIEL";
			else s = "RICHARD";

		}
		else {
			if(x[a][b][c]) s = "GABRIEL";
			else  s = "RICHARD";
		}




		printf("Case #%d: ",cas++);
		cout<<s<<endl;
	}


}


#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

#define		P		0
#define		R		1
#define		S		2
#define		next(i)	((((i)+1)%3))

string pt[3] = {"P","R","S"};


int res[3][13][3];
string rp[3][13];

int solve(int i,int j,int k){
	int &r = res[i][j][k];
	if (r!=-1) return r;
	int ni = next(i);
	r = solve(i,j-1,k)+solve(ni,j-1,k);
	return r;
}

string find(int i,int n){
	string &p = rp[i][n];
	if (p!="") return p;
	if (n==0){ 
		p = pt[i];
		return p;
	}
	string s1 = find(i,n-1);
	int ni = next(i);
	string s2 = find(ni,n-1);
	if (s1<s2) p = s1+s2;
	else p = s2+s1;
	return p;
}

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	for (int i=0;i<3;i++)
		for (int j=0;j<13;j++)
			for (int k=0;k<3;k++)
				res[i][j][k] = -1;
	
	int k,n,p,s,r;

	for (int i=0;i<3;i++){
		int k = i;
		res[i][0][k] = 1;
		k = next(k);
		res[i][0][k] = 0;
		k = next(k);
		res[i][0][k] = 0;		
	}
	
	for (int i=0;i<3;i++)
		for (int j=0;j<3;j++)
			solve(i,12,j);

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){

		cin >> n >> r >> p >> s;
		string rs = "Z";
		for (int i=0;i<3;i++){
			if (res[i][n][P]==p && res[i][n][R]==r && res[i][n][S]==s)
				rs = min(rs,find(i,n));
		}
		if (rs == "Z")
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << tc << ": " << rs << endl;
	}

	return 0;
}
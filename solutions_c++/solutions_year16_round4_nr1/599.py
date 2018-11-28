#include <bits/stdc++.h>
using namespace std;

int P, R, S;

string results;
string arrs1[3];
void don(int n,int papers,int rocks,int scis);

void funcss(int testCase){
	cout<<"Case #"<<testCase<<": ";
	int n, rocks, papers, scis;
	cin>>n>>rocks>>papers>>scis;
	P = papers; R = rocks; S = scis;
	for(int i=1;i<=n;i++){
		int p_Des = (rocks+papers-scis)/2;
		int s_Des = (scis+papers-rocks)/2;
		int r_Des = (rocks+scis-papers)/2;
		if(p_Des < 0 || s_Des < 0 || r_Des < 0){
			cout<<"IMPOSSIBLE\n";
			return;
		}
		papers = p_Des, rocks = r_Des, scis = s_Des;
	}
	arrs1[0] = "P";
	arrs1[1] = "R";
	arrs1[2] = "S";
	don(n, P, R, S);
}

void don(int n,int papers,int rocks,int scis){
	if(n == 0){
		if(papers)cout<<arrs1[0].c_str()<<endl;
		if(rocks)cout<<arrs1[1].c_str()<<endl;
		if(scis)cout<<arrs1[2].c_str()<<endl;
		return;
	}

	string strsss[3];
	if(arrs1[0] > arrs1[1])strsss[0] = arrs1[1] + arrs1[0];
	else strsss[0] = arrs1[0] + arrs1[1];
	if(arrs1[1] > arrs1[2])strsss[1] = arrs1[2] + arrs1[1];
	else strsss[1] = arrs1[1] + arrs1[2];
	if(arrs1[2] > arrs1[0])strsss[2] = arrs1[0] + arrs1[2];
	else strsss[2] = arrs1[2] + arrs1[0];
	for(int i=0;i<3;i++)arrs1[i] = strsss[i];
	int p_Des = (rocks+papers-scis)/2;
	int s_Des = (scis+papers-rocks)/2;
	int r_Des = (rocks+scis-papers)/2;
	don(n-1, p_Des, r_Des, s_Des);
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int testCases;
	cin>>testCases;
	for(int testCase=1;testCase<=testCases;testCase++){
		funcss(testCase);
	}
	return 0;
}

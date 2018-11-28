#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
#include <deque>
#include <set>
#include <unordered_map>

using namespace std;

string convertChar(char c){
	if(c=='P') return "PR";
	if(c=='R') return "RS";
	if(c=='S') return "SP";
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++)
	{		
		int N,P,R,S;
		scanf("%d %d %d %d\n",&N,&R,&P,&S);
		if(abs(R-P)>1 || abs(P-S)>1 || abs(S-R)>1){
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}
		int p=1;
		int r=0;
		int s=0;
		for(int i=0;i<N;i++){
			int tempP=p+s;
			int tempR=p+r;
			int tempS=r+s;
			p=tempP;
			r=tempR;
			s=tempS;
		}
		char winner;
		if(P==p && S==s && R==r) winner='P';
		else if(R==p && P==s && S==r) winner='R';
		else if(S==p && R==s && P==r) winner='S';
		else winner='E';
		vector < vector <char> > level(N+1);
		level[0]={winner};
		for(int i=0;i<N;i++){
			level[i+1]=vector <char>(level[i].size()*2);
			for(int j=0;j<level[i].size();j++){
				string temp=convertChar(level[i][j]);
				level[i+1][2*j]=temp[0];
				level[i+1][2*j+1]=temp[1];
			}
		}
		string ans="";
		for(int i=0;i<level[N].size();i++) ans+=level[N][i];
		for(int i=0;i<N;i++){
			//cout << ans << endl;
			for(int j=0;j<(1<<(N-i-1));j++){
				//cout << (1<<i)*j << " " << (1<<i) << "," << (1<<i)*(j+1) << " " << (1<<i) << endl;
				string left=ans.substr((1<<(i+1))*j,1<<i);
				string right=ans.substr((1<<(i+1))*j+(1<<i),1<<i);
				//cout << left << " " << right << endl;
				if(left>right){
					ans.replace((1<<(i+1))*j,1<<i,right);
					ans.replace((1<<(i+1))*j+(1<<i),1<<i,left);
				}
			}
		}
		
		
		cout << "Case #" << t << ": " << ans << endl;
	}
  return 0;
}

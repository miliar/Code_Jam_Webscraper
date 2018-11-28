#include<bits/stdc++.h>
using namespace std;
string line;
int main ()
{
	freopen("A-large.in","r",stdin);
	freopen("standing.out","w",stdout);
	int t;
	cin>>t;
	for (int i=1;i<=t;i++){
		int s=0;
		int res=0;
		int maxs;
		cin >>maxs>>line;
		for (int j=0;j<line.size();j++){
			if (s<j&& line[j]!='0'){
				res+= j-s;
				s=j;
			}
			s+= line[j]-'0';
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	
}

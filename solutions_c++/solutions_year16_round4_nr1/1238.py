/**/
#include<bits/stdc++.h>
using namespace std;
/***********************************************/
/*      ____________
 *     /            \
 *    /  /\      /\  \
 *   /  /  \    /  \  \
 *   \                /
 *    \     \___/    /
 *     \____________/
 */
const long long mod = 1000000007;
struct Ro{
	int R,P,S;
	string line;
};
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,C = 1;
	cin>>T;
	while(T--){
		cout<<"Case #"<<C++<<": ";
		int N,R,S,P;
		cin>>N>>R>>P>>S;
		long long to = 1ll<<N;
		queue<Ro> rs;
		rs.push({0,0,1,"S"});
		rs.push({0,1,0,"P"});
		rs.push({1,0,0,"R"});
		bool can = false;
		string out = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz";
		while(!rs.empty()){
			Ro u = rs.front();
			rs.pop();
			if(u.line.size() == to){
				if(u.R == R && u.P == P && u.S == S){
					can = true;
					for(int j = 1;j <= N;j++){
						string to;
						for(int k = 0;k < u.line.size();k+=(1<<j)){
							to += min(u.line.substr(k,(1<<(j-1))),u.line.substr(k+(1<<(j-1)),(1<<(j-1))));
							to += max(u.line.substr(k,(1<<(j-1))),u.line.substr(k+(1<<(j-1)),(1<<(j-1))));
						}
						u.line = to;
					}
					out = min(out,u.line);
				}
				continue;
			}
			Ro v = Ro();
			for(int i = 0;i < u.line.size();i++){
				if(u.line[i] == 'R')
					v.line += 'R',v.line += 'S',v.R++,v.S++;
				if(u.line[i] == 'S')
					v.line += 'P',v.line += 'S',v.P++,v.S++;
				if(u.line[i] == 'P')
					v.line += 'P',v.line += 'R',v.R++,v.P++;
			}
			rs.push(v);
		}
		if(!can)
			cout<<"IMPOSSIBLE";
		else
			cout<<out;
		cout<<endl;
	}
	return 0;
}
/**/

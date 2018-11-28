#include <bits/stdc++.h>
using namespace std;
#define all(c) c.begin(), c.end()
#define tr(container, it) for(auto it = container.begin(); it != container.end(); it++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define rof(i,a,b) for(int (i)=(a);(i) > (b); --(i))
#define rep(i, c) for(auto &(i) : (c))
#define x first
#define y second
#define pb push_back
#define PB pop_back()
#define fastscan ios_base::sync_with_stdio(0);cin.tie(NULL);
int sides[100];
int lim = 0;
int done(){
	int ret=1;
	for(int x=0;x<lim;x++){
		if(sides[x]==0){
			ret=0;
			break;
		}
	}
	return ret;
}
int minMoves(int i, int side) {
	if(i==lim-1&&side==1){
		return 0;
	}
	int j=i+1;
	while(j<lim&sides[j]==side){
		j++;
	}
	if(j==lim&&side==0){
		return 1;
	}else if(j==lim&&side==1){
		return 0;
	}
	else{
		return 1 + minMoves(j, sides[j]);
	}
}
int main() {
	int l;
	cin>>l;
	int i = 1;
	while(l--) {
		string t;
		cin>>t;
		for(int x=0;x<lim;x++){
			sides[x]=0;
		}
		lim=0;
		for(int x=0;x<t.size();x++){
			char c = t.at(x);
			if(c=='-'){
				sides[x]=0;
			}else{
				sides[x]=1;
			}
			lim++;
		}
		int n=minMoves(0,sides[0]);
		cout<<"Case #"<<i<<": "<<n<<"\n";
		i++;
	}
}

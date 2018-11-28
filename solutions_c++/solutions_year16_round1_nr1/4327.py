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
int main() {
	int t, i=1;
	cin>>t;
	while(t--){
		string s, res;
		cin>>s;
		char head = s.at(0);
		res = res+head;
		for(int x=1;x<s.size();x++){
			char c = s.at(x);
			if(c<head){
				res = res+c;
			}else{
				res = c + res;
				head = c;
			}
		}
		cout<<"Case #"<<i<<": "<<res<<"\n";
		i++;
	}
}

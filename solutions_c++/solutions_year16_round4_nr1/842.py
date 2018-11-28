#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef pair<int,ii> iii;

int n,p,r,s;
int c[3];
char l[3] = {'P','R','S'};

int main(){
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> n >> r >> p >> s;
    queue<int> q1,q2;
    string ss[3] = {"","",""};
    for(int x = 0; x < 3; ++x){
      q1.push(x);
      for(int i = 0; i < n; ++i){
	while(!q1.empty()){
	  int y = q1.front(); q1.pop();
	  if(y == 0){ q2.push(0); q2.push(1); }
	  if(y == 1){ q2.push(1); q2.push(2); }
	  if(y == 2){ q2.push(0); q2.push(2); }
	}
	while(!q2.empty()){
	  q1.push(q2.front());
	  q2.pop();
	}
      }
      for(int i = 0; i < 3; ++i) c[i] = 0;
      while(!q1.empty()){
	int y = q1.front(); q1.pop();
	ss[x] += l[y];
	++c[y];
      }
      if(c[0] == p and c[1] == r and c[2] == s){
	for(int i = 4; i <= ss[x].size(); i <<= 1){
	  for(int j = 0; j < ss[x].size(); j += i){
	    if(ss[x].substr(j+i/2,i/2) < ss[x].substr(j,i/2)){
	      for(int k = 0; k < i/2; ++k){
		char aux = ss[x][j+k];
		ss[x][j+k] = ss[x][j+k+i/2];
		ss[x][j+k+i/2] = aux;
	      }
	    }
	  }
	}
      }
      else ss[x] = "Z";
    }
    sort(ss,ss+3);
//     cout << ss[0] << ' ' << ss[1] << ' ' << ss[2] << endl;
    if(ss[0] == "Z") cout << "Case #" << cass << ": IMPOSSIBLE\n";
    else cout << "Case #" << cass << ": " << ss[0] << "\n";
  }
}
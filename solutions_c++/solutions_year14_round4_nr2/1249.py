#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<set>
#include<cassert>
using namespace std;

int T,N;
typedef pair<int,vector<int> >P;

void display(vector<int> vec){

    for(int i = 0 ; i < N ; i++){ //
      cout << vec[i] << ' ';
    }
    cout << endl;

}

void solve(){
  cin >> N;
  vector<int> vec = vector<int>(N,0);
  int maxi = 0;
  int maxi_id = 0;
  for(int i = 0 ; i < N ; i++){
    cin >> vec[i];
    maxi = max(maxi,vec[i]);
  }

  set<vector<int> >st;
  queue<P>que;
  que.push(P(0,vec));
  st.insert(vec);

  while(que.size()){

    P p = que.front(); que.pop();
    vec = p.second;

    bool f = true;
    int pre = -1;
    int pos = 0;

    //cout << "p.first = " << p.first << endl;
    //display(vec);

    for( ; pos < N ; pos++){
      if(vec[pos] == maxi)break;
      if(pre > vec[pos]){
	f = false;
	break;
      }
      pre = vec[pos];
    }

    pre = maxi;
    pos++;
    
    for( ; pos < N ; pos++){
      if(pre < vec[pos]){
	f = false;
	break;
      }
      pre = vec[pos];
    }

    if(f){
      cout << p.first << endl;
      return;
    }

    for(int i = 0 ; i < N ; i++){
      for(int j = -1 ; j < 2 ; j+=2){
	vector<int>nvec = vec;
	if(i+j < 0 || i+j >= N)continue;
	swap(nvec[i],nvec[i+j]);
	//cout << "i = " << i << " j = " << j << endl;
	//display(nvec);
	if(st.count(nvec))continue;
	st.insert(nvec);
	//cout << "??" << endl;
	que.push(P(p.first+1,nvec));
      }
    }
  }
  assert(false);
}

int main(){
  cin >> T;
  for(int i = 1 ; i <= T ; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}

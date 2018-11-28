#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>

using namespace std;

typedef long long in;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int test=0;test<t;test++){
    int n;
    cin >> n;
    vector<pair<int, char> > sen;
    char c='A';
    int q;
    int am=0;
    for(int i=0;i<n;i++){
      cin >> q;
      sen.push_back(make_pair(q,c));
      c++;
      am+=q;
    }
    cout << "Case #" << test+1 << ": ";
    int part=n;
    while(am!=0){
      sort(sen.begin(),sen.end(), greater<pair<int,char> >());
      for(int i=0;i<n;i++){
	if(sen[i].first>=2){
	  if(sen[i+1].first<=(am-2)/2){
	    sen[i].first-=2;
	    am-=2;
	    if(sen[i].first==0)
	      part--;
	    cout << sen[i].second << sen[i].second << " ";
	  }
	  else if(sen[i+1].first-1<=(am-2)/2){
	    sen[i].first--;
	    sen[i+1].first--;
	    if(sen[i].first==0)
	      part--;
	    if(sen[i+1].first==0)
	      part--;
	    cout << sen[i].second << sen[i+1].second << " ";
	    am-=2;
	  }
	  break;
	}
	else if(sen[i].first==1){
	  if(part==3){
	    cout << sen[i].second << " ";
	    part--;
	    sen[i].first--;
	    am--;
	  }
	  else{
	    cout << sen[i].second << sen[i+1].second << " ";
	    sen[i].first--;
	    sen[i+1].first--;
	    am-=2;
	    if(sen[i+1].first==0)
	      part--;
	    part--;
	  }
	  break;
	}
      }
    }
    cout << endl;
  }
  return 0;
}
  
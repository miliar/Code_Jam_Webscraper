#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <list>
#include <iomanip> 

using namespace std;

struct VoteP {
int yes;
int no;
double prob;
};

void subset(vector<double> v, int left, int index, vector<double> &l, vector<vector<double> > &subsets){
    if(left==0){
        subsets.push_back(l);
        return;
    }
    for(int i=index; i<v.size();i++){
        l.push_back(v[i]);
        subset(v,left-1,i+1,l, subsets);
        l.pop_back();
    }
}  


double calc_prob(const vector<double> &v) {
  vector<double> curr_probs;
  vector<double> vp(v.size()*2);
  vector<double> vp2(v.size()*2);
  for(int i = 0; i < vp.size(); i++) {
    vp[i] = 0.0;
  }
  vp[0] = (1-v[0]);
  vp[1] = v[0];
  for(int i = 1; i < v.size(); i++) {
    double p = v[i];
    for (int j = 0; j < vp.size(); j++) {
      if(j==0) {
        vp2[j] = vp[j]*(1.0-p);
      } else {
        vp2[j] = vp[j]*(1.0-p) + vp[j-1]*(p);
      }
    }
    vp = vp2;
  }
  return vp[v.size()/2];
}

vector<double> get_vp(const vector<double> &v) {
  vector<double> curr_probs;
  vector<double> vp(v.size()*2);
  vector<double> vp2(v.size()*2);
  for(int i = 0; i < vp.size(); i++) {
    vp[i] = 0.0;
  }
  vp[0] = (1-v[0]);
  vp[1] = v[0];
  for(int i = 1; i < v.size(); i++) {
    double p = v[i];
    for (int j = 0; j < vp.size(); j++) {
      if(j==0) {
        vp2[j] = vp[j]*(1.0-p);
      } else {
        vp2[j] = vp[j]*(1.0-p) + vp[j-1]*(p);
      }
    }
    vp = vp2;
  }
  return vp;
}

double highest_prob_check(long N, long K, vector<double> probs) {
  vector<vector<double> > subsets;
  vector<double> tmp;
  subset(probs, K, 0, tmp, subsets);
  
  double max_prob=0.0;
  
  for (int i = 0; i < subsets.size(); i++) {
    double curr = calc_prob(subsets[i]);
    if (curr > max_prob) {
       max_prob = curr;
    }
  }
  
  return max_prob;
}

double test2(vector<double> v, vector<double> probs, long K, vector<double> &outv) {
  double m = 0.0;
  vector<double> usable_probs = probs;
  for (int i = 0; i < v.size(); i++) {
    vector<double>::iterator pos = find(usable_probs.begin(), usable_probs.end(), v[i]);
    if (pos == usable_probs.end()) {
      cout << "WTF" << endl;
      return 0.0;
    }
    usable_probs.erase(pos);
  }
  
  for (int i =0; i < v.size(); i++) {
    vector<double> vv = v;
    usable_probs.push_back(vv[i]);
    vv.erase(vv.begin()+i);
    vector<double> vp = get_vp(vv);
    for (int j= 0; j < usable_probs.size(); j++) {
      double p = usable_probs[j];
      double mm = vp[K/2-1]*p + vp[K/2]*(1.0-p);
      if (mm > m) {
        outv = vv;
        outv.push_back(p);
      }
      m = max(m,mm);
    }
    usable_probs.pop_back();
  }
  return m;
}

double test(long N, long K, vector<double> probs) {
  sort(probs.begin(), probs.end());
  vector<double> v;
  for(int i = 0; i < K/2; i++) {
    v.push_back(probs[i]);
    v.push_back(probs[N-1-i]);
  }
  double m = calc_prob(v);
  vector<double> curr = v;
  for(int i=0; i < 200; i++) {
    test2(v, probs, K, curr);
    v = curr;
  }
  return max(m, test2(v, probs, K, curr));
}

int main() {
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    long N, K;
    cin >> N >> K;
    vector<double> probs;
    for(int i = 0; i < N; i++) {
      double foo;
      cin >> foo;
      probs.push_back(foo);    
    }
    //double ans = highest_prob_check(N, K, probs);
    double ans2 = test(N,K,probs);
    
    cout << fixed;
    cout << setprecision(9);
    cout << "Case #" << tt << ": " << ans2 << endl;
  }

  return 0;
}



#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

int main() {
  int T;
  cin>>T;
  for (int t=1;t<=T;t++) {
    int N;
    double V,X;
    cin>>N>>V>>X;
    vector<pair<double,double> > rates(N);
    for (int n=0;n<N;n++) {
      double ri,ci;
      cin>>ri>>ci;
      ci-=X;
      rates[n]=make_pair(ci,ri);
    }
    sort(rates.begin(), rates.end());
    double best = -1;
    double rate=0, temp=0;
    for (int i=0;i<N;i++) {
      if (rates[i].first<=0) {
	double nrate=rate+rates[i].second;
	double ntemp=(rate*temp+rates[i].first*rates[i].second)/nrate;
	rate=nrate;
	temp=ntemp;
      } else {
	double nrate=rate+rates[i].second;
	double ntemp=(rate*temp+rates[i].first*rates[i].second)/nrate;
	if (ntemp>=0) {
	  rate=rate-(rate*temp)/rates[i].first;
	  best=rate;
	  break;
	}
      }
    }
    if (best == -1) {
    rate=0, temp=0;
    for (int i=N-1;i>=0;i--) {
      if (rates[i].first>=0) {
	double nrate=rate+rates[i].second;
	double ntemp=(rate*temp+rates[i].first*rates[i].second)/nrate;
	rate=nrate;
	temp=ntemp;
      } else {
	double nrate=rate+rates[i].second;
	double ntemp=(rate*temp+rates[i].first*rates[i].second)/nrate;
	if (ntemp<=0) {
	  rate=rate-(rate*temp)/rates[i].first;
	  best=rate;
	  break;
	}
      }
    }
    }
    if (best == -1 && temp==0 && rate !=0) {
      best=rate;
    }
    if (best == -1 || best == 0) {
      cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
    } else {
      cout.precision(15);
      cout<<"Case #"<<t<<": "<<V/best<<endl;
    }
  }
}

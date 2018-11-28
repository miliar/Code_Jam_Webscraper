#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

const double EPS=1e-12;

int main(void) {
  cout << fixed << setprecision(9);
  int64_t T;
  cin >> T;

  for(int64_t t=1;t<=T;t++) {
    int64_t N;
    cin >> N;
    double V, X;
    cin >> V >> X;
    vector<pair<double,double>> RC(N);
    for(int64_t i=0;i<N;i++) {
      cin >> RC[i].second >> RC[i].first;
    }
    sort(RC.begin(), RC.end()); //Sort by temp
    if(RC[0].first > X + EPS || RC[N-1].first < X - EPS) { //Too cold or warm
      cout << "Case #" << t << ": IMPOSSIBLE\n";
      continue;
    }
    //Should be possible now
    
    double Rlow=0,Rhigh=0,Tlow=0,Thigh=0,Requal=0,Tequal=0;
    for(int64_t i=0;i<N;i++) {
      if(RC[i].first < X - EPS) {
        Rlow+=RC[i].second;
        Tlow+=RC[i].second*RC[i].first;
      } else if(RC[i].first < X + EPS && RC[i].first > X - EPS) {
        Requal+=RC[i].second;
        Tequal+=RC[i].second*RC[i].first;
      }
        else {
        Rhigh+=RC[i].second;
        Thigh+=RC[i].second*RC[i].first;
      }
    }

    if(Thigh < EPS) {
      Rhigh+=Requal;
      Thigh+=Tequal;
    } else {
      Rlow+=Requal;
      Tlow+=Tequal;
    }

    if(Tlow < EPS) {
      cout << "Case #" << t << ": " << V/Rhigh << "\n";
      continue;
    }

    /*if(Thigh < EPS) {
      cout << "Case #" << t << ": " << V/Rlow << "\n";
      continue;
    }*/
    Tlow/=Rlow;
    Thigh/=Rhigh;
    double T1=V/Rlow * (Thigh - X)/(Thigh - Tlow);
    double T2=V/Rhigh * (X - Tlow)/(Thigh - Tlow);
    cout << "Case #" << t << ": " << max(T1,T2) << "\n";
  }
  return 0;
}


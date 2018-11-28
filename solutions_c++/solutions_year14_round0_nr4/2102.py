#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<algorithm>

using namespace std;

#define FOR1(i, n) for (int i=1; i<=n; ++i)
#define FOR0(i, n) for (int i=0; i<n; ++i)

typedef vector<double>::iterator VDI;

class Ken : public set<double> {
 public:
  // Ken(Ken& k) : set(static_cast<set>(k)) {}
  Ken(VDI b, VDI e) : set(b,e) {}
  // respond to noemie, return if wins
  bool operator()(const double naomi){
    set<double>::iterator b2w = end(); // better to worse
    b2w--;
    if (naomi < *b2w){
      // win, give weakest better
      for (b2w--; *b2w > naomi && b2w != begin(); b2w--);
      if (*b2w < naomi)
        b2w++;
      //cerr << "Ken wins with " << *b2w << " against " << naomi << endl;
      erase(b2w);
      return true;
    }
    {
      // lose, give wekeast
      //cerr << "Ken loses with " << *begin() << " against " << naomi << endl;
      erase(begin());
      return false;
    }
  }
};

class Dnaomi : public set<double> {
  Ken& ken;
 public:
  Dnaomi(VDI b, VDI e, Ken& k) : set(b,e), ken(k) {}
  // init force: Smallest: Lose against biggest or win against smallest
  bool operator()(){
    double n = *begin();
    erase(begin());
    if (n < *ken.begin()){
      // lose against biggest
      ken(*ken.rbegin()-0.000001);
      return false;
    }
    // win against smallest
    ken((1+*ken.rbegin())/2);
    return true;
  }
};

void testcase(int tc){
  int n;
  cin >> n;
  vector<double> naomi(n);
  FOR0(i,n)
    cin >> naomi[i];
  vector<double> ken(n);
  FOR0(i,n)
    cin >> ken[i];

  sort(naomi.begin(), naomi.end());
  sort(ken.begin(), ken.end());

  int w = n; // honest war
  {
    Ken keno(ken.begin(),ken.end());
    // bottom to top, once Ken starts losing he'll always lose
    FOR0(i,n){
      if (keno(naomi[i])){
        w--;
      }
    }
  }
  
  //cerr << endl;
  
  int dw = 0;
  {
    Ken keno(ken.begin(),ken.end());
    Dnaomi naomio(naomi.begin(),naomi.end(),keno);
    FOR0(i,n){
      if (naomio())
        dw++;
    }
  }
  printf("Case #%d: %d %d\n", tc, dw, w);
}

int main(){
  int ntc;
  cin >> ntc;
  FOR1(tc, ntc){
    testcase(tc);
  }
}

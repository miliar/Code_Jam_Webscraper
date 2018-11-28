#include <bits/stdc++.h>
#include <string>
#include <fstream>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
// #define fr(i, counter, inc) for(int j = i; j<counter; j += inc)

int main(){
  ios_base::sync_with_stdio(0);
  int t, val, c, temp;
  string s;
  set<int> myset;
  set<int>::iterator it;
  cin >> t;
  ofstream myfile;
  myfile.open ("example.txt");
  for(int i = 0; i < t; i++){
    myset.clear();
    cin >> temp;
    if(temp == 0){myfile<< "Case #"<<i+1<<": "<<"INSOMNIA\n";continue;}
    val = temp;
    c = 0;
    while(myset.size() != 10){
      val = temp * ++c;
      s = to_string(val);
      // cout << s << "\n";
      for(int j = 0; j<s.size(); j++){
        myset.insert(s[j]);
      }
    }
    // printf("%d", val);
    myfile << "Case #"<<i+1<<": "<<val <<"\n";
  }
}

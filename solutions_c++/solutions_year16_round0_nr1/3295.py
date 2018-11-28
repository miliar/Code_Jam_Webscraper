#include "sheep.h++"

typedef long long int lli;


class Problem {
public:

  Problem(istream & cin, int icase){
    cin >> N;
    lcnv( N );
    lli i = 1;
    set<char> A;
    shared_ptr<string> result;
    int ndim = A.size();
    int lasted = 0;
    while ( 1 ){
      const lli c = N*i;
      stringstream ss;
      ss << c;
      const string s = ss.str();
      for(auto c : s){
        A.insert(c);
      }
      const int n = A.size();
      if( n > ndim ){
        ndim = n;
        lasted = 0;
      } else {
        lasted++;
      }
      lcnv( ndim );
      if( ndim == 10 ){
        result = shared_ptr<string>(new string(s));
        break;
      }
      i++;
      if ( lasted == 100 ) break;
    }
    solution = result.get() ? *result : "INSOMNIA";
  }
  std::string solve() {
    return solution;
  }


  lli N; // Chests to open
  string solution;
};



int main(){
  try {
    istringstream iss = op::getline(cin);
    int T;
    iss >> T;
    lcnv(T);
    lcnh();
    for(int icase = 1; icase <= T; icase++){
      Problem p(cin,icase);
      //const auto ans = "skipping";
      const auto ans = p.solve();
      cout << "Case #" << icase << ": " << ans << endl;
    }

    return 0;
  } catch ( const exception & e ){
    cerr << e.what() << endl;
    return 1;
  }
}

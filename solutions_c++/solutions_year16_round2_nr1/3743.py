#include "digits.h++"

vector<string> words = {"ZERO", "ONE", "TWO", "THREE", 
                        "FOUR", "FIVE", "SIX", "SEVEN", 
                        "EIGHT", "NINE"};

string F(char bottom, map<char,int> phstat){

  bool empty = true;
  for(auto c : phstat){
    if( c.second ){
      empty = false;
      break;
    }
  }
  if( empty ) return "";


  // Possible continuations
  vector<char> ics;
  {
    for(char ic = bottom; ic <= '9'; ic++){
      const string word = words[ic-'0'];
      bool test = true;
      {
        for( auto c : word){
          if( phstat[c] == 0 ){
            test = false;
            break;
          }
        }
      }
      if( test ){
        ics.push_back(ic);
      }
    }
  }

  for(auto ic : ics){
    const string word = words[ic-'0'];

    map<char,int> phs = phstat;
    for( auto c : word ) phs[c]--;
    try {
      lcnv( ic );
      return ic+F(ic,phs);
    }
    catch ( int ){
      continue;
    }
  }

  throw 1;
};





class Problem {
public:

  Problem(istream & cin, int icase){
    istringstream iss = op::getline(cin);

    // Number of keys to start with; number of chests.
    iss >> phn;
    lcnv(phn);
  }
  std::string solve() {

    map<char,set<int> > charindex;
    {
      int i = 0;
      for(auto w : words){
        //lcnv(w);
        for(auto c : w){
          //cout << i << ", " << c << endl;
          charindex[c].insert(i);
        }
        i++;
      }
    }


    string prefix;
    map<char,int> phstat;
    {
      for(auto c : phn){
        phstat[c]++;
      }
    }

    try {
      return F('0',phstat);
    }
    catch ( int ){
      return "TBD";
    }
  }

  string phn;


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

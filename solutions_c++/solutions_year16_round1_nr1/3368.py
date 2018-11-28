#include <fstream>
#include <sstream>
#include <set>

using namespace std;

int main(int argc, char* argv[]){
	ifstream in(argv[1]);
	ofstream out("frakt.out");
  int T;
  string S;
  in >> T;
  for(int C=1; C<=T; C++){
    in >> S;
    string final = "";
    string ch;
    char f = S[0];
    for(int i=0; i<S.length(); i++){
      stringstream ss;
      ss << S[i];
      ss >> ch;
      if(S[i]>=f){
        final = ch + final;
        f = S[i];
      } else{
        final = final + ch;
      }
    }
    out << "Case #" << C << ": " << final << endl;
  }
}

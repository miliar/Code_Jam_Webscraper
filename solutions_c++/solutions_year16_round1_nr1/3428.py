# include <iostream>
# include <cmath>
# include <vector>
# include <string>
# include <algorithm>
# include <ostream>
# include <fstream>
# include <queue>
# include <stack>

using namespace std;

typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pair<int, int> > vp;
typedef vector<vd> vvd;


# define REP(i,a,b) for(int i = a; i < b; i++)
# define REVREP(i,a,b) for(int i = a; i >= b; i--)
# define newl cout << endl
# define debl(a) cout << a << " "
# define debl2(a,b) cout << a << " " << b << " "
# define debnl(a) cout << a << endl
# define debnl2(a,b) cout << a << " " << b << endl
# define minv(a) *min_element(a.begin(), a.end())
# define maxv(a) *max_element(a.begin(), a.end())
# define minvind(a) min_element(a.begin(), a.end())
# define maxvind(a) max_element(a.begin(), a.end())

//string CaseName = "A-prac";
//string CaseName = "A-small-attempt1";
string CaseName = "A-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;

void Solve(void) {
  
  return;
}

string word;

int main() {

	int NCases; 
	
	In.open(CaseName+".in");
	
	// Reads Number of cases //
  In >> NCases;
  
  Out.open(CaseName+".out");
  
	
	int i,j;

  REP(i,1,NCases+1) {
  
    In >> word;
    
    int maxind = -1;
    int max = 'A';
    
    for (int i = 0; i < word.size(); i++) {
      if (word[i] > max) {
        max = word[i];
        maxind = i;
      }
    }
    
    string ret;
    
    ret = word[0];
    
    int curmax = word[0];
    
    REP(i,1,word.size()) {
      
    /*  if ((i < maxind) || (word[i] == max)) {
        
        if (ret[ret.size()-1] > word[i]) {
          ret = ret + word[i];
        } else {
          ret = word[i] + ret;
        }        
        
      } else {
        ret += word[i];
      }
    */
      
      if (word[i] >= curmax) {
        curmax = word[i];
        
        ret = word[i] + ret;
      } else {
      
        ret = ret + word[i];
      } 
    
    
    }
    
    
    
    
    
		Out << "Case #" << i << ": ";
		cout << "Case #" << i << ": ";		
    Out << ret << endl;
    cout << ret << endl;
    
    Solve();
		
	}
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <cmath>
#include <limits>
#include <vector>
#include <sstream>
using namespace std;

#define print(x) cout << #x " = " << x << endl;

int numberOfCases(ifstream &infile);
int readCaseFromStream(ifstream &infile, int m, int n, int ** a);
int readCaseSizeFromStream(ifstream &infile, int &m, int &n);

int main ( int argc, char* argv[] ) {
  if ( argc < 2 ) { 
    cerr << "Usage: main <file.in>" << endl;  
    return EXIT_FAILURE; 
  }
  ifstream infile; infile.open(argv[1]);  
  int numCases = numberOfCases(infile);

  int m = 0, n = 0;
  
  for ( int k = 0; k < numCases; ++k ) {
    if ( readCaseSizeFromStream(infile, m, n) ) {
      int **lawn;
      lawn = new int *[m];
      for ( int i = 0; i < m; ++i ) {
	lawn[i] = new int[n];
      }
      readCaseFromStream(infile, m, n, lawn);                   
      cout << "Case #" << k+1 << ": ";

      vector<int> v_m_max(m,0), v_m_min(m,101), v_n_max(n,0), v_n_min(n,101);

      bool possible = true;

      for ( int i = 0; i < m; ++i ) {
	for ( int j = 0; j < n; ++j ) {
	  v_m_max[i] = max(v_m_max[i], lawn[i][j]);
	  v_m_min[i] = min(v_m_min[i], lawn[i][j]);
	  v_n_max[j] = max(v_n_max[j], lawn[i][j]);
	  v_n_min[j] = min(v_n_min[j], lawn[i][j]);
	}	
      }  

      for ( int i = 0; i < m; ++i ) {
	for (int j = 0; j < n; ++j ) {
	  if ( (v_m_max[i] > lawn[i][j]) && (v_n_max[j] > lawn[i][j]) ) {
	    possible = false; break;
	  }
	}
      }

      if ( possible ) { cout << "YES"; } 
      else { cout << "NO"; } 

      cout << endl;   

      for ( int i = 0; i < m; ++i ) {
	delete [] lawn[i];       
      }
      delete [] lawn;
    }
  }
  infile.close();
  return 0;
}

int readCaseFromStream(ifstream &infile, int m, int n, int ** a) {
  if ( infile ) {
    for ( int i = 0; i < m; ++i ) {
      string s, token;
      getline(infile, s);
      istringstream ss(s);
      int j = 0;
      while ( getline (ss, token, ' ') ) {
	a[i][j] = atoi(token.c_str());
	++j;
      }
    }
    return 1;
  }     
  return 0;
}

int readCaseSizeFromStream(ifstream &infile, int &m, int &n) {
  if ( infile ) {
    string s;
    if ( getline(infile, s) ) {
      unsigned pos = s.find(" ");
      m = atoi(s.substr(0,pos).c_str());
      n = atoi(s.substr(pos).c_str());
      return 1;
    }
    return 0;
  }
  return 0;
}

int numberOfCases(ifstream &infile) {
  if ( infile ) {
    string s;
    if ( getline(infile, s) ) {
      return atoi(s.c_str());
    } 
    return 0;  
  } 
  return 0;
}

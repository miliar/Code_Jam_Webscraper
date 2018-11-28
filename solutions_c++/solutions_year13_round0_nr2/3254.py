#include <vector>
#include <iostream>
using namespace std;

class lawn {
    vector < vector <int> > sim;

  int rowok(int i, int j, int h, vector < vector <int> > spec) {
    int n, m;
    n = spec.size();
    m = spec[0].size();
    for (j = 0; j < m; j++) {
      if (spec[i][j] > h) {
	return 0;
      }
    }
    return 1;
  }

  int colok(int i, int j, int h, vector < vector <int> > spec) {
    int n, m;
    n = spec.size();
    m = spec[0].size();
    for (i = 0; i < n; i++) {
      if (spec[i][j] > h) {
	return 0;
      }
    }
    return 1;
  }


  int rowseth(int i, int j, int h, vector < vector <int> > spec) {
    int n, m;
    n = spec.size();
    m = spec[0].size();
    for (j = 0; j < m; j++) {
      sim[i][j] = h;
    }
    return 1;
  }

  int colseth(int i, int j, int h, vector < vector <int> > spec) {
    int n, m;
    n = spec.size();
    m = spec[0].size();
    for (i = 0; i < n; i++) {
      sim[i][j] = h;
    }
    return 1;
  }


public:
  int isok(vector < vector <int> > spec) {
    int n, m, i, j, h;
    n = spec.size();
    m = spec[0].size();

    
    for (i = 0; i < n; i++) {
      vector <int> row;
      for (j = 0; j < m; j++) {
	row.push_back(100);
      }
      sim.push_back(row);
    }


    for (h = 100; h > 0; h--) {
      for (i = 0; i < n; i++) {
	for (j = 0; j < m; j++) {
	  if (sim[i][j] > h && sim[i][j] > spec[i][j]) {
	    if (rowok(i, j, h, spec)) {
	      rowseth(i, j, h, spec);
	    } else if (colok(i, j, h, spec)) {
	      colseth(i, j, h, spec);
	    } else {
	      return 0;
	    }
	  }
	}
      }
    }
      
    return 1;
  }

};

int main(void) {
  int T, t;

  cin >> T;

  for (t = 1; t <= T; t++) {
    int N, M;

    cin >> N;
    cin >> M;
    int i, j, res;
    vector < vector <int> > sp;
    for (i = 0; i < N; i++) {
      vector <int> v;
      int h;
      for (j = 0; j < M; j++) {
	cin >> h;
	v.push_back(h);
      }
      sp.push_back(v);
    }
    lawn L;

    res = L.isok(sp);
    cout << "Case #" << t << ": " << (res ? "YES" : "NO") << endl;
  }

}

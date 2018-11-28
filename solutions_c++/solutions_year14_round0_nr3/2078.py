#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

class Minfld
{
  int r,c,m,t;
  int* fld;
  int total_rev;

  int nbi[9] = {-1,-1,-1, 0,0,0, 1,1,1};
  int nbj[9] = {-1,0,1, -1,0,1, -1,0,1};

  stack<int> zer, rev;

  inline int nbr(int m, int n){ 
    int m_i = m / c;
    int m_j = m % c;
    
    int n_i = m_i + nbi[n];
    int n_j = m_j + nbj[n];
    
    return (n_i < 0 || n_j < 0 || n_i >= r || n_j >= c ) ? -1 : n_i * c + n_j;

  };

  inline void may_unrev(int cursq)
  {
    for(int i = 0; i < 9; i++){
      int curn = nbr(cursq, i);
      if (curn != -1)
        if (fld[curn] == 0)
          return;
    }

    if (fld[cursq] == 1)
      total_rev--;

    fld[cursq] = -1;
  }

  void zero_me(int cursq) {
    zer.push(cursq);
    if (fld[cursq] == -1) 
      total_rev++;
    fld[cursq] = 0;
    for(int i = 0; i < 9; i++)
      if (i != 4) {
        int curn = nbr(cursq,i);
        if (curn != -1)
          if (fld[curn] < 0)
          {
            fld[curn] = 1;
            total_rev++;
            //my_rev[cursq].add(curn);
          }
      }
  }

  void unzero_me(int cursq) {
    zer.pop();
    fld[cursq] = 1;
    for(int i = 0; i < 9; i++) {
      int curn = nbr(cursq,i);
      if (curn != -1)
        may_unrev(nbr(cursq,i));
    }
  }

  bool compute_possible_position(int curzer)
  {
    zero_me(curzer);
    //cout << curzer << endl;
    //print_position(-1);


    if (total_rev + m > t) {
      unzero_me(curzer);
      return false;
    }

    if (total_rev + m == t) return true;

    for(int i = 0; i < t; i++) {
      if (fld[i] == 1) {
        //int cursq = nbr(curzer,i);
        //if (/*(cursq != curzer) && */(fld[i] != 0))
          if (compute_possible_position(i) == true) 
            return true;
      }
    }

    unzero_me(curzer);
    return false;

  }

public:
  int compute_click_all()
  {
    for(int cursq = 0; cursq < t; cursq++) {
      fld[cursq] = 1;
      total_rev++;
      if (total_rev + m == t) return cursq;
      if (compute_possible_position(cursq)) return cursq;
      reset_fld();
    }
    
    return -1;
  }

  void print_position(int click)
  {
    int ci = click / c;
    int cj = click % c;
    
    for(int i = 0; i < r; i++) {
      for(int j = 0; j < c; j++) {
        char curs =  (fld[i*c+j] == -1) ? '*' : ((fld[i*c+j] == 0) ? '.':'.');
        if ((i == ci) && (j == cj))
          curs = 'c';
        cout << curs;
      }
      cout << endl;
    }

  }
  
  Minfld(int nr, int nc, int nm)
    :r(nr), c(nc), m(nm), total_rev(0)
  {
    t = r*c;
    
    fld = new int[t];
    reset_fld();
    //my_rev = new stack<int>[t];
    
  }

  inline void reset_fld() { memset(fld, -1, t*sizeof(int));};
    
};

int main()
{

  int T;
  cin >> T;

  for(int cc = 1; cc <= T; cc++)
    {
      int R,C,M;
      cin >> R >> C >> M;
      
      //cout << R << "," << M<< endl;
      Minfld mfld(R,C,M);

      int c = mfld.compute_click_all();
      cout << "Case #" << cc << ":" << endl;
      if (c >= 0)
        mfld.print_position(c);
      else
        cout << "Impossible" << endl;
    }
  
  return 0;
}

#include "senate.h++"


class Problem {
public:

  Problem(istream & cin, int icase ) : m_icase(icase) {
    // Input
    {
      istringstream iss;
      iss = op::getline(cin);
      iss >> N;
      iss = op::getline(cin);
      for( int i = 0; i < N; i++){
        int P;
        iss >> P;
        nsen += P;
        lcnv(P);
        nmem.push_back(P);
      }
    }
    lcnv(nsen);

    stringstream ss;

    while( nsen > 0 ){
      int nmaj = nsen/2 + (nsen%2);

      // First candidate
      int i1;
      {
        shared_ptr<int> ind;
        {
          for(int i = 0; i < N; i++){
            const int n = nmem[i];
            if( (!ind) || n > nmem[*ind] ) ind = shared_ptr<int>(new int(i));
          }
        }
        // Get rid of it for sure right now.
        i1 = *ind;
        const char p = 'A'+i1;
        ss << p;
        lcnv(p);
        nmem[i1]--;
        nsen--;
      }

      // Second candidate
      {
        shared_ptr<int> ind;
        int npleft=0;
        for(int i = 0; i < N; i++){
          const int n = nmem[i]; // takes into account the absence of the first.
          if( n > 0 ) npleft++;
          if( i == i1 ) continue;
          if( n == 0 ) continue; 
          // ignoring the first selected one from now on
          if( (!ind) || n > nmem[*ind] ) ind = shared_ptr<int>(new int(i));
        }
        if( ind ){
          const char p = 'A'+*ind;
          clog << "candidate:" << p << endl;
        }
        bool include = ind && ((nmem[*ind] > 1 ) || (npleft != 2) );
        if( include ){
          const char p = 'A'+*ind;
          lcnv( npleft );
          lcnv( *ind );
          lcnv( nmem[*ind] );
          lcnv(p);
          ss << p;


          nmem[*ind]--;
          nsen--;
        }
      }
      if( nsen ) ss << " ";
      lcnv( nsen );
      clog << endl;
    }


    solution = ss.str();
  }
  std::string solve() {
    return solution;
  }

  const int m_icase;

  int N=0;
  vector<int> nmem;
  int nsen=0;
  string solution = "TBD";
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
      clog << "---------------" << endl;
    }

    return 0;
  } catch ( const exception & e ){
    cerr << e.what() << endl;
    return 1;
  }
}

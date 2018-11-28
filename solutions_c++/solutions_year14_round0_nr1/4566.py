#include <fstream>

using namespace std ;

const int NMAX = 5 ;

ifstream cin("magictrick.in") ;
ofstream cout("magictrick.out") ;

int T ;
int X1, X2 ;
int A[NMAX][NMAX], B[NMAX][NMAX] ;
int act = 0, sol;

int main()
{
cin >> T ;
    while(T)
    {
        ++ act ;
        bool ok = false ;
        int cnt = 0 ;
        cin >> X1 ;
        for(int i = 1 ; i <= 4 ; ++ i)
            for(int j = 1 ; j <= 4 ; ++ j)
                cin >> A[i][j] ;
        cin >> X2 ;
        for(int i = 1 ; i <= 4 ; ++ i)
            for(int j = 1 ; j <= 4 ; ++ j)
                cin >> B[i][j] ;

            for(int j = 1 ; j <= 4 ; ++ j)
            {for(int jj = 1 ; jj <= 4 ; ++ jj)
               if(A[X1][j] == B[X2][jj])
                {
                    ok = true ;
                    ++ cnt ;
                    sol = A[X1][j] ;
                }
            }
                cout << "Case #" << act << ": " ;

                if(ok == true && cnt == 1)
                    cout << sol << '\n';
                    else if(ok == true && cnt > 1)
                        cout << "Bad magician!" << '\n' ;
                    else if(ok == false)
                        cout << "Volunteer cheated!" << '\n' ;
        -- T ;
    }
    cin.close() ;
    cout.close() ;
    return 0 ;
}

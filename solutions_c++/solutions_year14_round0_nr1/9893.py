#include<bits/stdc++.h>

#define SZ(X) (int)(X).size()
#define SS stringstream
#define MP make_pair
#define PB push_back

#define ALL(X) (X).begin(),(X).end()
#define ALLR(X) (X).rbegin(),(X).rend()
#define MEM(X,ZS) memset(X,ZS,sizeof(X))

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

#define f first
#define s second


using namespace std;
int toI(string S){ SS ss ; ss << S ; int n ; ss >> n ; return n ; }
string toS(int n){ SS ss ; ss << n ; string S ; ss >> S ; return S ; }
// 3awz arou7 :(

int tab1[4][4] , tab2[4][4] ;
int main(){

    READ("A-small-attempt0.in") ;
    WRITE("A-small-attempt0.out") ;

    int t , n , m , c , cc;
    cin >> t ;

    for(int k=1 ; k<=t ; k++)
    {
        cin >> n ;
        for(int i=0 ; i<4 ; i++)
            for(int j=0 ; j<4 ; j++)
              cin >> tab1[i][j] ;

        cin >> m ;
        for(int i=0 ; i<4 ; i++)
            for(int j=0 ; j<4 ; j++)
              cin >> tab2[i][j] ;

        c = 0 ;
        for(int i=0 ; i<4 ; i++)
            for(int j=0 ; j<4 ; j++)
                if(tab1[n-1][i] == tab2[m-1][j])
                    c++ , cc = tab1[n-1][i] ;

        cout << "Case #" << k << ": " ;

        if( c == 1 )
            cout << cc << endl ;
        else if( c > 1 )
            cout << "Bad magician!\n" ;
        else
            cout << "Volunteer cheated!\n" ;

    }

}

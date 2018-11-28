#include<bits/stdc++.h>

#define SZ(S) (int)S.size()
#define MEM(X,XX) memset(X,XX,sizeof(X))
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

/**    LAST STAND    **/
/**    Just for myself    **/
using namespace std;

int main(){

#ifndef ONLINE_JUDGE
READ("A-large.in") ;
WRITE("A-large.out") ;
//    READ("A-small-attempt3.in") ;
//    WRITE("A-small-attempt3.out") ;
#endif
/*
    WRITE("test.txt") ;
    cout << "1 1000\n";
    for(int i=0 ; i<1000 ; i++)
        cout << "0";
*/


 //   READ("test.txt");
    int t , n ,c , cc ;
    cin >> t ;

    string str ;
    for(int k=1 ; k<=t ; k++)
    {
        cin >> n >> str ;

        c = 0 , cc = str[0]-'0' ;
        for(int i=1 ; i<SZ(str) ; i++)
        {

            if( i > cc )
                c += (i-cc) , cc += (i-cc) ;
            cc += str[i]-'0' ;
        //    cout << i << " " << c << " " << cc << " " << str[i]-'0' << endl ;
//            c += ( (i>c) ? i-c : 0 ) ;
        }
        cout << "Case #" << k << ": " << c << endl ;
    }




}

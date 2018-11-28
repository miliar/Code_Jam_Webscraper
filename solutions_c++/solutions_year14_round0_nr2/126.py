#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T ;
    cin>>T ;
    int cnt = 1;
    while(T--)
    {
        double  C , F , X ;
        cin>>C>>F>>X ;
        long double rate  = 2 ;
        int nooffarms  = 1 ;
        double timetox  = X/rate ;
        double timetof = C/rate ;
        double newtimetox = X/(rate+nooffarms*F) + timetof;

        while(newtimetox < timetox )
        {
            timetox = newtimetox ;
            timetof += C/(rate+nooffarms*F ) ;
            nooffarms++ ;
            newtimetox = X/(rate+nooffarms*F) + timetof;
        }
        std::cout.setf( std::ios::fixed, std:: ios::floatfield );
        cout<<std::setprecision(7)<<"Case #"<<cnt++<<": "<<timetox<<endl ;

    }
    return 0 ;
}

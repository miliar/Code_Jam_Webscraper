#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;
 
 
int main()
{
   int  T ;
   cin >> T ;
   for ( int ii = 0 ; ii < T; ii ++)
    {
        int A ,  B ;
 
        cin >> A >> B;
        int tot = 0 ;
        for ( int i = A ; i <=B ; i ++)
            {
                ostringstream os ;
                os <<i ;
                string a = os.str() ;
 
                string  a2 = a ;
       // cout << a2 <<endl;
                reverse(a.begin(),a.end()) ;
 
                if ( a2 == a )
                {//   cout << a <<endl;
                int k = sqrt(i) ;
                if ( k * k  == i)
                {
                    ostringstream o ;
                    o << k ;
                    string b1 = o.str() ;
 
                    string b2 = b1 ;
 
                    reverse(b1.begin(),b1.end() ) ;
 
                    if ( b2 == b1)
                    {
                        tot ++ ;
                //cout << b2 <<endl;
                    }
 
            }
        }
 
 
 
 
 
    }
 
    cout <<"Case #"<<ii+1<<":"<<" "<< tot <<endl;
 
    }
 
return 0 ;
 
}
 

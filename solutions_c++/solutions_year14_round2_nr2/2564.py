#include<iostream>
#include<cstdio>
#include<vector>
#include<fstream>
#include<cmath>
#include<string>
#include<limits>
#include<climits>
#include<set>
#include<set>
#include<stack>
#include<list>

using namespace std;

#define cin fin
#define cout fout

typedef int typei;
typedef long long int typell;
typedef float typef;
typedef double typed;

//number of cases
typei T;
typei A;
typei B;
typei K;
typei result;
typei counter = 0;


int main(void)
{
 ifstream fin("B-small-attempt0.in");
 ofstream fout("output.txt");
    cin >> T; //get number of cases

    for( typei i = 0 ; i < T ; i++ ){
        counter = 0;

        cin >>A >> B >> K;
        cout << "Case #" << i+1 << ": " ;
        for ( int k = 0 ; k < A ; k++ )
        {
            for ( int j = 0 ; j < B ; j++ )
            {
                result = k&j;
               // cout << result;
                for ( int l = 0 ; l < K ; l++ )
                {
                    if( result == l ){
                        counter++;
                        break;
                    }
                }
            }
        }
        cout << counter << endl;

    }//end for loop and test cases
return 0;
}

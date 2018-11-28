#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> fairSquare;

int range(int a, int b)
{
    int result = 0;
    for( int i = 0; i < fairSquare.size(); i++ )
        if( fairSquare[i] >= a && fairSquare[i] <= b )
                result++;
    return result;
}

int main()
{
    int t, i, j;
    ifstream cin("C-small-attempt4.in");
    ofstream cout("a.out");
    fairSquare.push_back( 1 );
    fairSquare.push_back( 4 );
    fairSquare.push_back( 9 );
    fairSquare.push_back( 121 );
    fairSquare.push_back( 484 );
    cin >> t;
    int a, b;
    for( i = 1; i <= t; i++ )
    {
        cin >> a >> b;
        int result = range(a, b);
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}

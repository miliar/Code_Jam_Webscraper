#include <iostream>
#include <vector>

using namespace std;

int x1,x2;
vector<int> r1;
vector<int> r2;

void read_row( vector<int> &row, int row_index )
{
    for ( int j = 1; j <=4; ++j )
    {
        for ( int k = 1; k <=4; ++k )
        {
            int t;
            cin >> t;

            if ( j == row_index )
                row.push_back( t );
        }
    }
}

void ans_it()
{
    int match_count = 0;
    int c;
    for ( int i : r1 )
        for ( int j : r2 )
            if ( i == j )
            {
                ++match_count;
                c = i;
            }
    if ( match_count == 1 )
        cout << c << endl;
    else if ( match_count == 0 )
        cout << "Volunteer cheated!" << endl;
    else
        cout << "Bad magician!" << endl;
}

int main()
{
    int case_count = 0;
    cin >> case_count;
    for ( int i = 0; i < case_count; ++i )
    {
        cin >> x1;
        r1.clear();
        read_row( r1, x1 );
        r2.clear();
        cin >> x2;
        read_row( r2, x2 );

        cout << "Case #" << i + 1 << ": ";
        ans_it();
    }
    return 0;
}

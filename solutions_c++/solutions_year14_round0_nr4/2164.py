#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

void error( const char *str)
{
    cout << str;

    exit( 1);
}

int main()
{
    ifstream input( "input.txt");

    if ( !input )
        error( "Cannot open input file");

    ofstream output( "output.txt");

    if ( !output )
        error( "Cannot open output file");

    int num_cases;

    input >> num_cases;

    for ( int i = 0; i < num_cases; i++ )
    {
        int N;

        input >> N;

        vector<double> Naomi( N);
        vector<double> Ken( N);

        for ( int j = 0; j < N; j++ )
            input >> Naomi[j];

        for ( int j = 0; j < N; j++ )
            input >> Ken[j];

        sort( Naomi.begin(), Naomi.end());
        sort( Ken.begin(), Ken.end());

        int count_fair = 0, count_unfair = 0;
        int Ken_ind_fair = 0;
        int Ken_ind_unfair_low = 0, Ken_ind_unfair_high = N - 1;

        for ( int j = 0; j < N; j++ )
        {
            while ( Ken_ind_fair < N &&
                    Ken[Ken_ind_fair] < Naomi[j] )
            {
                Ken_ind_fair++;
            }

            if ( Ken_ind_fair == N )
                count_fair++;
            else
                Ken_ind_fair++;

            if ( Naomi[j] < Ken[Ken_ind_unfair_low] )
                Ken_ind_unfair_high--;
            else
            {
                count_unfair++;
                Ken_ind_unfair_low++;
            }
        }

        output << "Case #" << i + 1 << ": " << count_unfair << " " << count_fair << "\n";
    }

    return 0;
}

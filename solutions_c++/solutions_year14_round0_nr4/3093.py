#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

vector<double> blocksNaomiFirst;
vector<double> blocksNaomiSec;
vector<double> blocksKenFirst;
vector<double> blocksKenSec;

int main()
{
    vector<int> naomiNoCheat;
    vector<int> naomiCheat;

    int testCases = 0;
    cin >> testCases;

    for ( int i = 0; i < testCases; ++i )
    {
        int numBlocks = 0;
        cin >> numBlocks;

        naomiNoCheat.push_back( 0 );
        naomiCheat.push_back( 0 );

        for ( int j = 0; j < numBlocks; ++j )
        {
            double tmp;
            cin >> tmp;
            blocksNaomiFirst.push_back( tmp );
            blocksNaomiSec.push_back( tmp );
        }

        for ( int j = 0; j < numBlocks; ++j )
        {
            double tmp;
            cin >> tmp;
            blocksKenFirst.push_back( tmp );
            blocksKenSec.push_back( tmp );
        }

        sort( blocksNaomiFirst.begin(), blocksNaomiFirst.begin() + ( numBlocks ) );
        sort( blocksKenFirst.begin(), blocksKenFirst.begin() + ( numBlocks ) );
        sort( blocksNaomiSec.begin(), blocksNaomiSec.begin() + ( numBlocks ) );
        sort( blocksKenSec.begin(), blocksKenSec.begin() + ( numBlocks ) );

        for ( int j = 0; j < numBlocks; ++j )
        {
            double tmpKen[2] { 0, 0 };
            int counter = 0;

            for ( auto k : blocksKenFirst )
            {
                if ( k > blocksNaomiFirst[0] )
                {
                    tmpKen[0] = k;
                    tmpKen[1] = counter;
                    break;
                }
                counter++;
            }

            if ( tmpKen == 0 )
            {
                tmpKen[0] = blocksKenFirst[0];
                tmpKen[1] = 0;
            }

            if ( tmpKen[0] < blocksNaomiFirst[0] )
                ++naomiNoCheat[i];

            blocksNaomiFirst.erase( blocksNaomiFirst.begin() );
            blocksKenFirst.erase( blocksKenFirst.begin() + tmpKen[1]  );

            counter = 0;
        }

        for ( int j = 0; j < numBlocks; ++j )
        {
            double told = 0;
            int index = 0;
            int kenSize = blocksKenSec.size();
            int naomiSize = blocksNaomiSec.size();

            if ( blocksNaomiSec[ 0 ] > blocksKenSec[ kenSize - 1 ] )
            {
                told = blocksNaomiSec[ 0 ];
                index = 0;
            }
            else if ( blocksNaomiSec[ 0 ] > blocksKenSec[ 0 ] )
            {
                told = blocksNaomiSec[ naomiSize - 1 ];
                index = 0;
            }
            else
            {
                told = blocksKenSec[ kenSize - 1 ] - 0.00001;
                index = 0;
            }

            double tmpKen[2] { 0, 0 };
            int counter = 0;

            for ( auto k : blocksKenSec )
            {
                if ( k > told )
                {
                    tmpKen[0] = k;
                    tmpKen[1] = counter;
                    break;
                }
                counter++;
            }

            if ( tmpKen == 0 )
            {
                tmpKen[0] = blocksKenFirst[0];
                tmpKen[1] = 0;
            }

            if ( tmpKen[0] < told )
                ++naomiCheat[i];

            blocksNaomiSec.erase( blocksNaomiSec.begin() + index );
            blocksKenSec.erase( blocksKenSec.begin() + tmpKen[1]  );
        }
    }

    for ( int i = 0; i < testCases; ++i )
    {
        printf( "Case #%d: %d %d\n", i+1, naomiCheat[i], naomiNoCheat[i] );
    }
}

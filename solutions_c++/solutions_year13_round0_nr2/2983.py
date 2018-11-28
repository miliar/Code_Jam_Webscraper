#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <fstream>
#include <iostream>

#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <utility>

using namespace std;







int main(void)
{
	int T;
	int a,i,j,k,l,n,m;

    int N,M;
    int lawn[100][100];
    bool ans;
    
    int high;
    bool bad;

	fstream input, output;

	input.open("B-large.in", fstream::in);
	output.open("output.txt", fstream::out);

	if ( ! input.is_open() || ! output.is_open() )
	{
		cout << "well..." << endl;
		return -1;
	}

	input >> T;

	for ( n = 0; n < T; n++ )
	{
		input >> N >> M;
        
        high = 0;
		for ( i = 0; i < N; i++ )
        {
            for ( j = 0; j < M; j++ )
            {
                input >> lawn[i][j];
                if ( lawn[i][j] > high )
                    high = lawn[i][j];
            }
        }
        
        ans = true;
        for ( i = 0; i < N; i++ )
        {
            for ( j = 0; j < M; j++ )
            {
                bad = false;
                a = lawn[i][j];
                for ( l = 0; l < N; l++ )
                    if ( lawn[l][j] > a )
                        bad = true;
                if ( bad )
                    for ( l = 0; l < M; l++ )
                        if ( lawn[i][l] > a )
                        {
                            ans = false;
                            goto IMPOSSIBLE; // hehe
                        }
            }
        }
        IMPOSSIBLE:
        
        

		output << "Case #" << n+1 << ": ";
		
        if ( ans )
            output << "YES" << endl;
        else
            output << "NO" << endl;
	}

	input.close();
	output.close();

	return 0;
}







/* */
#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("output.txt");
    int i,N,T,m,c,freq[10],k;
    fin >> T;
    for( i = 1; i <= T; i++ )
    {
        fin >> N;
        if( N == 0)
        {
            fout << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            c = 0;
            memset( freq, 0, sizeof(freq) );
            for( m = N; c < 10; m += N )
            {
                k = m;
                while( k > 0 )
                {
                    if( freq[ k % 10 ]++ == 0)
                    {
                        c++;
                    }
                    k/=10;
                }
            }
            fout << "Case #" << i << ": " << m-N << endl;
        }
    }

    return 0;
}

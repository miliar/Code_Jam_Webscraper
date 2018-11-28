#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int N;

int main()
{
    cin >> N;

    for( int i=0; i<N; i++ ){
        string s;
        
        cin >> s;

        s.push_back('+');

        int c = 0;
        for( int j=1; j<s.length(); j++ ){
            if( s[j-1] != s[j] ) c++;
        }

        printf( "Case #%d: %d\n", i+1, c );
    }
        
}

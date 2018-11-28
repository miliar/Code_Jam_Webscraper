#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int N;
int case_no;

bool check_digits( vector<bool> & d )
{
    return count(d.begin(), d.end(), true ) == 10;
}

void fill_digits( int n, vector<bool> & d )
{
    string s = to_string(n);

    for( int i=0; i<s.length(); i++ ){
        d[s[i]-'0'] = true;
    }
    
}

void sheep( int n )
{
    vector<bool> d(10,false);

    for( int i=1; i<=1000000; i++ ){
        fill_digits(n*i,d);
        if( check_digits(d) ){
            printf( "Case #%d: %d\n", case_no, n*i );
            return;
        }
    }

    printf( "Case #%d: INSOMNIA\n", case_no );
    
}

int main()
{
    cin >> N;
    case_no = 1;

    for( int i=0; i<N; i++ ){
        int n;
        cin >> n;
        sheep(n);
        case_no ++;
    }
}

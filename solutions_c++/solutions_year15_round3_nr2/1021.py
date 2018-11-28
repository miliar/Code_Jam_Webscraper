#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <stdio.h>
using namespace std;

string target , letters ;
double ans ;
int s ;
int num ;
int MAX ;
int match ;
int coun(string lol)
{
    int got = 0 ;
    for ( int i = 0 ; i < lol.size() ; i++ )
    {
        if ( lol.find(target,i) != lol.npos )
        {
            i = lol.find(target,i);
            got++;
        }
    }
    return got ;
}
void solve( string tmp)
{
    if ( tmp.size() == s )
    {
        int koko = coun(tmp);
        num++;
        match += koko;
        MAX = max(koko,MAX);
        return ;
    }
    for ( int i = 0 ; i < letters.size() ; i++ )
        solve(tmp+letters[i]);
}

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t ;
    cin >> t ;
    int k , l ;
    for ( int i = 1 ; i <= t ; i++ )
    {
        num  = 0;
        MAX  = 0;
        match= 0;
        cin >> k >> l >> s ;
        cin >> letters >> target ;
        solve("");
        cout << "Case #" << i << ": " ;
        cout << setprecision(6) <<fixed<< (double)MAX - (double)((double)match/num);
        cout << endl;
    }
    return 0;
}

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <iterator>
#include <algorithm>
#include <numeric>

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;

#define fr(i, a, b) for(i = (a); i < (b); ++i)
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
 
#define ROW_LEN 4

bool IsWin(string str, char c)
{
    int i = 0;
    multimap<int, int, less<int> > m;
    m.insert(pii(0,5)); m.insert(pii(3,3)); m.insert(pii(0,1)); m.insert(pii(4,1)); 
    m.insert(pii(8,1)); m.insert(pii(12,1)); m.insert(pii(0,4)); m.insert(pii(1,4)); 
    m.insert(pii(2,4)); m.insert(pii(3,4));
    
    tr(m, it) 
    {
        int pos = it->first;
        vi v;
        fr(i, 0, ROW_LEN)
        {
            v.pb( str[pos] == c || str[pos] == 'T' ? 1 : 0 );   
            pos+= it->second;
        }
        if ( accumulate(all(v), 0) == 4 ) return true;
    }
    return false;
}

int main() 
{
    int T = 0, i = 0, j = 0;
    string s;
    //ifstream fin("../src/A-small-attempt0.in");
    
    ifstream fin("A-large-attempt0.in");
	ofstream fout("A-large-attempt0.out");
    
    fin >> T; getline(fin, s, '\n');
    fr(i, 0, T)
    {   
        string board, ans;
        fr(j, 0, ROW_LEN) 
        {
            getline(fin, s, '\n');
            board+=s;
        }
        getline(fin, s, '\n'); // empty row
        if ( IsWin(board, 'X') ) 
            ans = "X won";
        else if ( IsWin(board, 'O') )
            ans = "O won";
        else if ( board.find('.') != string::npos )
            ans = "Game has not completed";
        else
            ans = "Draw";
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
}
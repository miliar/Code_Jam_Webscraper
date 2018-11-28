#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <sstream>
#include <iomanip>
#include <map>
#include <set>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

ifstream in;
ofstream out;

int T;

typedef vector<pair<int,int> > vp; //Define vector of pairs
typedef vector<vector<pair<int,int> > > vvp; //Define vector of vector of pairs

template< typename T, size_t N, size_t M >
inline void printArray( T(&theArray)[N][M], T a, T b  ) {
    
    for ( int x = 0; x < a; x ++ ) {
        for ( int y = 0; y < b; y++ ) {
            cout << (char)theArray[x][y] << "";
            out << (char)theArray[x][y] << "";
        }
        cout << endl;
        out << endl;
    }
};

struct sort_pred {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        if (left.second > right.second)
            return true;
        else if(left.second == right.second)
            return left.first > right.first;
        else
            return false;
    }
};

int A, B, K;

int main ()
{
    // Create input/Output Streams
    in.open("data.in");
    out.open("data.out");
    
    //Read N
    in >> T;
    
    for (int t = 0; t < T; t++)
    {
        in >> A >> B >> K;
        
        vector<int> k;
        k.clear();
        
        for(int i = 0; i < A; ++i)
        {
            for(int x = 0; x < B; ++x)
            {
                k.push_back(i&x);
            }
        }
        
        int num = 0;
        tr(k, n)
        {
            if(*n < K )
                num++;
        }
        
        out << "Case #" << t+1 << ": " << num;
        cout << "Case #" << t+1 << ": " << num;
        
        //out.setf(ios::fixed); out.setf(ios::showpoint); out.precision(6);
        //cout.setf(ios::fixed); cout.setf(ios::showpoint); cout.precision(6);
        
        out << endl;
        cout << endl;
    }
    
    return 0;
}

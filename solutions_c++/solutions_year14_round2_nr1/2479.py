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

int N;
int difChar[1001][100];
int chars[1001][100];

int main ()
{
    // Create input/Output Streams
    in.open("data.in");
    out.open("data.out");
    
    //Read N
    in >> T;
    
    for (int t = 0; t < T; t++)
    {
        in >> N;
        memset(difChar, 0, sizeof(difChar));
        memset(chars, 0, sizeof(chars));
        
        vector<string>strings;
        strings.clear();
        
        int maxDif = 0;
        int minDif = 999999;
        
        for(int i = 0; i< N; ++i)
        {
            string s;
            in >> s;
            strings.push_back(s);
        
            set<char> tmp;
            int charIndex = 0;
            int began = 0;
            
            tr(s,c)
            {
            
                
                    if(difChar[i][charIndex] != *c)
                    {
                        if(began)
                            charIndex++;
                        else
                            began = 1;
                        
                        difChar[i][charIndex] = *c;
                        chars[i][charIndex]++;

                    }
                    else
                    {
                        chars[i][charIndex]++;
                    }
            }
            
            maxDif = max(maxDif, charIndex);
            minDif = min(minDif, charIndex);
        }

        
        out << "Case #" << t+1 << ": ";
        cout << "Case #" << t+1 << ": ";
        
        int possible = 1;
        int minChange;
        
        if(maxDif == minDif)
        {
            
            //Make sure it is possibel
            for(int i = 1; i < N; ++i)
            {
                for(int x = 0; x <= maxDif; x++)
                {
                    if(difChar[i][x] != difChar[i-1][x])
                    {
                        possible = 0;
                        i = N;
                        break;
                    }
                }
            }
            
            if(possible)
            {
                int top = N;
                
                /*for(int i = 0; i < N; ++i)
                {
                    for(int x = 0; x < maxDif; x++)
                    {
                        if(chars[i][x] > 1)
                        {
                            int z = chars[i][x];
                            while(z > 0)
                            {
                                for(int b = 0; b < maxDif; ++b)
                                {
                                    if(b == x)
                                    {
                                        chars[top][b] = z;
                                    }
                                    else
                                    {
                                        chars[top][b] = chars[i][b];
                                    }
                                    
                                    difChar[top][b] = difChar[i][b];
                                }
                                z--;
                                top++;
                            }
                            
                        }
                    }
                }*/
                
                minChange = 0;
                
                for(int z = 0; z < N; ++z)
                {
                    for(int x = 0; x <= maxDif; x++)
                    {
                        minChange += abs(chars[z][x]-1);
                    }
                }
                
                //Find score
                for(int i = 0; i < top; ++i)
                {
                    int score = 0;
                    
                    for(int z = 0; z < N; ++z)
                    {
                        for(int x = 0; x <= maxDif; x++)
                        {
                            score += abs(chars[z][x]-chars[i][x]);
                        }
                    }
                    
                    minChange = min(minChange,score);
                    
                    if(minChange == 0)
                        break;
                }
                
                cout << minChange;
                out << minChange;
            
            }
            else
            {
                cout << "Fegla Won";
                out << "Fegla Won";
            }
        }
        else
        {
            cout << "Fegla Won";
            out << "Fegla Won";
        }
        out << endl;
        cout << endl;
    }
    
    return 0;
}

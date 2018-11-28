#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <climits>
#include <iostream>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
#define ll long long
#define ull unsigned long long
#define inf 0x3f3f3f3f
#define infl 0x3FFFFFFFFFFFFFFFLL
#define np next_permutation
#define pp prev_permutation
#define mp make_pair
#define abs(x) (((x) < 0) ? - (x) : (x))
#define pi 3.1415926535897932384626433832795
#define sz(a) int((a).size()) 
#define fr first
#define sc second
#define pb push_back 
#define fors(i, s) for(int i = 0; i < sz(s); i++)
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define TRvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define present(c,x) ((c).find(x) != (c).end()) 
using namespace std;
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction
typedef vector<string> vs;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef pair<ii,int> iii; 
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef map<string, int> si;
typedef map<int, string> is;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    //system("PAUSE");
    int T;
    int M;
    int empe;
    int convidar;
    
    cin >> T;
    for (int i=0; i<T ; i++)
    {
    	empe = 0;
    	convidar = 0;
    	cin >> M;
    	char r[M+1]; 
    	cin >> r; 
        
        empe = (int)r[0] - 48;
        for (int j = 1; j<=M ; j++)
        {
        	if (empe >= j)
        	{
        	   empe+=(int)r[j] - 48;
			}
        	else
        	{
        		convidar += j - empe;
        		empe += j - empe; 
        		empe += (int)r[j] - 48;
			}
		}
		cout << "Case #" << i+1<< ": " << convidar << "\n";
	}
    
    return 0;
}








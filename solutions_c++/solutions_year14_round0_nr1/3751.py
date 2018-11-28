//Aditya Dixit
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <functional>
#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <cmath>
#include <numeric>
#include <set>

using namespace std;

#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#define LIM
#define MOD 1000000009
#define pb push_back
#define mp make_pair
#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define DBG(vari) cerr<<#vari<<" ==> "<<(vari)<<endl;

const int INF = 2000000000;

typedef long long int i64;
typedef long int i32;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector <PII> VPII;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("aaout.txt","w",stdout);
	
	std::ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	
	int x = 1;
	while(t--)
	{
		int a;
		cin >> a;
		
		int deck1[4][4],deck2[4][4];
		
		for(int i = 0; i < 4 ; i++)
			for(int j = 0; j < 4 ; j++)
				cin >> deck1[i][j];
				
		int b;
		cin >> b;
		
		for(int i = 0; i < 4 ; i++)
			for(int j = 0; j < 4 ; j++)
				cin >> deck2[i][j];
		
		int cnt = 0,ans = 0;
		for(int i = 0; i < 4 ; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if( deck1[a-1][i] == deck2[b-1][j])
				{
					ans = deck1[a-1][i];
					cnt++;
				} 
			}
		}
		
		if( cnt == 1 )
		cout << "Case #"<< x <<": "<< ans << endl;
		else if( cnt > 1 )
		cout << "Case #"<< x <<": Bad magician!" << endl;
		else
		cout << "Case #"<< x <<": Volunteer cheated!" << endl;
		
		x++;
	}
	
    return 0;
}





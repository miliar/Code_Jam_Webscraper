#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//---------- macros ----------
#define fp(i,a,b) for(int i=a; i<b; i++)
#define fm(i,a,b) for(int i=a; i>b; i--)
#define xwon "X won"
#define owon "O won"
#define draw "Draw"
#define incomplete "Game has not completed"

using namespace std;

int t, n, m;  long D; int _case;
int lawn[100][100];
bool valid;
int low, h, boundaryH;
int lx,ly;


int main()
{
    _case=1;		
    cin >> t;
    while(_case<=t)
    {
		cin >> n >> m;
		fp(i,0,n){
			fp(j,0,m){
				cin >> lawn[i][j];
			}
		}
		valid = false;
		fp(i,0,n){
			valid = true;
			fp(j,0,m){
				h = lawn[i][j];
				valid = true;
				fp(k,0,m){
					if(lawn[i][k] > h){
						valid = false;
						break;
					}
				}
				if(!valid){
					valid = true;
					fp(k,0,n){
						if(lawn[k][j] > h){
							valid = false;
							break;
						}
					}
				}
				if(!valid) break;
			}
			if(!valid) break;
		}
		
        cout <<"Case #"<< _case <<": ";
	    if(valid)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
        _case++;
    }
	return 0;
}

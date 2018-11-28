/*input
5
1
2
3
4
5
*/
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef long long LL;
typedef pair<int,int> ii;
typedef pair<string,int> si;
typedef pair<int,ii> iii;
typedef vector <si> vsi;
typedef vector <ii> vii;
typedef vector <int> vi;
typedef vector <string> vs;
typedef map <string,int> msi;
#define INF 1000000000
#define pb push_back
#define mp make_pair
#define lp(i,j,k) for(int i=0;i<j;i+=k)
#define lpe(i,j,k) for(int a=i;a<=j;i+=k)
#define bitcount(x) __builtin_popcount(x)
int power(int x, unsigned int y){
    int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}

int main(){
    ios_base::sync_with_stdio(0);
  	freopen("in.txt", "r", stdin);
  	freopen("out.txt", "w", stdout);
    LL t,n;
    cin>>t;
    LL cs=0;
    set<LL> fd;
    while(t--){
    	fd.clear();
    	cin>>n;
    	if(n == 0 ){ cout<<"Case #"<<++cs<<": "<<"INSOMNIA"<<endl;continue;}
    	bool entr=false;
    	for (int i = 1; i <= 100 && !entr; ++i)
    	{
    		LL mult=i*n;
    		LL xx = mult;
    		while(xx>0){
    			LL z = xx%10;
    			xx /= 10;
    			fd.insert(z);
    		}
    		if(fd.size() == 10){
    			entr=true;
    			cout<<"Case #"<<++cs<<": "<<mult<<endl;
    			break;
    		}
    	}
    }
 return 0;

}

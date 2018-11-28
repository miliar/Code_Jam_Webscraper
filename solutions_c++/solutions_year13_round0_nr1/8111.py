#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cmath>
#include <list>
#include <cstdlib>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define FOR(i,a,b)  for(int (i) = (a);(i)<(b);(i)++)
#define   REP(i,n) FOR(i,0,n)
#define  INF (1<<29)
#define         pb push_back
#define 	     sz size()
#define         mp make_pair
#define all(a) a.begin(),a.end()
#define SI(n)               scanf("%d",&n);
#define SL(n)               scanf("%lld",&n);
#define fill(ar,val) memset(ar,val,sizeof ar)
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define fi first
#define se second
typedef long long ll;
typedef pair<int,int>  pii;
typedef vector<string> vs;
ll s2i(string s) { istringstream iss(s); ll x;iss>>x; return x;}
string i2s(ll x) { ostringstream oss; oss<<x; return oss.str();}




int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output1.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	int c1 = 1;
	char cz;
	while ( t-- ) {
		string s[4];
		for ( int i = 0; i < 4;i++) {
			cin >> s[i];
			//cout << s[i] << endl;
		}
		char a[4][4];
		int w = -1;
		int flag = 0;
		for ( int i = 0; i < 4;i++) {
			for ( int j = 0; j < 4;j++) {
				//scanf("%c",&a[i][j]);
				a[i][j] = s[i][j];
				//cout << a[i][j] << endl;
				if (a[i][j] == '.')
					flag = 1;
			}
		}
	
		//cin >> cz;
		for ( int i = 0; i < 4; i++) {
			char c = a[i][0];
			int count = 1;
			
			for ( int j = 1; j < 4; j++) {
				if ( c =='.')
					break;
				if ( a[i][j] == c || a[i][j] =='T' )
					count++;	
			}
			if ( c =='T')
				c = a[i][1];
			if ( count == 4) {
			  //  cout <<"esf" << count << endl;
			    if ( c == 'O')
				w = 0;
			    else
				w = 1;
			} 
			c = a[0][i];
			count = 1;
			if ( c == 'T')
				c = a[1][i];
			for ( int j = 1; j < 4; j++) {
				if ( c== '.')
					break;
				if ( a[j][i] == c || a[j][i] == 'T')
					count++;
			}
			if ( count == 4) {
			//	cout << count << endl;
				if ( c == 'O')
					w = 0;
				else
					w = 1;
			}
		}
		char c = a[0][0];
		int count = 1;
		if ( c == 'T')
			c = a[1][1];
		for ( int i = 1; i < 4;i++) {
			if ( c == '.')
				break;
			if ( c == a[i][i] || a[i][i] == 'T')
				count++;
		}			
		if ( count == 4) {
			   //cout << "FFE "<< count << endl;
                            if ( c == 'O')
                                w = 0;
                            else
                                w = 1;
               	}
		 c = a[0][3];
		 count = 1;
		int j = 1;
		if ( c == 'T')
			c = a[1][2];
		for ( int i = 2; i >= 0; i--) {
			if ( c == '.')
				break;
			if ( a[j][i] == 'T' || a[j][i]== c)
				count++;
			j++;
		}
		if ( count == 4) {	
		//	cout <<"fs "<< count << endl;
                	if ( c == 'O')
                                w = 0;
                            else
                                w = 1;
                }
		if( w == 1)
			cout <<"Case #"<<c1<<": "<<"X won"<< endl;
		else if ( w ==0 ) 
			cout <<"Case #"<<c1<<": "<<"O won"<< endl;
		else if ( flag == 0)
			 cout <<"Case #"<<c1<<": "<<"Draw"<< endl;
		else
			cout <<"Case #"<<c1<<": "<<"Game has not completed"<< endl;

		c1++;
	}

	return 0;
}










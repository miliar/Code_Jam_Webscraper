

#include <bits/stdc++.h>
using namespace std;

#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define pb push_back
#define mp make_pair
#define rep(i, m) for( i = 0 ; i < (int)m ; i ++)

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;

#define N 100005

string great(string a , string b){
	int l = a.size();
	for ( int  i = 0 ; i < l ; i ++ ){
		if ( a[i] > b[i] ) return a;
		else if ( a[i] < b[i]) return b;
	}
	return a;
}
int a, b, c, i, j, k;
int main ()
{
	int t;
	scanf("%d",&t);
	string str;
	int ll = 1;
	string st;
	while ( t -- ){
		cin >> str ;	
		int len = str.size();
		st = "";
		st +=str[0];
		for ( int i = 1  ; i < len ; i ++ )
		{
			st = great(st+str[i],str[i]+st);
		}
		cout << "Case #"<< ll++ << ": "<< st << endl;
		str.clear();
		st.clear();

	}
	return 0;
}

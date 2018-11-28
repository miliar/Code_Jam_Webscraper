/*
GOOGLE CODEJAM 2014
ROUND 1B
prob: A
id: i.amlansaha@gmail.com
lang: C++
date: May 3, 2014
algo: 
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef map<int, int> MAPII;
typedef map<string,int> MAPSI;

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define ROF(i,a,b) for(i=a;i>=b;i--)
#define FR(i,n)	for(i=0;i<n;i++)
#define RF(i,n) for(i=n;i>0;i--)
#define CLR(a) memset ( a, 0, sizeof ( a ) )
#define RESET(a) memset ( a, -1, sizeof ( a ) )
#define PB(a)	push_back ( a )


int main ()
{
//	freopen("A-small.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-output.out", "w", stdout);

    int i, j, k, l, temp, t, n, ans, caseno = 0;

    VI trck[105];
    string str[105], temps, temp0;
    scanf ( "%d", &t );
    
    while ( t-- )	{
    	scanf ( "%d", &n );
    	FR ( i, n )	trck[i].clear();
    	temps.clear();
    	temp0.clear();
    	FR ( i, n )	{
    		str[i].clear();
    		cin >> str[i];
    	}
    	ans = -1;
    	l = str[0].size();
    	k = 0;

		char ch = str[0][0];
		int len = 1;

		for (j = 1; j < str[0].size(); j++) {
			if (ch != str[0][j]) {
				temp0 += ch;
				trck[0].push_back(len);
				ch = str[0][j];
				len = 1;
    		}
    		else	len++;
    	}
    	temp0+= ch;
    	trck[0].push_back(len);

    	FOR ( i, 1, n-1 )	{
    		ch = str[i][0];
    		len = 1;
    		temps.clear();
    		int ll = str[i].size();
    		for ( j = 1; j < ll; j++){
    			if ( ch != str[i][j] )	{
    				temps+= ch;
    				trck[i].push_back(len);
    				ch = str[i][j];
    				len = 1;
    			}
    			else	len++;
    		}
			temps+= ch;
			trck[i].push_back(len);
			if ( temps != temp0 )	{
				ans = 0;
				break;
			}
    	}

    	printf ( "Case #%d: ", ++caseno );
    	if ( ans == 0 )	{
    		printf("Fegla Won\n");
    		continue;
    	}

    	ans = 0;
    	l = temp0.size();
//    	cout << "PPPPP";
    	FR ( i, l )	{
    		VI tempv;
    		tempv.clear();
    		FR ( j, n )	tempv.push_back(trck[j][i]);
    		sort(tempv.begin(), tempv.end());
    		temp = tempv[n/2];
    		FR ( j, n )	ans+= abs(temp-trck[j][i]);
    	}
    	printf ( "%d\n", ans );
    }
    return 0;
}

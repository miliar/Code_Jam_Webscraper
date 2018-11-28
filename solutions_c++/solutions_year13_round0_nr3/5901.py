//--BY--©--WA-
#include<iostream> //cout, cin, getline

#include<algorithm> //find, reaplce, swap, sort, lower_bound, uper_bound, binnary_search...
#include<vector> //push_back, size, resize, 
#include<string>
#include<queue> //empty, front, back, push
#include<stack> //push, top, empty
#include<map>
#include<set>
#include<list> //spajazny zoznam .. vsetko v O(1)

#include<stdio.h> //printf, scanf, getchar, putchar
#include<math.h> //cos, sin, exp, pow, sqrt,  flnoor, cell
#include<stdlib.h> //atio, atl, strtod, strtol, atof, abs, 
#include<ctype.h> //isalnum, isalpha, isdigit, islower, isupper, toupper, tolower, 
#include<string.h> //strcm, strstr, strlen,

using namespace std;

#define FOREACH(obj,it) for(__typeof(obj.begin()) it = (obj).begin(); it != (obj).end(); (it)++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define REP(i,a,b) for(int i=a; i<b; i++)
#define DEBUG(V,S) FOR(i,0,S-1){cout << i << ". " << V[i] << endl;}

#define PB push_back
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define MP make_pair
#define fi first
#define se second

#define SIZE(s) (int) (s).size()

#define INF 987654321
#define EPS 1e-9
#define ld long double // %Lf, double %lf
#define ll long long   // %llf

//--------------------------------------------------------------------------------------
//


int N, A, B;

string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp = "";
    string returnvalue = "";
    while (number > 0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i = 0; i < SIZE(temp); i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}


bool is_pal(int x) {
	string s = convertInt(x);
	bool ok = true;
	FOR (i, 0, SIZE(s)-1) {
		if (s[i] != s[SIZE(s)-1-i]) ok = false;
	}
	return ok;
}

int main()
{

	scanf("%d\n", &N);
	FOR (q, 1, N) {
		printf("Case #%d: ", q);

		scanf("%d %d\n", &A, &B);

		int poc = 0;
		FOR (i, A, B) {
			int odm = round(sqrt(i));
			if (odm*odm == i && is_pal(i) && is_pal(odm)) poc++;
		}
		printf("%d\n", poc);
	}
	
	return 0;
}

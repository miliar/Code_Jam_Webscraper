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

#define MAX 147

int N,M,BN;
int A[MAX], B[MAX];

int find()
{
	if (BN == 0) return 0;
	
	int BM = M;
//specialny pripad
	if (BM == 1)
	{
		//cout << "tu" << endl;
		return BN;
	}
	
	//zaciname s M co sme si nacitali
	int k = 0;
	int added = 0;
	while(true)
	{
		if (k == BN)
			return added;
			
		if (B[k] >= BM)
		{
			//musime pridat
			added++; //[pridali sme jedno
			BM+= BM-1;
		}
		else
		{
			BM += B[k];
			k++;
		}
	}
	return BN;
}

int best()
{
	int a = 1;
	FOR(i,1,N)a*= 2;
	int best = INF;
	FOR(step,0,a)
	{
		//cout << "step: "<< step << endl;
		int kolko = 0;
		BN = 0;
		FOR(i,0,N-1)
		{
			//cout << i << " ";
			if ( (step & (1<<i)) == (1<<i))
			{
				//cout << "ano";
				B[BN] = A[i];
				BN++;
				kolko++;
			}
			//cout << endl;
		}
		kolko = N-kolko;
		//cout << kolko << " " << (find()) << endl;
		kolko+= find();
		if (kolko < best) best = kolko;
	}
	return best;
}

int main()
{
	//cout << (1<<0);
	//return 0;
	
	int Q;
	scanf("%d",&Q);
	FOR(q,1,Q)
	{
		scanf("%d %d",&M,&N);
		FOR(i,0,N-1) scanf("%d",A+i);
		sort(A,A+N);
		
		printf("Case #%d: %d\n",q,best());
	}
	return 0;
}

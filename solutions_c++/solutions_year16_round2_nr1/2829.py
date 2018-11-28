/*
 * first.cpp/*
 * new_template.cpp
 *
 *  Created on: Apr 18, 2016
 *      Author: Nizam
 */


#include <bits/stdc++.h> // Contains all useful header files

using namespace std;

// Data types
#define ll 				long long
#define llu 			long long unsigned
#define ui				unsigned int
#define ld				long double
// Input macros
#define s(n) 			int (n); scanf("%d", &n)
#define sc(n) 			char (n); scanf("%c", &n)
#define sl(n) 			llu (n); scanf("%I64d", &n)
#define sf(n) 			double (n); scanf("%lf", &n)
#define ss(n) 			string (n); cin >> n
#define sArr(src, N)	FR(i, 0, N) cin >> src[i]
// Output macros
#define p(n)			printf("%d", n)
#define pn(n)			printf("%d\n", n)
#define pl(n)			printf("%I64d ", n)
#define pln(n)			printf("%I64d\n ", n)
#define pf(n)			printf("%f ", n)
#define pfn(n)			printf("%f\n", n)
#define ps(n)			cout<<n
#define psn(n)			cout<<n<<endl
// Useful constants
#define INF				(int)1e9
#define EPS				1e-9
// Useful hardware instructions
#define bitcount		__builtin_popcount
#define gcd				__gcd
// Useful bit manipulations
#define bit(x, i) 		(x & (1<<i))							// Select the bit of position i of x
#define lowbit(x)		((x) & ((x) ^ ((x) - 1)))				// Get the lowest bit of x
#define hBit(msb, n)	asm("bsrl %1, %0" : "=r"(msb) : "r"(n)) // Get the highest bit of x
// Inequalities
#define IN(i, l, r)		((l<i) && (i<r))
#define LIN(i, l, r)	((l<=i) && (i<r))
#define INR(i, l, r)	((l<i) && (i<=r))
#define LINR(i, l, r)	((l<=i) && (i<=r))
// Useful traversal macros
#define FR(i, l, r)		for(int i=l; i<r; i++)
#define FL(i, r, l)		for(int i=r; i>l; i--)
#define FRL(i, l, r)	for(llu i=l; i<r; i++)
#define FOREACH(i, t)	for(typeof(t.begin()) i=t.begin(); i!=t.end(); i++)	// Traverse an STL data structure
#define ALL(c)			(c).begin(), (c).end()					// For functions like sort()
#define PRESENT(c, x)	(find(ALL(c), x) != (c).end())
// For map, pair
#define mp				make_pair
#define fi				first
#define se	 			second
// For vectors
#define pb				push_back
typedef vector<int>		vi;
typedef vector<vi>		vii;
typedef pair<int, int>	ii;
// Some common useful functions
#define maX(a, b) 		((a) > (b) ? (a) : (b))
#define miN(a, b) 		((a) < (b) ? (a) : (b))
#define RESET(a, x)		memset(a, x, sizeof(a))
#define char2Int(c)		(c-'0')
#define int2String(i, str)	ostringstream temp; temp<<i; str = temp.str()
#define string2Int(i, str) 	stringstream(str) >> i

template<class T> T abs(T x) { return x > 0 ? x : -x; }
long double eps = 1e-15;

bool equalArray(int A[], int B[]){
	return equal((A), (A + sizeof A/ sizeof *A), (B));
}

int* readSingleArray(int m){
	int* arr1D;
	arr1D = new int[m];

	FR(i, 0, m){
		s(k);
		arr1D[i] = k;
	}
	FR(i, 0, m){
		p(arr1D[i]);cout<<" ";
	}cout<<endl;
	return arr1D;
}

int** readDoubleArray(int m, int n){
	int** arr2D;
	arr2D = new int*[m];
	FR(i, 0, m){
		arr2D[i] = new int[n];
		FR(j, 0, n){
			s(k);
			arr2D[i][j] = k;
		}
	}
	FR(i, 0, m){
		FR(j, 0, n){
			p(arr2D[i][j]);cout<<" ";
		}cout<<endl;
	}
	return arr2D;
}

string solve(string S){

//	cout<<S<<endl;
	int res[10] = {};
	string rest = "";

	int letters[26] = {};

	FR(i, 0, S.size()){
		int a = S[i];
		letters[a-65]++;
	}

//	FR(i, 0, 26)cout<<letters[i]<<" ";
//	cout<<endl;

	if(letters[25] > 0){
		int temp = letters[25];
		while(temp--){
			letters[25]--;letters[4]--;letters[17]--;letters[14]--;
			res[0]++;
		}
	}
	if(letters[22] > 0){
		int temp = letters[22];
		while(temp--){
			letters[19]--;letters[22]--;letters[14]--;
			res[2]++;
		}
	}
	if(letters[20] > 0){
		int temp = letters[20];
		while(temp--){
			letters[5]--;letters[14]--;letters[20]--;letters[17]--;
			res[4]++;
		}
	}
	if(letters[23] > 0){
		int temp = letters[23];
		while(temp--){
			letters[18]--;letters[8]--;letters[23]--;
			res[6]++;
		}
	}
	if(letters[6] > 0){
		int temp = letters[6];
		while(temp--){
			letters[4]--;letters[8]--;letters[6]--;letters[7]--;letters[19]--;
			res[8]++;
		}
	}

	if(letters[14] > 0){
		int temp = letters[14];
		while(temp--){
			letters[14]--;letters[13]--;letters[4]--;
			res[1]++;
		}
	}
	if(letters[17] > 0){
		int temp = letters[17];
		while(temp--){
			//letters[]--;letters[22]--;letters[14]--;
			res[3]++;
		}
	}
	if(letters[5] > 0){
		int temp = letters[5];
		while(temp--){
			letters[5]--;letters[8]--;letters[21]--;letters[4]--;
			res[5]++;
		}
	}
	if(letters[18] > 0){
		int temp = letters[18];
		while(temp--){
			//letters[18]--;letters[8]--;letters[23]--;
			res[7]++;
		}
	}
	if(letters[8] > 0){
		int temp = letters[8];
		while(temp--){
			//letters[4]--;letters[8]--;letters[6]--;letters[7]--;letters[19];
			res[9]++;
		}
	}

//	FR(i, 0, S.size()){
//		if(S[i] == 'Z') res += "0";
//		else if(S[i] == 'W') res += "2";
//		else if(S[i] == 'U') res += "4";
//		else if(S[i] == 'X') res += "6";
//		else if(S[i] == 'G') res += "8";
//		else rest += S[i];
//	}
//
//	FR(i, 0, rest.size()){
//		if(S[i] == 'O') res += "";
//		else if(S[i] == 'W') res += "2";
//		else if(S[i] == 'U') res += "4";
//		else if(S[i] == 'X') res += "6";
//		else if(S[i] == 'G') res += "8";
//		else rest += S[i];
//	}

	FR(i, 0, 10){
		int tempt = res[i];
		while(tempt--){
			ostringstream temp; temp<<i;
			rest += temp.str();
		}
	}

	return rest;
}

int main(){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	s(T);
	int r = T;
	while(T--){
		string S;
		cin >> S;


		ps("Case #");p(r-T);ps(": ");cout<<solve(S)<<endl;
//		fprintf (stderr, "%d / %d = %.2f | %.2f\n", r-T, r, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / r-T * r) / CLOCKS_PER_SEC);
	}
//	fclose(stdin);
//	fclose(stdout);

	return 0;
}




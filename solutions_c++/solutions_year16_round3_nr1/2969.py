/*
 * new_template.cpp
 *
 *  Created on: Apr 18, 2016
 *      Author: Nizam
 */


#include <bits/stdc++.h> // Contains all useful header files

using namespace std;

// Data types
#define ll 				long long			// 9,223,372,036,854,775,807
#define llu 			long long unsigned 	// 18,446,744,073,709,551,615
#define ui				unsigned int		// 4,294,967,295
#define ld				long double			// 1.7E +/- 308 (15 digits)
// Input macros
#define s(n) 			int (n); scanf("%d", &n)
#define sc(n) 			char (n); scanf("%c", &n)
#define sl(n) 			llu (n); scanf("%I64d", &n)
#define sf(n) 			double (n); scanf("%lf", &n)
#define sss(n) 			string (n); cin >> n
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
#define MOD 			1000000007
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
#define ARRAY_SIZE(A) 	sizeof(A)/sizeof(A[0])
// For map, pair
#define mp				make_pair
#define fi				first
#define se	 			second
// For vectors
#define pb				push_back
typedef vector<int>		vi;
typedef vector<vi>		vii;
typedef pair<int, int>	ii;
typedef pair<string, string> pss;
// Some common useful functions
#define maX(a, b) 		((a) > (b) ? (a) : (b))
#define miN(a, b) 		((a) < (b) ? (a) : (b))
#define RESET(a, x)		memset(a, x, sizeof(a))
#define char2Int(c)		(c-'0')
#define int2String(i, str)	ostringstream temp; temp<<i; str = temp.str()
#define string2Int(i, str) 	stringstream(str) >> i

#define TRACE(x) 		cout<< #x << " = " << x << endl

template<class T> T abs(T x) { return x > 0 ? x : -x; }
bool isEqualPrec(double a, double b){ return (a > b) ? (a-b < EPS) : (b-a < EPS); }

int indexOfChar(char c){ return c - '0' - 49; }
char incrChar(char c, int p){ return c - 48 + p + '0'; }

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
//	FR(i, 0, m){
//		p(arr1D[i]);cout<<" ";
//	}cout<<endl;
	return arr1D;
}

void solve(int N, int* arr1D){

	vector<int> temp (arr1D, arr1D+N);
	sort(temp.begin(), temp.end(), greater<int>());

//	cout<<temp[0]<<" "<<temp[1]<<endl;
//	cout<<arr1D[0]<<" "<<arr1D[1]<<endl;

	if(temp[0] == temp[1]){
		vector<int> vec;
		FR(i, 0, N){
			if(arr1D[i] != temp[0] || vec.size() == 2){
				FR(j, 0, arr1D[i]) cout<<char(i+65)<<" ";
			}
			else{
				vec.pb(i);
//				cout<<vec[i]<<endl;
			}
		}
		FR(i, 0, temp[0]){
			cout<<char(vec[0]+65)<<char(vec[1]+65)<<" ";
		}
	}
	else if(temp[1] == temp[2]){
//		cout<<"HI "<<endl;
		vector<int> vec;
		FR(i, 0, N){
			if(arr1D[i] != temp[1] || vec.size() == 2){
				FR(j, 0, arr1D[i]) cout<<char(i+65)<<" ";
			}
			else vec.pb(i);
		}
		FR(i, 0, temp[1]){
			cout<<char(vec[0]+65)<<char(vec[1]+65)<<" ";
		}
	}
	else{
		int highest = 0, iter = temp[0];
		FR(i, 0, N) if(arr1D[i] == temp[0]){ highest = i; break;}
		FR(i, 0, temp[0]){
			cout<<char(highest+65)<<" ";
			iter--; arr1D[highest]--;
			if(temp[1] == iter) break;
		}
		vector<int> vec;
		FR(i, 0, N){
			if(arr1D[i] != temp[1] || vec.size() == 2){
				FR(j, 0, arr1D[i]) cout<<char(i+65)<<" ";
			}
			else vec.pb(i);
		}
		FR(i, 0, temp[1]){
			cout<<char(vec[0]+65)<<char(vec[1]+65)<<" ";
		}
	}

}

int main(){
	freopen ("A-small-attempt1.in", "r", stdin);
	freopen ("A-small-attempt1.out", "w", stdout);
	s(T);
	int r = T;
	while(T--){
		sl(N);
		int* arr1D = readSingleArray(N);

		ps("Case #");p(r-T);ps(": ");solve(N, arr1D);cout<<endl;
//		fprintf (stderr, "%d / %d = %.2f | %.2f\n", r-T, r, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / r-T * r) / CLOCKS_PER_SEC);
	}
//	fclose(stdin);
//	fclose(stdout);

	return 0;
}





/*
 * third.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Nizam
 */

#include <bits/stdc++.h> // Contains all useful header files

using namespace std;

// Data types
#define ll 				long long
#define llu 			long long unsigned
#define ui				unsigned int
// Input macros
#define s(n) 			int (n); scanf("%d", &n)
#define sc(n) 			char (n); scanf("%c", &n)
#define sl(n) 			llu (n); scanf("%I64d", &n)
#define sf(n) 			double (n); scanf("%lf", &n)
#define ss(n) 			char tmp[102]; scanf("%101s", tmp); string n=tmp
// Output macros
#define p(n)			printf("%d", n)
#define pn(n)			printf("%d\n", n)
#define pl(n)			printf("%I64d ", n)
#define pln(n)			printf("%I64d\n", n)
#define pf(n)			printf("%f ", n)
#define pfn(n)			printf("%f\n", n)
#define ps(n)			cout<<n;
#define psn(n)			printf("%s\n", n)
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
//#define pb				push_back
typedef vector<int>		vi;
typedef vector<vi>		vii;
typedef pair<int, int>	ii;
// Some common useful functions
#define maX(a, b) 		((a) > (b) ? (a) : (b))
#define miN(a, b) 		((a) < (b) ? (a) : (b))
#define RESET(a, x)		memset(a, x, sizeof(a))
#define char2Int(c)		(c-'0')

int main(){
	freopen ("C-large.in", "r", stdin);
	freopen ("C-large.out", "w", stdout);
	s(T);
	int r = T;
	while(T--){
		s(N); s(J);
		// Highest possible number
		llu highest = 0;
		// Lowest possible number
		//llu lowest = 0;
		vector<vector<llu> > preProcessed;//(9, vector<llu>(N, 0));
		FR(i, 2, 11){
			vector<llu> temp;
			FR(j, 0, N){
				temp.push_back((llu)round(pow(i, j)));
				//cout<<temp[j]<<endl;
				if(i == 10) highest += temp[j];
				//if(i == 10 && j == 15) lowest = temp[j]+1;
			}
			preProcessed.push_back(temp);
		}

		int iter = 0;
		vector<bitset<32> > jamCoin;
		vector<vector<int> > possibleNonTriDivGlob;

		// The starting pattern of jam coin
		bitset<32> a(string("10000000000000000000000000000001"));
		bitset<32> b(string("10"));
		bitset<32> result;

		while(iter < J){
			// Increment by 2 preserving the LSB is always 1
			bool carry = false;
			FR(k, 0, result.size()){
				bool sum = (a[k] ^ b[k] ^ carry);
				carry = (a[k] && b[k]) || (a[k] && carry) || (b[k] && carry);
				result[k] = sum;
			}
			a = result;

			bool primeGlobal = false;
			vector<int> possibleNonTriDiv;

			FR(ii, 2, 11){
				llu num = 0;
				FR(jj, 0, N-1){		// N-1 because, to avoid Nth calculation being added
					num += preProcessed[ii-2][jj]*a[jj];
				}
				//cout<<ii<<": "<<num<<endl;

				// Test whether the number is a prime
				llu primeNumber = num, testNumber = 1, testResult = 0;//pn(primeNumber);
				bool prime = true;
				if(N < 18){
					while(prime && testNumber <= sqrt(primeNumber)){
						testNumber++;
						testResult = primeNumber % testNumber;
						if(testResult == 0){
							//cout<<testNumber<<endl;
							prime = false;
						}
					}
				}
				else {

					llu limit = (llu)round(pow(ii, N/2));
					//cout<<"Limit is: "<<limit<<endl;
//					llu testResultShow1, testResultShow2, testResultShow3, testResultShow4, testResultShow5, testResultShow6;
					while(prime && testNumber <= 1000){
						testNumber++;
						testResult = primeNumber % testNumber;
//						testResultShow1 = testResult;
						//cout<<"1 "<<testResult<<" and "<<testNumber<<endl;
						// Testing for the MSD's value
						llu tempTestResult = 1;
						FR(kk, 0, 5){
							tempTestResult = (tempTestResult * ((llu)round(pow(ii, pow(2, kk))) % testNumber)) % testNumber;
							//cout<<"2 "<<testResult<<" and "<<testNumber<<endl;

						}
						testResult = (testResult + tempTestResult) % testNumber;
						if(testResult == 0){
							//cout<<testNumber<<endl;
							prime = false;
						}
					}

				}
				if(prime){
					primeGlobal = true;
					break;
				}
				else {
					possibleNonTriDiv.push_back(testNumber);
				}
			}

			if(!primeGlobal){
				jamCoin.push_back(a);
				possibleNonTriDivGlob.push_back(possibleNonTriDiv);
				iter++;
			}
		}

		ps("Case #");p(r-T);ps(": ");ps("\n");
		FR(l, 0, J){
			cout<<(jamCoin[l])<<" ";
			FR(kk, 0, 9){ p(possibleNonTriDivGlob[l][kk]); ps(" ");}
			ps("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}



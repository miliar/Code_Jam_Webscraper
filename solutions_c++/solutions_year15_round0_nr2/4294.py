#include <iostream>
#include <cstdio>
#include <cmath>
#include <limits>
/*
#include <vector>
#include <string>
#include <complex>
#include <algorithm>
#include <iterator>
*/
using namespace std;

/*****************************************************
* Configurations
* Problem Category: A, B or C
* Problem Size: "small" or "large"
* Is it a practice problem: true or false
******************************************************/
#define PROB_CAT "B"
#define PROB_SIZE "large"
#define PROB_PRACTICE false

// Shorthands
#define push push_back
#define all(V) V.begin(),V.end()
#define rall(V) V.rbegin(),V.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define repStep(i,m,s) for(int i=0;i<(int)(m);i=i+s)
#define repInit(i,n,m) for(int i=n;i<(int)(m);i++)
#define repInitStep(i,n,m,s) for(int i=n;i<(int)(m);i=i+s)
#define repCond(i,c) for(int i=0;c;i++)
#define repCondStep(i,c,s) for(int i=0;c;i=i+s)
#define repInitCond(i,n,c) for(int i=n;c;i++)
#define repInitCondStep(i,n,c,s) for(int i=n;c;i=i+s)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(V) ((V)/length(V))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
#define printVect(V) std::copy(V.begin(), V.end(), std::ostream_iterator<string>(std::cout, " "))

#if PROB_PRACTICE == true
#define FILE_SUFFIX "-practice"
#else
#define FILE_SUFFIX ""
#endif
#define INFILE PROB_CAT "-" PROB_SIZE FILE_SUFFIX ".in"
#define OUTFILE PROB_CAT "-" PROB_SIZE FILE_SUFFIX ".out"
/*
typedef std::istringstream InStream;
typedef std::ostringstream OutStream;
typedef std::pair<int, int> PairIntInt;
typedef std::vector<PairIntInt> VectPairIntInt;
typedef std::vector<string> VectStr;
typedef std::vector<int> VectInt;
typedef std::vector<double> VectDbl;
typedef std::vector<vector<int> > VectVectI;
typedef long long LongLong;
typedef long double LongDbl;
typedef std::complex<double> Point;
typedef std::pair<Point, Point> Segment;
typedef std::pair<double, Point> Circle;
typedef std::vector<Point> Polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;
*/
int main() {
	// Standard variables
	int caseCount;			// Number of test cases
	//string txtline, word;	// Single line of text and its each word read from input file
	const std::string infile = INFILE;
	const std::string outfile = OUTFILE;
	
	if (std::freopen(infile.c_str(), "rt", stdin) == NULL) {
		printf("Error occurred while opening input file: %s\n", INFILE);
		return -1;
	}
	if (std::freopen(outfile.c_str(), "wt", stdout) == NULL) {
		printf("Error occurred while opening output file: %s\n", OUTFILE);
		fclose(stdin);
		return -1;
	}
	
	/************ Solution starts from here ***************/	
	// Program variables
	int arrSize, maxP, seriesMax;
	int finalMins, currMins, attempt, result;
	int threshold = 3;
	int allowedAttempts = 5;	// may increase later in program
	long int sumP;
	int seriesMaxCounter;
	
	// Get number of test cases
	std::cin >> caseCount;	// DO NOT CHANGE
	//std::getline(cin, txtline);
	// Get data for each test case
	repInit(caseIdx, 1, caseCount + 1) {
		std::cout << "Case #" << caseIdx << ": ";	// DO NOT CHANGE
		maxP = 0;
		sumP = 0;
		result = std::numeric_limits<int>::max();
		// Do input for each case
		cin >> arrSize;
		int P[arrSize];
		rep(i, arrSize) {
			cin >> P[i];
			sumP += P[i];
			if (P[i] > maxP) {
				maxP = P[i];
			}
		}
		
		// Processing here...
		attempt = 1;
		seriesMaxCounter = 1;
		while(attempt <= allowedAttempts) { 
			finalMins = 0;
			if (attempt == 1) {				
				if (maxP > threshold) {
					seriesMax = (int) ceil(sqrt(maxP));
				} else {
					seriesMax = maxP;
				}
			} else if (attempt == 2) {
				if (maxP & 1 == 1) {
					// Odd
					seriesMax = ((int) maxP >> 1) + 1;
				} else {
					// Even
					seriesMax = ((int) maxP >> 1);
				}
			} else if (attempt == 3) {
				seriesMax = (int) ceil(sqrt(sumP));
			} else if (attempt == 4) {
				seriesMax = maxP;
			} else if (attempt > 4) {
				seriesMax = threshold + seriesMaxCounter++;
				if (seriesMax < maxP) {
					allowedAttempts++;
				}
			}
			//cout << "seriesMax = " << seriesMax << endl;			// DEBUG
			rep(i, arrSize) {
				currMins = 0;
				if (P[i] > seriesMax) {
					currMins = round((P[i] - 1) / seriesMax);
				}
				//cout << "special minutes = " << currMins << endl;	// DEBUG
				finalMins += currMins;
			}
			finalMins += seriesMax;
			//cout << "Minutes took: " << finalMins << endl;			// DEBUG
			attempt++;
			if (finalMins <= maxP && finalMins < result) {
				result = finalMins;
			}
		}
		cout << result;
		
		// DO NOT CHANGE endline code
		if (caseIdx < caseCount) {
			cout << endl;
		}
	}
	
	// Close in & out streams
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}

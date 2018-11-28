/**
 * Author: Saurabh Sharma (saurabh257@gmail.com)
 */

#include <iostream>
#include <cstdio>

#include <vector>
#include <tuple>
#include <string>
#include <complex>
#include <algorithm>
#include <iterator>

using namespace std;

/*****************************************************
* Configurations
* PROB_CAT: A, B or C
* PROB_SIZE: "small" or "large"
* PROB_PRACTICE: Is it a practice problem: true or false
* PROB_ATTEMPT: Is it an numbered (_NUM: 0, 1, ...) attempt to solve the problem: true or false
******************************************************/
#define PROB_CAT "B"
#define PROB_SIZE "large"
#define PROB_PRACTICE false
#define PROB_ATTEMPT false
#define PROB_ATTEMPT_NUM "0"

// Shorthands
#define first 0
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
#define printVectInt(V) std::copy(V.begin(), V.end(), std::ostream_iterator<int>(std::cout, " "))
#define printVectStr(V) std::copy(V.begin(), V.end(), std::ostream_iterator<string>(std::cout, " "))

#if PROB_PRACTICE == true
#define FILE_SUFFIX "-practice"
#elif PROB_ATTEMPT == true
#define FILE_SUFFIX "-attempt" PROB_ATTEMPT_NUM
#else
#define FILE_SUFFIX ""
#endif
#define INFILE PROB_CAT "-" PROB_SIZE FILE_SUFFIX ".in"
#define OUTFILE PROB_CAT "-" PROB_SIZE FILE_SUFFIX ".out"

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

int main() {
	// Standard variables
	int caseCount;			// Number of test cases
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
	string txtLine;
	int inputSize;
	bool allHappyFace;
	int flipSize;
	int result;
	char flipFace;
	char happyFace = '+';
	char plainFace = '-';
	
	// Get number of test cases
	std::cin >> caseCount;	// DO NOT CHANGE
	
	// Get data for each test case
	repInit(caseIdx, 1, caseCount + 1) {
		std::cout << "Case #" << caseIdx << ": ";	// DO NOT CHANGE
		// Do input for each case
		cin >> txtLine;		
		
		// Processing here...
		result = 0;
		inputSize = txtLine.size();
		if (inputSize == 1 && txtLine[first] == plainFace) {
			result = 1;
		} else {
			do {
				flipSize = 0;
				allHappyFace = false;
				// Get flip size and check if all have happy face
				repInit(idxCurrent, 1, inputSize) {
					if (txtLine[idxCurrent] != txtLine[first]) {
						flipSize = idxCurrent;
						flipFace = txtLine[idxCurrent];
						break;
					}
				}
				// Flip
				if (flipSize > 0) {
					repInit(idxCurrent, 0, flipSize)
						txtLine[idxCurrent] = flipFace;
					result++;
				} else {
					// No need of flip so all should have same face
					if (txtLine[first] == happyFace) {
						allHappyFace = true;
					} else {
						// All have plain face so just 1 more flip is required to make all happy face
						result++;
						allHappyFace = true;
					}
				}
			} while(!allHappyFace);
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

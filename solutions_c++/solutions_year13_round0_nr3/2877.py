// Code Jam 2013 qualifier
// Problem C
// Author: intrepid
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <iterator>
using namespace std;

// I will use the GNU Multiple Precision Arithmentic Library for large integers
// It is freely attainable at ftp://ftp.gmplib.org/pub/gmp-5.1.1/gmp-5.1.1.tar.lz
// More info at: http://gmplib.org/
#include <gmpxx.h>

template <class InputIterator>
bool is_palindrome(InputIterator begin, InputIterator end)
{
	bool returnValue = true;
	--end;
	while ( distance(begin,end) > 0 ) {
		if ( *begin != *end ) returnValue = false;
		++begin;
		--end;
	}
	
	return returnValue;
}

struct v_base10_t {
	vector<int> v;
	size_t digits;
};

class RunState {
public:
	RunState(v_base10_t& v_cur, v_base10_t& v_max, mpz_class& bigBuffer) :
		v_cur(v_cur),
		v_max(v_max),
		v_matches(),
		n_matches(0),
		checkDigit(0),
		checking(false),
		finished(false),
		bigScratch(bigBuffer),
		numFair(0)
	{
		// Sanity checks
		if ( v_cur.digits <= 0 || v_max.digits <= 0 ) throw std::logic_error("Non-positive digits!\n");
	}
	
	// Returns false if there are no possible square and fair nums
	bool initialize()
	{
		if ( v_cur.digits > v_max.digits ) {
			return false;
		}
		
		setupMatches();
		
		if ( v_cur.digits == v_max.digits ) {
			beginChecking();
			if ( finished ) return true;
			checkLimits();
			return !finished;
		}
		else return true;
	}
	
	void increment()
	{
		int curDigit = 0;
		while( ++v_cur.v[curDigit] > 9 && curDigit < v_cur.digits - 1) {
			v_cur.v[curDigit] = 0;
			// Check for match.
			checkDigitMatch(curDigit);
			++curDigit;
		}
		
		// Overflow
		if ( v_cur.v[curDigit] > 9 ) {
			v_cur.v[curDigit] = 0;
			v_cur.v.push_back(1);
			v_cur.digits = v_cur.v.size();
			if ( v_cur.digits == v_max.digits ) beginChecking();
			
			// Must reset matches
			setupMatches();
			
			// No harm here.
			checkLimits();
		}
		else {
			checkDigitMatch(curDigit);
		}
		
		// Hit check digit?
		if ( curDigit == checkDigit ) checkFinished();
	}
	
	void checkSquareAndFair()
	{
		if ( isPalindrome() && isSquarePalindrome() ) ++numFair;
	}
	
	bool isSquarePalindrome() const
	{
		bigScratch.set_str(toString(), 10);
		bigScratch *= bigScratch;
		std::string scratchString = bigScratch.get_str(10);
		return is_palindrome(scratchString.begin(), scratchString.end());
	}
	
	bool isPalindrome () const
	{
		return ((size_t)n_matches == v_cur.digits);
	}
	
	bool isFinished () const
	{
		return finished;
	}
	
	std::string toString() const
	{
		std::string returnValue;
		returnValue.reserve(v_cur.digits);
		for_each(v_cur.v.rbegin(), v_cur.v.rend(), [&returnValue] (const int& c) {
			returnValue.push_back((char) c + '0');
		});
		return returnValue;
	}
	
	size_t numSquareFair() const { return numFair; }
	
private:
	void beginChecking()
	{
		checking = true;
		checkDigit = v_max.digits - 1;
		checkFinished();
	}
	
	void checkFinished()
	{
		if ( checking ) {
			while ( v_cur.v[checkDigit] == v_max.v[checkDigit] && checkDigit >= 0 ) --checkDigit;
			if ( checkDigit == -1 ) finished = true;
		}
	}
	
	// Must be callled after checkFinished()
	void checkLimits()
	{
		if ( checking && v_cur.v[checkDigit] > v_max.v[checkDigit] ) finished = true;
	}
	
	void setupMatches()
	{
		v_matches.resize(v_cur.digits / 2);
		v_matches.clear();
		n_matches = v_cur.digits % 2;
		
		for (size_t curDigit = 0; curDigit < v_cur.digits / 2; ++curDigit) {
			if ( v_cur.v[curDigit] == v_cur.v[v_cur.digits - curDigit - 1] ) {
				v_matches[curDigit] = 1;
				n_matches += 2;
			}
		}
	}
	
	void checkDigitMatch(int digit)
	{
		// Check for match.
		if ( digit < v_cur.digits / 2 ) {
			if ( v_cur.v[digit] == v_cur.v[v_cur.digits - digit - 1] ) {
				// Mathches!
				v_matches[digit] = 1;
				n_matches += 2;
			}
			else {
				// Does not match.
				if ( v_matches[digit] ) {
					v_matches[digit] = 0;
					n_matches -= 2;
				}
			}
		}
	}
	
    v_base10_t& v_cur;
	v_base10_t& v_max;
	vector<int> v_matches;
	int n_matches;
	int checkDigit;   // The first digit that does not match
	bool checking;       // Are we checking yet?
	bool finished;       // We have incremented beyond range;
	
	mpz_class& bigScratch;
	
	size_t numFair;      // Number of square and fair
};

int main()
{
	size_t numRuns;
	cin >> numRuns;
	if ( !cin.good() ) {
		cerr << "Error reading numRuns!\n";
		return 1;
	}
	cerr << "Processing " << numRuns << " runs.\n";
	
	string strLowLimit, strHighLimit;
	mpz_class big_limit, big_root;
	v_base10_t v_cur, v_max;
	
	for (int i=0; i < numRuns; ++i) {
		cerr << "On run " << i + 1 << endl;
		cin >> strLowLimit >> strHighLimit;
		if ( !cin.good() ) {
			cerr << "Error reading limits for run #" << i + 1 << ".\n";
			return 1;
		}
		
		// Calculate lower sqrt limit
		big_limit.set_str(strLowLimit,10);
		if ( !mpz_root(big_root.get_mpz_t(), big_limit.get_mpz_t(), 2) ) ++big_root;
		string strLowRoot = big_root.get_str(10);
		v_cur.v.clear();
		for_each(strLowRoot.rbegin(), strLowRoot.rend(), [&v_cur] (const char& c) {v_cur.v.push_back(c - '0');});
		v_cur.digits = v_cur.v.size();
		
		// Calculate higher sqrt limit
		big_limit.set_str(strHighLimit,10);
		mpz_root(big_root.get_mpz_t(), big_limit.get_mpz_t(), 2);
		string strHighRoot = big_root.get_str(10);
		v_max.v.clear();
		for_each(strHighRoot.rbegin(), strHighRoot.rend(), [&v_max] (const char& c) {v_max.v.push_back(c - '0');});
		v_max.digits = v_max.v.size();
		
		// Dump them to screen
#if !defined(NDEBUG)
		cerr << strLowLimit << ' ' << strHighLimit << ' ';
		copy(v_cur.v.rbegin(), v_cur.v.rend(), ostream_iterator<int>(cerr,""));
		cerr << ' ';
		copy(v_max.v.rbegin(), v_max.v.rend(), ostream_iterator<int>(cerr,""));
		cerr << '\n';
#endif
		// Digits
#if !defined(NDEBUG)
		cerr << v_cur.digits << ' ' << v_max.digits << '\n';
#endif

		// Run output starts here!
		cout << "Case #" << i + 1 << ": ";
		
		// Initialize run
		RunState state(v_cur, v_max, big_limit);
		
		if ( !state.initialize() ) {
			cout << "0\n";
			continue;
		}
		
		state.checkSquareAndFair();
		while ( !state.isFinished() ) {
			state.increment();
			state.checkSquareAndFair();
		}
		cout << state.numSquareFair() << "\n";
	}
	
	cerr << "Done." << endl;
	
	return 0;
}
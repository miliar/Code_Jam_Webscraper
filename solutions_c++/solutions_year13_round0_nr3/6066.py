/**
 * Problem
 *
 * Little John likes palindromes, and thinks them to be fair (which is
 * a fancy word for nice). A palindrome is just an integer that reads
 * the same backwards and forwards - so 6, 11 and 121 are all
 * palindromes, while 10, 12, 223 and 2244 are not (even though
 * 010=10, we don't consider leading zeroes when determining whether a
 * number is a palindrome). 
 *
 * He recently became interested in squares as well, and formed the
 * definition of a fair and square number - it is a number that is a
 * palindrome and the square of a palindrome at the same time. For
 * instance, 1, 9 and 121 are fair and square (being palindromes and
 * squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are
 * not fair and square: 16 is not a palindrome, 22 is not a square,
 * and while 676 is a palindrome and a square number, it is the square
 * of 26, which is not a palindrome. 
 *
 * Now he wants to search for bigger fair and square numbers. Your
 * task is, given an interval Little John is searching through, to
 * tell him how many fair and square numbers are there in the
 * interval, so he knows when he has found them all. 
 *
 * Solving this problem 
 *
 * Usually, Google Code Jam problems have 1 Small input and 1 Large
 * input. This problem has 1 Small input and 2 Large inputs. Once you
 * have solved the Small input, you will be able to download any of
 * the two Large inputs. As usual, you will be able to retry the Small
 * input (with a time penalty), while you will get only one chance at
 * each of the Large inputs. 
 *
 * Input 
 *
 * The first line of the input gives the number of test cases, T. T
 * lines follow. Each line contains two integers, A and B - the
 * endpoints of the interval Little John is looking at. 
 *
 * Output 
 *
 * For each test case, output one line containing "Case #x: y", where
 * x is the case number (starting from 1) and y is the number of fair
 * and square numbers greater or equal to A and smaller or equal than
 * B. 
 *
 * Limits 
 *
 * Small dataset 
 *
 * 1 ≤ T ≤ 100.
 * 1 ≤ A ≤ B ≤ 1000.
 *
 * First large dataset
 * 
 * 1 ≤ T ≤ 10000.
 * 1 ≤ A ≤ B ≤ 10^14.
 *
 * Second large dataset
 *
 * 1 ≤ T ≤ 1000.
 * 1 ≤ A ≤ B ≤ 10^100.
 *
 * Sample
 * 
 * 
 * Input 
 *	
 * Output 
 *
 * 3
 * 1 4
 * 10 120
 * 100 1000
 * Case #1: 2
 * Case #2: 0
 * Case #3: 2
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned long long ull_t;

vector<ull_t> fsq_10R3;					    // 10-Raise-3
vector<ull_t> fsq_10R14;				    // 10^14
vector<ull_t> fsq_10R100;				    // 10^100

// returns true if 'N' is a palindrome, false otherwise
static bool
is_number_palindrome(unsigned long long N)
{
	unsigned long long x = N;
	unsigned long long y = 0;

	while (x) {
		y = y * 10;
		y = y + x % 10;
		x = x/10;
	}

	return (y == N);
}

/* return's true if 'N' begins with 1/2/3. false otherwise */
static bool
is_number_123(unsigned long long N)
{
	unsigned long long X = N;

	while (N) {
		X = N;
		N = N/10;
	}

	return (X == 1 || X == 2 || X == 3);
}

/*
 * Rationale For The Approach
 * --------------------------
 *
 * we take the simple approach of generating the fair-square-numbers
 * in a range, and then use that to satisfy john's queries.
 * 
 * let us denote a range of numbers, as [A, B], and we want to
 * generate numbers x1, x2, ... xn such that :
 * 
 * 1. A <= (xi * xi) <= B
 *    this implies that x-max cannot be > sqrt(B). thus we generate
 *    number x1, x2, ... , x-max such that x-max == ceil(sqrt(B))
 * 
 * 2. since both xi and xi*xi must be a palindrome, we eliminate those
 *    xi's which are not from the above list. thereby saving the
 *    expense of brute-force-computing of squares, and corresponding
 *    palindrome checking operations.
 * 
 * 3. consider an 'N' digit number with digits
 *    d1,d2,d3,...,dn. with the palindrome rule, it implies that
 *    both d1 and dn must be the one and the same number.
 * 
 *    thus, palindrome will be of the format: 1...1, 2...2, 3...3,
 *    etc, where 1...1 implies a number starting with 1, containing a
 *    bunch of digits, and ending with 1.
 *
 *    ok so, taking a number which begins with say, 7, it must end
 *    with 7 as well. thus, the square of this number must both end
 *    with '9' (7*7 = 49, duh !), and it must begin with '9' as well.
 *
 *    but for a square number to begin with '9' and end with '9', it's
 *    square-root must have initial digit 3 or 9. but
 *    this doesn't hold since the number started with '7'. thus,
 *    implying that we cannot have 'fair-square' number with '7' as
 *    the first numeral.
 * 
 *    in a similar fashion, we realize that we cannot have fair-square
 *    numbers with 4,5,6,7,8,9 as the first numeral. 
 *
 * enough chit-chat, let's get on with it.
 */

/*
 * this function generates a generates fair-square numbers in the
 * range: [1, 10^3]
 */
static void
compute_fsq_in_10R3(void)
{
	unsigned long long xi_max = ceil(sqrt(1000));
	unsigned long long xi = 0;
	unsigned long long xi_sq = 0;

	while (xi < xi_max) {
		if (is_number_palindrome(xi) && is_number_123(xi)) {
			xi_sq = xi * xi;
			if (is_number_palindrome(xi_sq)) {
				fsq_10R3.push_back(xi_sq);
			}
		}

		xi = xi + 1;
	}

	return;
}

static void
debug_dump_fsq(const vector<ull_t> X, bool do_debug)
{
	if (do_debug) {
		ostream_iterator<ull_t> fsq_out(cout, "\n");
		copy(X.begin(), X.end(), fsq_out);
	}
	return;
}

static unsigned long long
num_fair_square_in_range(const vector<ull_t>& fsq,
			 unsigned long long start,
			 unsigned long long end)
{
	vector<ull_t>::iterator sp, ep;

	sp = lower_bound(fsq_10R3.begin(), fsq_10R3.end(), start);
	ep = upper_bound(fsq_10R3.begin(), fsq_10R3.end(), end);

	return (ep - sp);
}

static void
dump_results(int test_case,
	     unsigned long long result)
{
	cout << "Case #" << test_case << ": "
	     << result << endl;
	return;
}

int main(int argc, char **argv)
{
	ifstream ifs(argv[1]);
	int num_tc = 0;
	int A, B = 0;
	string line;
	int result;

	ifs >> num_tc;
	getline(ifs, line);

	/* compute the palindrome-vector */
	compute_fsq_in_10R3();
	debug_dump_fsq(fsq_10R3, false);
	
	for (int i = 0; i < num_tc; i++) {
		ifs >> A >> B;
		result = num_fair_square_in_range(fsq_10R3, A, B);
		dump_results(i+1,			    // test-case
			     result);
	}
	
	return 0;
}

/*
 * Local Variables:
 * compile-command : "g++ fair-and-square.cpp -o obj/fsq"
 * End:
 */

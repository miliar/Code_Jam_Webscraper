
/*
 * Michael V. Antosha
 * Michael.Antosha@gmail.com
 */

#include <iostream>
using std::endl;
using std::fixed;

#include <iomanip>
using std::setprecision;

// #include <set>
// using std::set;

// #include <vector>
// using std::vector;

// #include <algorithm>
// using std::set_intersection;

// clog...
#if defined(MIVAEL_DEBUG)  ||  defined(MIVAEL_CLOG_ENABLED)
using std::clog;
#endif

// assertions...
#if !defined(MIVAEL_DEBUG)  &&  !defined(NDEBUG)
#   define NDEBUG
#endif
#include <cassert>

typedef signed short int int16;
typedef signed int       int32;
typedef signed long int  int64;

typedef double fp_t;

const int MAX_TC = 100;  // max # of test cases

const fp_t START_SPEED = 2.0;

#ifdef TEST_DATASET
const fp_t MAX_FARM_COST = 500.0;
const fp_t MAX_SPEED_STEP = 4.0;
const fp_t MAX_TARGET = 2000.0;
#endif

#ifdef SMALL_DATASET
const fp_t MAX_FARM_COST  =  500.0;
const fp_t MAX_SPEED_STEP =    4.0;
const fp_t MAX_TARGET     = 2000.0;
#endif

#ifdef LARGE_DATASET
const fp_t MAX_FARM_COST  =  10000.0;
const fp_t MAX_SPEED_STEP =    100.0;
const fp_t MAX_TARGET     = 100000.0;
#endif

static inline void check_static_asserts(void)
{
    assert(8 * sizeof(int16) == 16  &&  (int16)-1 < 0);
    assert(8 * sizeof(int32) == 32  &&  (int32)-1 < 0);
    assert(8 * sizeof(int64) == 64  &&  (int64)-1 < 0);
}

int main(void)
{
    check_static_asserts();

    using std::cout;
    using std::cin;

    int T = 0;  cin >> T;  // # of test cases
    // clog << "Number of test cases: " << T << endl;
    assert(1 <= T  &&  T <= MAX_TC);

    for(int test_case = 1;  test_case <= T;  test_case++)
    {
        // clog << "Test case #" << test_case << ":" << endl;

	fp_t C = 0, F = 0, X = 0;  cin >> C >> F >> X;
	assert(1 <= C  &&  C <= MAX_FARM_COST);
	assert(1 <= F  &&  F <= MAX_SPEED_STEP);
	assert(1 <= X  &&  X <= MAX_TARGET);

	const fp_t n = START_SPEED;
	fp_t speed = n;
	fp_t expenses_per_cookie = 0;
	fp_t min_time = X / speed;  // same formula as 'spent_for_target'
	for (fp_t m = 1.0;  true;  m += 1.0)
	{
	    const fp_t prev_speed = speed;
	    speed += F;

	    // additional time per each cookie of farm cost
	    const fp_t cpc = 1.0 / prev_speed;

	    // overall additional time per each cookie of farm cost
	    expenses_per_cookie += cpc;

	    // overall additional time (due to farm building)
	    const fp_t farm_expenses = C * expenses_per_cookie;

	    // time to gain the target (after all farms are built)
	    const fp_t spent_for_target = X / speed;

	    const fp_t overall_time = farm_expenses + spent_for_target;

	    if (overall_time >= min_time)  break;
	    min_time = overall_time;
	}

        // Print the answer to standard output(screen).
        cout << "Case #" << test_case << ": "
	     << fixed << setprecision(7)
	     << min_time << endl;
    }

    return 0;
}

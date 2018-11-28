
/*
 * Michael V. Antosha
 * Michael.Antosha@gmail.com
 */

#include <iostream>
using std::endl;
using std::fixed;

// #include <iomanip>
// using std::setprecision;

#include <set>
using std::set;

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

#ifdef TEST_DATASET
const int MAX_TC = 4;  // max # of test cases
const int MAX_NO_BLOCKS = 9;
#endif

#ifdef SMALL_DATASET
const int MAX_TC = 50;
const int MAX_NO_BLOCKS = 10;
#endif

#ifdef LARGE_DATASET
const int MAX_TC = 50;
const int MAX_NO_BLOCKS = 1000;
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

	int N = 0;  cin >> N;
	assert(1 <= N  &&  N <= MAX_NO_BLOCKS);

	typedef set<fp_t> MassSet;

	MassSet masses_holder[2];
	for (int who = 0;  who < 2;  ++who)
	{
	    MassSet& masses = masses_holder[who];
	    for (int i = 0;  i < N;  ++i)
	    {
		fp_t m = -1;  cin >> m;
		assert(0.0 < m  &&  m < 1.0);
		masses.insert(m);
	    }
	}
	MassSet& naomi = masses_holder[0];
	MassSet& ken   = masses_holder[1];

	MassSet naomi_saved(naomi);
	MassSet ken_saved(ken);

	// deceitful war
	int naomi_dw = 0;  // D.W. result
	while (!naomi.empty())
	{
	    assert(naomi.size() == ken.size());
	    const MassSet::iterator nmin = naomi.begin();
	    const MassSet::iterator kmin = ken.begin();
	    naomi.erase(nmin);  // Naomi always chooses her "minimal" block.
	    if (*nmin > *kmin)
	    {
		// Naomi tells a mass larger than any one Ken has.
		// Ken sacrifies *kmin.
		// Naomi take it with minimal loss of potential.
		ken.erase(kmin);
		++naomi_dw;
	    }
	    else
	    {
		// Naomi tells a mass a little bit less that Ken's
		// maximum mass.
		// Ken puts the block with maximum mass to score a
		// point (and take Naomi's block with maximum loss of
		// potential for him).
		ken.erase(*ken.rbegin());
	    }
	}

	// war
	int naomi_war = 0;
	swap(naomi, naomi_saved);
	swap(ken, ken_saved);
	while (!naomi.empty())
	{
	    assert(naomi.size() == ken.size());
	    const MassSet::iterator nmin = naomi.begin();
	    naomi.erase(nmin);
	    const MassSet::iterator klarger = ken.upper_bound(*nmin);
	    if (klarger != ken.end())
	    {
		ken.erase(klarger);
	    }
	    else
	    {
		ken.erase(ken.begin());
		++naomi_war;
	    }
	}

        // Print the answer to standard output(screen).
        cout << "Case #" << test_case << ": "
	     << naomi_dw << " " << naomi_war << endl;
    }

    return 0;
}

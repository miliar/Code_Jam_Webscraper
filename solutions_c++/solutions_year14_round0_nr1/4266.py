
/*
 * Michael V. Antosha
 * Michael.Antosha@gmail.com
 */

#include <iostream>
using std::endl;

#include <set>
using std::set;

#include <vector>
using std::vector;

#include <algorithm>
using std::set_intersection;

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

// typedef int16 mytype_t;

#ifdef TEST_DATASET
const int MAX_TC = 3;  // max # of test cases
#endif

#ifdef SMALL_DATASET
const int MAX_TC = 100;
#endif

#ifdef LARGE_DATASET
// const int MAX_TC = 1000;
#endif

const int TRY_NUM = 2;
const int DIM = 4;
const int MIN_CARD = 1;
const int MAX_CARD = 16;

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

	typedef int card_t;
	typedef set<card_t> CardSet;

	int rows[TRY_NUM];
	CardSet cards[TRY_NUM];

	for(int q = 0;  q < TRY_NUM;  ++q)
	{
	    int& row = rows[q];
	    row = -1;  cin >> row;  --row;
	    // clog << "Row (try #" << q << "): " << row << endl;
	    assert(0 <= row  &&  row < DIM);

	    for(int y = 0;  y < DIM;  ++y)
		for(int x = 0;  x < DIM;  ++x)
		{
		    card_t card = -1;  cin >> card;
		    assert(MIN_CARD <= card  &&  card <= MAX_CARD);

		    if (y == row)
		    {
			// clog << "cards[" << q << "].insert(" << card << ")" << endl;
			cards[q].insert(card);
		    }
		}
	}

	vector<card_t> narrowed;
	set_intersection(cards[0].begin(), cards[0].end(),
			 cards[1].begin(), cards[1].end(),
			 back_inserter(narrowed));
	const size_t narrsz = narrowed.size();
	assert(/*0 <= narrsz  &&*/  (int)narrsz <= DIM);

        // Print the answer to standard output(screen).
        cout << "Case #" << test_case << ": ";
	if (narrsz == 0)
	    cout << "Volunteer cheated!";
	else if (narrsz == 1)
	    cout << narrowed[0];
	else
	    cout << "Bad magician!";
        cout << endl;
    }

    return 0;
}

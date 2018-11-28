#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAX_NUM = 100000;
const int MAX_DIG = 102;
const int MAX_ALL_1_HALF = 4;

class LargeIntNoCarry
{
public:
	LargeIntNoCarry(void) : len_(0) {}

	LargeIntNoCarry(int len) : len_(len) {}

	void fromString(const char str[])
	{
		len_ = strlen(str);
		strcpy(dig_, str);
		for (int i = 0; i < len_; ++i)
			{
			dig_[i] -= '0';
			}//end for
	}//end fromString

	bool operator<(const LargeIntNoCarry& li) const
	{
		if (len_ < li.len_)
			{
			return true;
			}
		else if(len_ > li.len_)
			{
			return false;
			}//end if

		for (int i = 0; i < len_; ++i)
			{
			if (dig_[i] < li.dig_[i])
				{
				return true;
				}
			else if (dig_[i] > li.dig_[i])
				{
				return false;
				}//end if
			}//end for

		return false;
	}//end operator<

	static int calcFairAndSquare(int dig, LargeIntNoCarry fs[]);

private:
	void expandAndCalcSquare(bool even, LargeIntNoCarry& sqr);

	char dig_[MAX_DIG];
	int len_;
};//end LargeIntNoCarry

int LargeIntNoCarry::calcFairAndSquare(int dig, LargeIntNoCarry fs[])
{
	LargeIntNoCarry li(MAX_DIG);
	int side_dig = dig / 4;
	int len;
	int half_len;
	int core_len;
	int cb, ce;
	int num_1_upper, num_1, num_0;

	fs[0].fromString("1");
	fs[1].fromString("4");
	fs[2].fromString("9");
	fs[3].fromString("121");
	fs[4].fromString("484");
	len = 5;

	for (half_len = 2; half_len <= side_dig; ++half_len)
		{
		// generate palindromes containing only 1 and 0
		li.dig_[0] = 1;
		core_len = half_len - 1;
		cb = 1;
		ce = cb + core_len;
		num_1_upper = std::min(core_len, MAX_ALL_1_HALF - 1);
		for (num_1 = 0; num_1 <= num_1_upper; ++num_1)
			{
			num_0 = std::max(core_len - num_1, 0);
			memset(li.dig_ + cb, 0, num_0);
			memset(li.dig_ + cb + num_0, 1, num_1);
			do	{
				li.len_ = half_len;
				li.expandAndCalcSquare(true, fs[len++]);

				if (half_len < side_dig)
					{
					li.dig_[half_len] = 0; // center is 0
					li.len_ = half_len + 1;
					li.expandAndCalcSquare(false, fs[len++]);

					li.dig_[half_len] = 1; // center is 1
					li.len_ = half_len + 1;
					li.expandAndCalcSquare(false, fs[len++]);
					}//end if
				} while (std::next_permutation(li.dig_ + cb, li.dig_ + ce));
			}//end for
		
		// generate palindromes with the center 2
		li.dig_[0] = 1;
		core_len = half_len - 2;

		cb = 1;
		ce = cb + core_len;
		li.dig_[half_len-1] = 2;
		memset(li.dig_ + cb, 0, core_len);
		// core is all zero
		li.len_ = half_len;
		li.expandAndCalcSquare(false, fs[len++]);
		// core contains a 1
		for (int i = cb; i < ce; ++i)
			{
			li.dig_[i] = 1;
			if (i > cb)
				{
				li.dig_[i-1] = 0;
				}//end if
			li.len_ = half_len;
			li.expandAndCalcSquare(false, fs[len++]);
			}//end for

		// generate palindromes begining with 2
		li.dig_[0] = 2;
		memset(li.dig_ + cb, 0, core_len);

		li.dig_[half_len-1] = 0; // center is 0
		li.len_ = half_len;
		li.expandAndCalcSquare(false, fs[len++]);

		li.dig_[half_len-1] = 1; // center is 1
		li.len_ = half_len;
		li.expandAndCalcSquare(false, fs[len++]);
		}//end for

	return len;
}//end LargeIntNoCarry::calcFairAndSquare


void LargeIntNoCarry::expandAndCalcSquare(bool even, LargeIntNoCarry& sqr)
{
	int le, ri;

	// expand
	if (even)
		{
		le = len_ - 1;
		ri = len_;
		len_ *= 2;
		}
	else{
		le = len_ - 2;
		ri = len_;
		len_ = len_ * 2 - 1;
		}//end if
	do	{
		dig_[ri] = dig_[le];
		--le;
		++ri;
		} while (le >= 0);

	sqr.len_ = len_ * 2 - 1;
	memset(sqr.dig_, 0, sqr.len_);

	// calc square
	// Don't mind the reversed calculation order. It's a palindrome right?
	for (int i = 0; i < len_; ++i)
		{
		for (int j = 0; j < len_; ++j)
			{
			sqr.dig_[i + j] += dig_[i] * dig_[j];
			}//end for
		}//end for
}//end LargeIntNoCarry::expandAndCalcSquare

bool less_than(const LargeIntNoCarry* a, const LargeIntNoCarry* b)
{
	return *a < *b;
}//end less_than

static LargeIntNoCarry *fs_ptr[MAX_NUM];
static LargeIntNoCarry fs[MAX_NUM];
static int fs_len = 0;

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	static char sa[MAX_DIG];
	static char sb[MAX_DIG];
	static LargeIntNoCarry a(MAX_DIG), b(MAX_DIG);
	int t;
	int c;

	fs_len = LargeIntNoCarry::calcFairAndSquare(100, fs);
	for (int i = 0; i < fs_len; ++i)
		{
		fs_ptr[i] = &fs[i];
		}//end for
	std::sort(fs_ptr, fs_ptr + fs_len, less_than);

	scanf("%d", &t);
	for (c = 1; c <= t; ++c)
		{
		scanf("%s%s", sa, sb);
		a.fromString(sa);
		b.fromString(sb);
		printf("Case #%d: %d\n", c, std::upper_bound(fs_ptr, fs_ptr + fs_len, &b, less_than)
									- std::lower_bound(fs_ptr, fs_ptr + fs_len, &a, less_than));
		}//end for
	
	return 0;
}//end main

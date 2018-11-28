//#include <stdio.h>
//#include <assert.h>
//#include <vector>
//#include <deque>
//#include <map>
//
//using std::vector;
//using std::deque;
//using std::map;
//
//unsigned long long reverse(unsigned long long n)
//{
//	unsigned long long ret = 0;
//	for(;n != 0;n /= 10)
//	{
//		ret *= 10;
//		ret += n%10;
//	}
//	return ret;
//}
//
//unsigned long long get_count(unsigned long long n)
//{
//	if(n <= 10) return n;
//	unsigned long long init = 0;
//	if(0 == (n%10)) { --n;++init; }
//	vector<unsigned int> digits;
//	for(unsigned long long i = n;i != 0;i /= 10) digits.push_back(i%10);
//
//	unsigned long long lv = 0,rv = 0;
//	size_t left = 0,right = digits.size()-1;
//	for(;left < right;++left,--right)
//	{
//		lv *= 10;lv += digits[left];
//		rv *= 10;rv += digits[right];
//	}
//	lv = reverse(lv);
//	rv = reverse(rv);
//
//	unsigned long long x = 0;
//	for(size_t i = 1;i < digits.size();++i) { x *= 10;x += 9; }
//	unsigned long long ans = lv - 1 + rv - 1 + 2;
//	if(1 != rv) ans += 1;
//	if(left == right)
//	{
//		unsigned long long y = 1;
//		for(size_t i = 0;i < left;++i) y *= 10;
//		ans += digits[left]*y;
//	}
//	return get_count(x) + ans + init;
//
//	//unsigned long long ans = 1;
//	//for(;;++ans)
//	//{
//	//	for(;1 != (n%10);++ans,--n);
//	//	if(n == 1) break;
//	//	unsigned long long r = reverse(n);
//	//	//printf("%u %I64u\n",i,r);
//	//	if(r >= n) { --n;continue; }
//	//	n = r;
//	//}
//	//return ans;
//	return 0;
//}
//
//int main()
//{
//	unsigned int nCases = 0;scanf("%d",&nCases);
//	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
//	{
//		unsigned long long n = 0;scanf("%I64d",&n);
//		unsigned long long ans = get_count(n);
//		printf("Case #%u: %I64u\n",iCases,ans);
//	}
//
//	//static const unsigned int maxn = 10000000;
//	//vector<unsigned int> values(maxn+1,maxn+10);
//	//values[1] = 1;
//	//deque<unsigned int> que;que.push_back(1);
//	////unsigned int prev = 1;
//	//for(;!que.empty();que.pop_front())
//	//{
//	//	unsigned int u = que.front();
//
//	//	//if(values[u] != prev)
//	//	//{
//	//		//if(prev <= 370) printf("\n");
//	//	//	prev = values[u];
//	//	//}
//	//	//if(prev <= 370) printf("%d ",u);
//
//	//	if(u + 1 <= maxn)
//	//	{
//	//		if(values[u]+1 < values[u+1])
//	//		{
//	//			assert(values[u+1] == maxn+10);
//	//			values[u+1] = values[u]+1;
//	//			que.push_back(u+1);
//	//		}
//	//	}
//	//	unsigned int r = (unsigned int)(reverse(u));
//	//	if(r <= maxn)
//	//	{
//	//		if(values[u]+1 < values[r])
//	//		{
//	//			assert(values[r] == maxn+10);
//	//			values[r] = values[u]+1;
//	//			que.push_back(r);
//	//		}
//	//	}
//	//}
//	//printf("%d\n",values[123456]);
//	//return 0;
//
//	//unsigned int nCases = 0;scanf("%d",&nCases);
//	//for(unsigned int iCases = 1;iCases <= nCases;++iCases)
//	//{
//	//	unsigned long long n = 0;scanf("%I64d",&n);
//	//	unsigned long long ans = 0;
//	//	if(n <= maxn) ans = values[n];
//	//	printf("Case #%u: %I64u\n",iCases,ans);
//	//}
//	return 0;
//}

#include <stdio.h>
#include <assert.h>
#include <vector>
#include <string>
#include <algorithm>
using std::vector;
using std::string;

unsigned int slove_small(const vector<string>& board)
{
	enum 
	{
		MASK_NO = 1,
		MASK_UP = 2,
		MASK_RIGHT = 4,
		MASK_DOWN = 8,
		MASK_LEFT = 16,
		MASK_FULL = 31,
	};
	size_t size = board.size(),len = board[0].size();
	vector< vector<unsigned int> > masks(size,vector<unsigned int>(len,MASK_FULL));
	for(size_t i = 0;i < size;++i)
	{
		for(size_t k = 0;k < len;++k)
		{
			if('.' == board[i][k]) masks[i][k] = MASK_NO;
			else masks[i][k] &= ~MASK_NO;
		}
	}
	masks[0][0] &= ~MASK_UP;masks[0][0] &= ~MASK_LEFT;
	masks[0][len-1] &= ~MASK_UP;masks[0][len-1] &= ~MASK_RIGHT;
	masks[size-1][0] &= ~MASK_DOWN;masks[size-1][0] &= ~MASK_LEFT;
	masks[size-1][len-1] &= ~MASK_DOWN;masks[size-1][len-1] &= ~MASK_RIGHT;
	for(size_t i = 0;i < len;++i)
	{
		masks[0][i] &= ~MASK_UP;
		masks[size-1][i] &= ~MASK_DOWN;
	}
	for(size_t i = 0;i < size;++i)
	{
		masks[i][0] &= ~MASK_LEFT;
		masks[i][len-1] &= ~MASK_RIGHT;
	}
	for(size_t i = 0;i < size;++i)
	{
		for(size_t k = 0;k < len;++k)
		{
			if(board[i][k] == '.') continue;
			masks[i][k] &= ~MASK_LEFT;
			break;
		}
	}
	for(size_t i = 0;i < size;++i)
	{
		for(size_t k = len - 1;k != (size_t)(-1);--k)
		{
			if(board[i][k] == '.') continue;
			masks[i][k] &= ~MASK_RIGHT;
			break;
		}
	}
	for(size_t i = 0;i < len;++i)
	{
		for(size_t k = 0;k < size;++k)
		{
			if(board[k][i] == '.') continue;
			masks[k][i] &= ~MASK_UP;
			break;
		}
	}
	for(size_t i = 0;i < len;++i)
	{
		for(size_t k = size - 1;k != (size_t)(-1);--k)
		{
			if(board[k][i] == '.') continue;
			masks[k][i] &= ~MASK_DOWN;
			break;
		}
	}

	vector< vector<unsigned int> > data(size,vector<unsigned int>(len,0));
	for(size_t i = 0;i < size;++i)
	{
		for(size_t k = 0;k < len;++k)
		{
			if('.' == board[i][k]) data[i][k] = MASK_NO;
			else if('^' == board[i][k]) data[i][k] = MASK_UP;
			else if('>' == board[i][k]) data[i][k] = MASK_RIGHT;
			else if('v' == board[i][k]) data[i][k] = MASK_DOWN;
			else if('<' == board[i][k]) data[i][k] = MASK_LEFT;
		}
	}

	unsigned int ans = 0;
	for(size_t i = 0;i < size;++i)
	{
		for(size_t k = 0;k < len;++k)
		{
			if(0 == masks[i][k]) return (unsigned int)(-1);
			if(data[i][k]&masks[i][k]) continue;
			++ ans;
		}
	}

	return ans;
}

int main()
{
	static const size_t buffsize = 110;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int r = 0,c = 0;scanf("%d%d",&r,&c);
		vector<string> board(r);
		char buff[buffsize] = { 0 };
		for(unsigned int i = 0;i < r;++i)
		{
			scanf("%s",buff);
			board[i] = buff;
		}
		unsigned int ans = slove_small(board);
		if((unsigned int)(-1) == ans) printf("Case #%u: IMPOSSIBLE\n",iCases);
		else printf("Case #%u: %u\n",iCases,ans);
	}
	return 0;
}

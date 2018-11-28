#define _SECURE_SCL 0

#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

#ifdef _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
#else// _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
//#define	Assert(E)		do { if (!(E)) { } } while (false)
#endif//_DEBUG

typedef unsigned long DWORD;
typedef unsigned char BYTE;
typedef unsigned __int64 QWORD;

struct Chest
{
	int type;
	vector<int> keys;
};

vector<Chest> chests;
vector<int> keys;
vector<int> result;
char checked[1 << 20];

//--------------------------------------------------------------------------------------------------
bool Check(long chests_mask, int keys_start, int keys_end)
{
	if (chests_mask == 0) return true;

	for(int i = 0; i < (int)chests.size(); ++i)
	{
		long m = 1 << i;
		if (!(chests_mask & m)) continue;

		long new_mask = chests_mask & (~m);
		if (checked[new_mask]) continue;

		int t = chests[i].type;
		int k;
		for(k = keys_start; k < keys_end; ++k)
			if (keys[k] == t)
				break;
		if (k >= keys_end) continue;

		checked[new_mask] = 1;

		for(int j = keys_start; j < k; ++j)
			keys.push_back(keys[j]);
		for(int j = k + 1; j < keys_end; ++j)
			keys.push_back(keys[j]);

		const vector<int> &ckeys = chests[i].keys;
		for(int j = 0; j < (int)ckeys.size(); ++j)
			keys.push_back(ckeys[j]);

		if (Check(new_mask, keys_end, (int)keys.size()))
		{
			result.push_back(i);
			return true;
		}
		keys.resize(keys_end);
	}
	return false;
}

//--------------------------------------------------------------------------------------------------
void ProcessTask(int in_id)
{
	int k, n;
	cin >> k;
	cin >> n;

	long keys_mask = 0;
	keys.resize(k);
	for(int i = 0; i < k; ++i)
	{
		cin >> keys[i];
		keys_mask |= keys[i] << 1;
	}

	chests.resize(n);
	for(int i = 0; i < n; ++i)
	{
		cin >> chests[i].type;
		int ck;
		cin >> ck;
		chests[i].keys.resize(ck);
		for(int j = 0; j < ck; ++j)
			cin >> chests[i].keys[j];
	}

	for(int i = 0; i < (1 << n); ++i)
		checked[i] = 0;

	result.clear();
	Check((1 << n) - 1, 0, (int)keys.size());

	printf("Case #%d:", in_id + 1);
	if (result.empty())
	{
		printf(" IMPOSSIBLE\n");
	}
	else
	{
		for(int i = (int)result.size() - 1; i >= 0; --i)
			printf(" %d", result[i] + 1);
		printf("\n");
	}
}


//--------------------------------------------------------------------------------------------------
int main()
{
	int numb;
	cin >> numb;

	for(int i = 0; i < numb; ++i)
	{
		ProcessTask(i);
	}

	return 0;
}

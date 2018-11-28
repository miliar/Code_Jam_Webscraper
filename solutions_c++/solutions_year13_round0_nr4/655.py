#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <list>
#include <stack>
#include <algorithm>
#include <queue>
#include <map>
#include <cstdlib>
#include <set>
#include <string>
#include <cstring>
#include <memory>
using namespace std;

//ofstream fout("C:\\Users\\Administrator\\Desktop\\C.out");
#define fout cout

class D
{
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();
	int DP(int remain);

private:
	const static int MAX_KEY_NUM = 200;
	const static int MAX_CHEST_NUM = 20;
	int caseNum, caseIndex;
	int keyNum, chestNum;
	int initialKeys[MAX_KEY_NUM];
	int chestType[MAX_CHEST_NUM];
	int chestKeyNum[MAX_CHEST_NUM];
	int chestKeys[MAX_CHEST_NUM][MAX_KEY_NUM];
	int DPBuffer[1 << MAX_CHEST_NUM];
	int route[MAX_CHEST_NUM];
};

void D::Run()
{
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void D::Input()
{
	scanf("%d %d", &keyNum, &chestNum);
	memset(initialKeys, 0, sizeof(initialKeys));
	for(int i = 0; i < keyNum; ++i)
	{
		int key;
		scanf("%d", &key);
		++initialKeys[key - 1];
	}
	memset(chestKeys, 0, sizeof(chestKeys));
	for(int i = 0; i < chestNum; ++i)
	{
		int type, kNum;
		scanf("%d %d", &type, chestKeyNum + i);
		chestType[i] = type - 1;
		for(int j = 0; j < chestKeyNum[i]; ++j)
		{
			int key;
			scanf("%d", &key);
			chestKeys[i][j] = key - 1;
		}
	}
}

void D::Do()
{
	memset(DPBuffer, 0xff, sizeof(DPBuffer));
	if(DP(0) < 0) route[0] = -1;
	else
	{
		int remain = 0;
		for(int i = 0; i < chestNum; ++i)
		{
			route[i] = DP(remain);
			remain ^= 1 << route[i];
			++route[i];
		}
	}
}

int D::DP(int remain)
{
	if(DPBuffer[remain] != -1) return DPBuffer[remain];
	if(remain == (1 << chestNum) - 1) return DPBuffer[remain] = 0;
	for(int i = 0; i < chestNum; ++i) if((remain >> i) % 2 == 0 && initialKeys[chestType[i]])
	{
		--initialKeys[chestType[i]];
		for(int j = 0; j < chestKeyNum[i]; ++j) ++initialKeys[chestKeys[i][j]];
		int opt = DP(remain ^ (1 << i));
		for(int j = 0; j < chestKeyNum[i]; ++j) --initialKeys[chestKeys[i][j]];
		++initialKeys[chestType[i]];

		if(opt >= 0)
			return DPBuffer[remain] = i;
	}
	return DPBuffer[remain] = -2;
}

void D::Output()
{
	fout << "Case #" << caseIndex << ":";
	if(route[0] == -1)
		fout << " IMPOSSIBLE";
	else
		for(int i = 0; i < chestNum; ++i)
			fout << " " << route[i];
	fout << endl;
}

D instance;
int main()
{
	instance.Run();
	return 0;
}

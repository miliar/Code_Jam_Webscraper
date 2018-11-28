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

#pragma comment(linker, "/STACK:104857600,104857600")

using namespace std;

#define FILE_IO

class A
{
private:
	const static int MAX_FILE_NUM = 10000;
	int caseNum, caseIndex;
	int fileNum, cap;
	int fileSize[MAX_FILE_NUM];
	int result;
	
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();
};

void A::Run()
{
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void A::Input()
{
	scanf("%d %d", &fileNum, &cap);
	for(int i = 0; i < fileNum; ++i)
		scanf("%d", fileSize + i);
}

void A::Do()
{
	sort(fileSize, fileSize + fileNum);
	map<int, int> files;
	for(int i = 0; i < fileNum; ++i)
		++files[fileSize[i]]; 
	result = 0;
	for(int i = fileNum - 1; i >= 0; --i)
	{
		int s = fileSize[i];
		if(files.find(s) == files.end()) continue;
		--files[s];
		if(files[s] == 0) files.erase(s);
		map<int, int>::iterator itr = files.lower_bound(cap - s + 1);
		if(itr != files.begin())
		{
			--itr;
			--(itr->second);
			if(itr->second == 0)
				files.erase(itr);
		}
		++result;
	}
}

void A::Output()
{
	printf("Case #%d: %d\n", caseIndex, result);
}

A instance;
int main()
{
	#ifdef FILE_IO
	freopen("C:\\Users\\Administrator\\Desktop\\A.in", "r", stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\A.out", "w", stdout);
	#endif

	instance.Run();
	return 0;
}

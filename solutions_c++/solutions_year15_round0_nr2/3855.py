#include <bits/stdc++.h>

using namespace std;

#define forless(i, s, e) for(int i = s; i < e; ++i)
#define forto(i, s, e) for(int i = s; i <= e; ++i)

map<int, int> cMap;

int Min;

void dfs(int t){
	if(t >= Min)	return;
	int Max = -1;
	for(map<int, int>::iterator it = cMap.begin(); it != cMap.end(); ++it){
		if(it->first > Max)	Max = it->first;
	}
	if(Max == -1)	return;
	if(Max + t < Min)	Min = Max + t;
	if(Max > 1){
		if(--cMap[Max] == 0)	cMap.erase(Max);
		forless(i, 1, Max){
			++cMap[i];
			++cMap[Max - i];
			dfs(t + 1);
			if(--cMap[i] == 0)	cMap.erase(i);
			if(--cMap[Max - i] == 0)	cMap.erase(Max - i);
		}
		++cMap[Max];
	}	
}

int main(){
	int T;
	cin >> T;
	forless(t, 0, T){
		int Max = -1;
		cMap.clear();
		int D;
		cin >> D;
		forless(i, 0, D){
			int tmp;
			cin >> tmp;
			++cMap[tmp];
			if(tmp > Max)	Max = tmp;
		}
		Min = Max;
		dfs(0);
		printf("Case #%d: %d\n", t + 1, Min);
	}
}
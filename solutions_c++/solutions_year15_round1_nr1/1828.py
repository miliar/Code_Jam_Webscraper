#include <cstdlib>
#include <set>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <vector>
#include <functional>
#include <algorithm> 
#include <stack>
#include <queue>
#include<map>
using namespace::std;
int N;
const int Max = 10010;
int mi[Max];
int main(){
	freopen("A-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Case;
	cin >> Case;
	for (size_t z = 1; z <= Case; z++)
	{
		cin >> N;
		for (size_t i = 0; i < N; i++)
		{
			cin >> mi[i];
		}
		int Max = 0;
		int sum = 0, res = 0;
		for (size_t i = 1; i < N; i++)
		{
			if (mi[i] < mi[i - 1]){
				sum += abs(mi[i] - mi[i - 1]);
				if (Max < abs(mi[i] - mi[i - 1]))Max = abs(mi[i] - mi[i - 1]);
			}
		}
		for (size_t i = 0; i < N - 1; i++)
		{
			if (mi[i] < Max)res += mi[i];
			else res += Max;
		}
		printf("Case #%d: %d %d\n", z, sum, res);
	}
}
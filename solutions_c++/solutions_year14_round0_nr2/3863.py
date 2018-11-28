#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
		
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int N; // test cases
	scanf("%d",&N);
	
	float base_output = 2.0;
			
	for (int i = 0; i < N; i++)
	{
		double C, F, X;
	  cin >> C ;
    cin >> F;
    cin >> X;
		double current_time = 0;
		double current_output = base_output;
		double remaining_time = X / current_output;
		while (C / current_output + X / (current_output + F) < remaining_time)
		{
			current_time += C / current_output;
			current_output += F;
			remaining_time = X / current_output;
		}
		double spent_time = current_time + X / current_output;
		
		cout << "Case #" << i + 1 << ": ";	
		printf("%5.7f\n", spent_time);
	}
	

	return 0;
};


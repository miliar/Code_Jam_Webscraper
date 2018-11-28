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
			
	for (int i = 0; i < N; i++)
	{
		int first_answer, second_answer;
		int first_deck[16];
		int second_deck[16];
	  scanf("%d",&first_answer);
	  for (int j = 0; j < 16; j++)
			scanf("%d",&first_deck[j]);
	  scanf("%d",&second_answer);
	  for (int j = 0; j < 16; j++)
			scanf("%d",&second_deck[j]);
		std::vector<int> v(8);                 
		std::vector<int>::iterator it;
		auto begin_first_row = first_deck + (first_answer - 1) * 4;
		auto end_first_row = first_deck + first_answer * 4;
		auto begin_second_row = second_deck + (second_answer - 1) * 4;
		auto end_second_row = second_deck + second_answer * 4;
		std::sort (begin_first_row, end_first_row);
    std::sort (begin_second_row, end_second_row);
    it = std::set_intersection (begin_first_row, end_first_row, begin_second_row, end_second_row, v.begin());
    int number_elements = it - v.begin();
		cout << "Case #" << i + 1 << ": ";
		if (number_elements == 0)
			cout << "Volunteer cheated!" << endl;
		else if (number_elements > 1)
			cout << "Bad magician!" << endl;
		else cout << v[0] << endl;
	}
	

	return 0;
};


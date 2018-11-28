#include <iostream>
#include <stdio.h>
#include <numeric>
#include <queue>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <iomanip>
#include <set>
#include <queue>
#include <bitset>
#include <iomanip>
#include <map>
#include <string.h>
#include <stack>
#include <algorithm>

#include <unordered_map>
#include <unordered_set>

using namespace std;

struct node
{
	char ch;
	int count;

	node(char ch , int count)
	{
		this -> ch = ch;
		this -> count = count;
	}

	bool operator< (const node& no) const
	{
		if (count < no.count)
			return true;
		else if (count > no.count)
			return false;
		else
		{
			if (ch < no.ch)
				return true;
			else
				return false;
		}
	}
};

priority_queue<node , vector<node> , less<node>> q;
vector<string> output;

int main()
{
//	freopen("E:\\things for work\\google\\A-large.in" , "r" , stdin);
//	freopen("E:\\things for work\\google\\out.txt" , "w" , stdout);

	int i , j , k , t , case_num = 1;
	scanf("%d" , &t);
	while (t --)
	{
		while (q.empty() == false)
			q.pop();

		output.clear();
		int n;
		scanf("%d" , &n);
		for (i = 1;i <= n;i ++)
		{
			int p;
			scanf("%d" , &p);
			// 字符i有p个
			q.push(node((char) ((i - 1) + 'A') , p));
		}

		while (!q.empty())
		{
			node no = q.top();
			q.pop();
			// 如果还有两个
			if (q.size() == 1)
			{
				string s = "";
				s += no.ch;
				s += q.top().ch;
				for (i = 0;i < no.count;i ++)
					output.push_back(s);
				break;
			}
			else
			{
				string s = "";
				s += no.ch;
				no.count --;
				output.push_back(s);

				if (no.count > 0)
					q.push(no);
			}
		}
		printf("Case #%d:" , case_num);
		for (i = 0;i < output.size();i ++)
			cout << " " << output[i];
		cout << endl;

		case_num ++;
	}
	return 0;
}

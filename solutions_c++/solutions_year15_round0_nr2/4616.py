#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int n;
vector <int> num;

int div(vector <int> tmp, int sol)
{
	int i, s = 10, mn = 0;
	for(i = 1; i < (int)tmp.size(); i++)
		if(tmp[i] > tmp[mn])
			mn = i;
	if(tmp[mn] == 3)
		return sol + 3;
	if(tmp[mn] == 2)
		return sol + 2;
	if(tmp[mn] == 1)
		return sol + 1;
	if(tmp[mn] + sol < s)
	{
		//printf("%d %d 5\n", t, sol);
		s = tmp[mn] + sol;
	}
	vector <int> t2 = tmp;
	t2.push_back(t2[mn] / 2);
	t2.push_back((t2[mn] + 1) / 2);	
	t2.erase(t2.begin() + mn);
	int t = div(t2, sol + 1);
	if(t < s)
	{
		//printf("%d %d 7\n", t, sol);
		s = t;
	}
	if(tmp[mn] >= 3)
	{
		vector <int> t3 = tmp;
		t3.push_back(t3[mn] / 3);
		t3.push_back((t3[mn] + 1) / 3);
		t3.push_back((t3[mn] + 2) / 3);		
		t3.erase(t3.begin() + mn);
		t = div(t3, sol + 2);
		if(t < s)
		{
			//printf("%d %d 9\n", t, sol);
			s = t;	
		}
	}
	/*if(tmp[mn] >= 4)
	{
		vector <int> t4 = tmp;
		t4.push_back(t4[mn] / 4);
		t4.push_back((t4[mn] + 1) / 4);
		t4.push_back((t4[mn] + 2) / 4);
		t4.push_back((t4[mn] + 3) / 4);		
		t4.erase(t4.begin() + mn);
		t = div(t4, sol + 3);
		if(t < s)
		{
			//printf("%d %d 2\n", t, sol);
			s = t;
		}
	}*/
	return s;
}

int main()
{
	int k, l;
	scanf("%d", &l);
	for(k = 0; k < l; k++)
	{
		scanf("%d", &n);
		int i;
		for(i = 0; i < n; i++)
		{
			int t;
			scanf("%d", &t);
			num.push_back(t);
		}
		printf("Case #%d: %d\n", k + 1, div(num, 0));
		num.clear();
	}
	return 0;
}

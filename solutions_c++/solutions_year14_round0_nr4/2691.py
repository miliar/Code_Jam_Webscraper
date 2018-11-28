#include<iostream>
#include<string>
#include<memory>
#include<cstring>
#include<set>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int main()
{
	int t,tt;
	cin >> tt;
	double naomi[1000];
	double ken[1000];
	int n;
	for(t = 1; t <= tt; t ++)
	{
		cin >> n;
		int i,j;
		for(i = 0; i < n; i ++)
			cin >> naomi[i];
		for(i = 0; i < n; i ++)
			cin >> ken[i];
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		i = j = n-1;
		int count_a = 0, count_b = 0;
		while(i>=0 && j>=0)
		{
			if(naomi[i] > ken[j])
			{
				count_a++;
				i --;
			}
			j --;
		}
		i = j = n-1;
		while(i>=0 && j>=0)
		{
			if(ken[i] > naomi[j])
			{
				count_b++;
				i --;
			}
			j --;
		}
		cout << "Case #" << t << ": " << count_a << " " << n-count_b << endl;
	}
	return 0;
}
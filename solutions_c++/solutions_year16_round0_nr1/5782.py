
#include<iostream>
#include<vector>
#include<stdio.h>
#include<memory.h>
#include<set>
using namespace std;
int main() {
	
	
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		long long x;
		scanf("%lld", &x);
		
		long long tmp = x;
		set<int>s;
		if (x == 0)
			printf("Case #%d: INSOMNIA\n", i + 1);
		else
		{
			long long lst = tmp;
			int j = 2;
			while (s.size() < 10)
			{
				long long tt = tmp;
				
				while (tt)
				{
					s.insert(tt % 10);
					tt /= 10;
				}
				lst = tmp;
				
				tmp = x* j; 
				++j;
		
			}
			
			printf("Case #%d: %lld\n", i + 1, lst);
		}
	}
}
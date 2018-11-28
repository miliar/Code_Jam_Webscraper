
//#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<stdio.h>
#include<memory.h>
#include<set>
#include<queue>
#include<map>
#include<string>
using namespace std;


int main() {


//	freopen("B-large.in", "r", stdin);
	//freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		string s;
		cin >> s;
		int c = 1;
		char lst = s[0];

		for (int i = 1; i < s.size(); ++i)
		{
			if (lst != s[i])
				++c, lst = s[i];
		}
		if (lst == '+')
			--c;
		
		printf("Case #%d: %d\n", i, c);
	}
}
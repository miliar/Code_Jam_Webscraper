#include <bits/stdc++.h>

using namespace std;

int test;

int main ()
 	{
 		ios :: sync_with_stdio(false);
 		cin.tie(0);

 		cin >> test;
 		int t = test;

 		while (test--)
 		 	{
 		 		cout << "Case #" << t - test << ": ";

 		 		string s;

 		 		cin >> s;
 		 		int n = s.size();

 		 		int res = 0;

 		 		for (int i = 0; i < n; i++)
 		 			{
 		 				if (i && s[i] != s[i-1]) res++;
 		 				if (i == n - 1 && s[i] == '-') res++;
 		 			}

 		 		cout << res << endl;
 		 	}
 		return 0;
 	}

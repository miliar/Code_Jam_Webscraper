#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;
const int maxn = 1005; 
char s[maxn]; 

int main()
{
	int T, I, n, sum = 0, diff, ans; 
	scanf ("%d", &T); 
	for (I=1; I<=T; I++)
	{
		scanf ("%d%s", &n, s); 
		sum = s[0] - '0'; 
		ans = 0; 
		for (int i=1; s[i]; i++)
		{
			if (sum >= i)
				sum += s[i] - '0'; 
			else{
				diff = i - sum; 
				ans += diff; 
				sum += diff + s[i] - '0'; 
			}
		}
		printf ("Case #%d: %d\n", I, ans); 
	}
}
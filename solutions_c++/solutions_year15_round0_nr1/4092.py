#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

void solve(int nCase)
{
	int gn, standing, required, i, n, n2;
	string s;
	
	cin >> gn >> s;

	standing = s[0] - '0';
	required = 0;
	for(i=1; i<s.size(); i++) {
		n = s[i] - '0';
		if(n) {
			if( standing < i) {
				n2 = i - standing;
				required += n2;
				standing += n2;
			}
			standing += n;
		}
	}
	printf("Case #%d: %d\n", nCase, required);

}


int main(int argc, char cargv[])
{
	int n, i;
	// freopen("2015_qr_01.in", "r", stdin);
	
	scanf("%d", &n);
	for(i=0; i<n; i++)
	{
		solve(i+1);
	}
	return 0;
}

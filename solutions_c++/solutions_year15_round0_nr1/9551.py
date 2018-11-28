//A
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
#include <math.h>
#include <cmath>
#include <string>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include <list>
#include <functional>
#include <sstream>
#include <fstream>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */
#include <bitset>
#include <utility>
#include <cctype>
#include <cstring>
#include <cctype>
#include <vector>
#include<valarray>
#include <map>
#include <set>
#include<complex>
#include<iomanip>
#include <numeric>
#include <stdio.h>
#include <stdlib.h>
typedef vector<int> vint;
typedef set<int> sint;
typedef long long ll;
#define sz(v) ((int)((v).size()))
#define all(v) ((v).begin()),((v).end())
#define INT_MAX 2147483647
#define INT_MIN -2147483648
#define pi acos(-1.0)


int main(){

	freopen("in.txt", "r", stdin);
	freopen("out3.txt", "w", stdout);
	int t, Smax, standing = 0, needs, ans = 0;
	char temp;
	scanf("%d",&t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ",i);
		scanf("%d",&Smax);
		cin >> temp;
		standing = (temp - '0');
		for (int j = 1; j < Smax + 1; j++)
		{
			cin >> temp;
			if (j > standing && (temp - '0')){
				ans += j - standing;
				standing += j - standing;
			}

			standing += temp - '0';

		}
		printf("%d\n",ans);
		ans = standing = 0;
	}

	return 0;
}
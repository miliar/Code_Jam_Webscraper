#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

bool vis[10][3][10010];
string x;

int getv(char c){
	if (c == 'i')
		return 1;
	if (c == 'j')
		return 2;
	return 3;
}

int mul[][8]={{0, 1, 2, 3, 4, 5, 6, 7},
			  {1, 4, 3, 6, 5, 0, 7, 2},
			  {2, 7, 4, 1, 6, 3, 0, 5},
			  {3, 2, 5, 4, 7, 6, 1, 0},
			  {4, 5, 6, 7, 0, 1, 2, 3},
			  {5, 0, 7, 2, 1, 4, 3, 6},
			  {6, 3, 0, 5, 2, 7, 4, 1},
			  {7, 6, 1, 0, 3, 2, 5, 4}};

bool can (int v, int t, int ind){
	if (ind == (int)x.size()){
		if (t == 2 && v == 3)
			return true;
		return false;
	}
	if (vis[v][t][ind])
		return false;

	int c = getv(x[ind]);

	//cout << v << " " << t << " " << ind << endl;

	if (can (mul[v][c], t, ind+1))
		return true;

	if (mul[v][c] == 1 && t == 0)
		if (can (0, 1, ind+1))
			return true;
	if (mul[v][c] == 2 && t == 1)
		if (can (0, 2, ind+1))
			return true;

	vis[v][t][ind] = true;
	return false;
}

int main (){

	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t;
	scanf ("%d", &t);


	for (int tc=1;tc<=t;tc++){
		int n, s;
		scanf ("%d %d", &n, &s);
		
		char str[n+5];
		
		scanf ("%s", str);
		string b = str;
		
		x = "";
		for (int i=0;i<s;i++)
			x = x + b;
		
		memset (vis, 0, sizeof(vis));
		printf ("Case #%d: %s\n", tc, can(0, 0, 0)?"YES":"NO");
	}
	return 0;
}

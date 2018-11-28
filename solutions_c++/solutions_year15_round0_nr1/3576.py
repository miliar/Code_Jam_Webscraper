#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <functional>
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
	ifstream fin("input.in");
	ofstream fout("output.out");

	int T; fin >> T;
	for (int Z = 0; Z < T; Z++)
	{
		int n; fin >> n;
		string s; fin >> s;
		n++;
		int standing = s[0] - '0';
		int ans = 0;
		for (int i = 1; i < n; i++)
		{
			if (standing < i){
				ans += i - standing;
				standing = i;
			}
			standing += s[i] - '0';
		}
		fout << "Case #" << Z + 1 << ": " << ans << endl;
	}
	return 0;
}
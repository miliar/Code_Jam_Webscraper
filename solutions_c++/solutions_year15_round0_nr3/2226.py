#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
#include <map>
#include <set>
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int main()
{
	int testcases;
	fin >> testcases;
	for (int testcase = 1; testcase <= testcases; ++testcase)
	{
		int l, ii = -1;
		long long int r = 0;
		string p, c = "1", ans = "NO"; 
		map<string, string> mul;
		mul["ij"] = mul["-ji"] = mul["1k"] = "k";
		mul["-ij"] = mul["ji"] = mul["-1k"] = "-k";
		mul["ki"] = mul["-ik"] = mul["1j"] = "j";
		mul["ik"] = mul["-ki"] = mul["-1j"] = "-j";
		mul["jk"] = mul["-kj"] = mul["1i"] = "i";
		mul["-jk"] = mul["kj"] = mul["-1i"] = "-i";
		mul["-ii"] = mul["-jj"] = mul["-kk"] = "1";
		mul["ii"] = mul["jj"] = mul["kk"] = "-1";
		fin >> l >> r>>p;
		for (int i = 0; i < l; ++i){
			c = mul[c + p[i]];
		}

		ans = "YES";
		if (c == "1") ans = "NO";
		else if (r % 2 == 0){
			if (c == "-1" || r%4 == 0) ans = "NO";
		}
		else{
			if (c != "-1") ans = "NO";
		}

		if(ans == "YES"){
			ans = "NO";
			string sc = "1";
			int r4 = 4;
			bool foundi = false, foundk = false, stop = false;
			for (int j = 0; j < r && j < r4; ++j){
				for (int i = 0; i < l; ++i){
					sc = mul[sc + p[i]];
					if (!foundi && sc == "i"){
						foundi = true;
						r4 = j + 4;
					}
					if (foundi && sc == "k"){
						foundk = true;
						stop = true;
						break;
					}
				}
				if (stop) break;
			}
			if (foundi && foundk) ans = "YES";
		}
		fout << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int level[1001];

int main(){
	int t;
	cin >> t;
	for (int it = 0; it < 1001; ++it)
	{
		level[it] = it;
	}
	for (int i = 0; i < t; ++i)
	{
		int smax,min = 0,available=0;
		cin >> smax;
		string shyness = "";
		cin >> shyness;
		int s[1001] = {};
		for (unsigned int j = 0; j < shyness.length(); ++j)
		{
			s[j] = shyness[j] - '0';
		}
		for (int k = 0; k < smax+1; ++k)
		{
			if (k==0 && s[k] == 0)
			{
				min++;
				available++;
			}
			if(available < level[k] && s[k]!=0){
				min += (level[k] - available);
				available += (level[k] - available)+s[k];
			}else if(available >= level[k]){
				available+=s[k];
			}
		}
		cout << "Case #" << i+1 << ": " << min << endl;
	}
	return 0;
}
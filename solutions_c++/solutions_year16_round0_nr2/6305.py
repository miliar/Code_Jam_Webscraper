#include "Revenge_of_the_Pancakes.h"
#include <iostream>
#include<string>
#include <algorithm>
#include<fstream>
#include <vector>
#include<cstdio>
#include<math.h>
#include<utility>
#include<queue>
#include<iomanip>



using namespace std;


	//FILE *stream;
int main(){
	//freopen_s(&stream,"C:\\Users\\Sherif\\Desktop\\output.txt", "w", stdout);
	int T; cin >> T;
	for (int k = 0; k < T; k++)
	{
		string s;
		cin >> s;
		int x = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-'){
				if (i == 0)x++;
				else if (s[i - 1] == '+')x += 2;
			}
		}
		cout << "Case #" << k + 1 << ": " << x << endl;
	}
	
	
}
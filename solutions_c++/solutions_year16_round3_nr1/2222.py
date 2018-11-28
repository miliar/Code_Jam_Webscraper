#include "Senate_Evacuation.h"
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
#include<set>



using namespace std;



FILE *stream;
long long gcd(long long x, long long y){
	while (y != 0){
		long long a = x%y;
		x = y;
		y = a;
	}
	return x;
}


int main(){
	//freopen_s(&stream,"C:\\Users\\Sherif\\Desktop\\output.txt", "w", stdout);
	long long T; cin >> T;
	for (long long k = 0; k < T; k++)
	{
		int n;
		cin >> n;
		vector<pair<int, char>> parties;
		int total= 0;
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			total += x;
			pair<int, char> temp;
			temp.first = x;
			temp.second = (char)i + 'A';
			parties.push_back(temp);
		}
		string s = "";
		for (int i = 0; i < total; i++)
		{
			sort(parties.begin(), parties.end());
			reverse(parties.begin(), parties.end());
			if (parties[0].first == 0)break;
			else if ((i == total - 3) && (parties[0].first != 0) && (parties[1].first != 0) && (parties[2].first != 0)){
				s += (char)parties[0].second;
				parties[0].first--;
			}
			else if ((parties[0].first != parties[1].first)&& parties[0].first>=2){
				s += (char)parties[0].second;
				s += (char)parties[0].second;
				parties[0].first -= 2;
				i++;
			}
			else if (parties[0].first!=0 && parties[1].first!=0){
				s += (char)parties[0].second;
				s += (char)parties[1].second;
				parties[0].first--;
				parties[1].first--;
				i++;
			}
			else{
				s += (char)parties[0].second;
				parties[0].first--;
			}
			s += " ";
		}
		cout << "Case #" << k + 1 << ": " << s << endl;
	}	
}
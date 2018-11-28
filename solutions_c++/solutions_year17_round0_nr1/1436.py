// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#ifdef _MSC_VER
#include "stdafx.h"
#endif
#include <cassert>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#ifdef _MSC_VER
#include "stdafx.h"
#endif
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
typedef long long ll;
using namespace std;
bool A[2010];

#ifdef WIN32
int __stdcall WinMain(int hThisInstance, int hPrevInstance, int lpszArgument, int nCmdShow)
#else
int main()
#endif
{	ios::sync_with_stdio(false); cin.tie(NULL);
int T; cin >> T;
for (int j = 0; j < T; j++) {
	string s;
	cin >> s;
	unsigned int K; cin >> K;
	int ans = 0;
	for (unsigned int i = 0; i < s.size(); i++)A[i] =( s[i] == '+');
	for (unsigned int i = 0; i < s.size(); i++) {
		if (A[i] == false) {
			if (i + K > s.size()){ans = -1; break;}
			for (int x = i; x < i + K; x++)A[x] = !A[x];
			ans++;
		}
		
	}
	//for(int i=0;i<s.size();i++)cout << A[i] << " ";
	cout << "Case #" << j+1<< ": " ;
	if (ans < 0) cout<<"IMPOSSIBLE"<<endl;
	else cout<< ans << endl;
}

	return 0;
}

/*

*/

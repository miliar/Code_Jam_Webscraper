#include<iostream>
#include<cstdio>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<string>
#include<set>
#include<utility>
#include<functional>
#include<map>
#include<sstream>
#define PB push_back
#define FOR(N,i) for(int i =0; i < N; i++)
#define lli long long int

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int j = 0; j < t; j++)
	{	
	 	string S;
	 	cin >> S;
	 	int cnt = 1;
	 	for(int i = 1 ;i < S.length(); i++)
	 	{
	 		if(S[i] != S[i-1])
	 			cnt++;
	 	}
	 	if(S[S.length() - 1] == '+')
	 		cout << "Case #" << j+1 << ": "<< cnt -1 << endl;
	 	else
	 		cout << "Case #" << j+1 << ": "<< cnt << endl;
	 }
}


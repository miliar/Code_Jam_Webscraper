#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<set>

#define INF 1000000000
#define endl '\n'
#define ll long long

using namespace std;


int main()
{
//	ios::sync_with_stdio(false);
//	cin.tie(0);
	
	string num[10];
	int order[10] = {0,2,6,8, 7,5,4,3,1,9};
	string key = "ZWXGSVFTOI";
	
	num[0] = "ZERO";
	num[1] = "ONE";
	num[2] = "TWO";
	num[3] = "THREE";
	num[4] = "FOUR";
	num[5] = "FIVE";
	num[6] = "SIX";
	num[7] = "SEVEN";
	num[8] = "EIGHT";
	num[9] = "NINE";
	
	/*
	for(int i = 0 ; i <= 9 ; i++)
	{
		for(IT it=num[i].begin(); it != num[i].end(); it++)
			cout << (*it);
		cout << endl;
	}
	*/
	
	int T;
	cin >> T;
	for(int t = 1 ; t <= T ; t++)
	{
		string s;
		cin >> s;
		
		int cnt[300];
		memset(cnt,0,sizeof(cnt));
		for(int i = 0 ; i < s.size() ; i++)
			cnt[s[i]]++;
		/*
		for(int i = 'A' ; i <= 'Z'  ;i++)
			cout << cnt[i] << " ";
		cout << endl;
		*/
		
		int ans[10];
		memset(ans,0,sizeof(ans));
		
		for(int i = 0 ; i < 10 ; i++)
		{
			int x = order[i];
			char k = key[i];
//			cout << "x = " << x <<endl;
//			cout << " key = " <<k <<endl;
			if(cnt[k] > 0)
			{
				ans[x] = cnt[k];
//				cout << "ans[" <<x << "] = " <<ans[x] << endl;
				for(int j = 0 ; j < num[x].size() ; j++)
					cnt[num[x][j]] -= ans[x];
			}
		}
		
		/*
		for(int i = 'A'; i <= 'Z' ; i++)
			if(cnt[i] != 0)
				cout << "!!" << (char)i;
		cout << endl;
		*/
		
		cout << "Case #" << t << ": ";
		for(int i = 0 ; i < 10 ; i++)
		{
			for(int j = 0 ; j < ans[i] ; j++)
				cout << i;
		}
		cout <<endl;
	}
	
	return 0;
}


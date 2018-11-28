/* bhupkas */

#include "bits/stdc++.h"

using namespace std;

vector < pair < char , int > > change(string str)
{
	vector < pair < char , int > > re;
	char ch = '#';
	int cnt = 0;
	for(int i = 0 ; i < str.size() ; ++i)
	{
		if(str[i] == ch)	
		{
			cnt++;
		}
		else
		{
			re.push_back(make_pair(ch,cnt));
			cnt = 1;
			ch = str[i];
		}
	}
	re.push_back(make_pair(ch,cnt));
	return re;
}

int fun(string s1,string s2)
{
	vector < pair < char , int > > v1,v2;
	v1 = change(s1);
	v2 = change(s2);
	int re = 0;
	if(v1.size() != v2.size())	return -1;
	for(int i = 0 ; i < v1.size() ; ++i)
	{
		if(v1[i].first != v2[i].first)	return -1;
		re += max(v1[i].second,v2[i].second) - min(v1[i].second,v2[i].second);
	}
	return re;
}

int main()
{
	int t;
	cin >> t;
	for(int tc = 1 ; tc <= t ; ++tc)
	{
		printf("Case #%d: ",tc);
		int n;
		cin >> n;
		string str1,str2;
		cin >> str1 >> str2;
		int re = 0;
		int check = fun(str1,str2);
		if(check == -1)
		{
			puts("Fegla Won");
			continue;
		}	
		else	cout << check << endl;
	}
	return 0;
}
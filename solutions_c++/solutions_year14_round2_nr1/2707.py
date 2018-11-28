#include<algorithm>
#include<deque>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;
		vector<string> v;
		string s;
		for (int j = 0; j < N; ++j)
		{
			cin >> s;
			v.push_back(s);
		}
		
		int ttl = 0;
		bool ok = true;
		//cout << "dealing: " << endl;
		while (v[0].size() > 0 && ok)
		{
			vector<int> vCnt;		// for counting
			for (int j = 0; j < N; ++j)
				vCnt.push_back(0);
			char ch = v[0][0];
			string s2;
			for (int j = 0; j < N && ok; ++j)
			{
				//cout << "dealing line " << j << endl;
				int cnt = -1;
				s2 = v[j];
				int k = 0;
				if (s2.size() == 0)
				{
					//cout << "step 1" << endl;
					ok = false;
					break;
				}

				if (s2[0] != ch)
				{
					ok = false;
					break;
				}
				for (; k < s2.size(); ++k)
				{
					/*
					if (s2[k] != ch && j != 0)
					{
						cout << "step 2" << endl;
						ok = false;		// don't equal to first char of the first line
						break;
					} 
					else if (s2[k] != ch && j == 0)
					{
						break;
					}
					*/
					if (s2[k] != ch)
						break;
					//cout << s2[k] << '\t';
					++cnt;
				}
				//cout << endl;
				//cout << "ok: " << ok << " k = " << k << endl;
				if (!ok)
					break;
				s2 = s2.substr(k, s2.size());
				v[j] = s2;
				vCnt[j] = cnt;
			}
			if (!ok)
				break;

			int cnt = 0;
			for (int j = 0; j < vCnt.size(); ++j)
				cnt += vCnt[j];
			double avg = cnt * 1.0 / N;
			int iAvg = (int) (avg + 0.5);
			for (int j = 0; j < vCnt.size(); ++j)
			{
				int diff = vCnt[j] - iAvg;
				if (diff < 0)
				{
					ttl += diff * (-1);
				}
				else 
				{
					ttl += diff;
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		for (int j = 0;j < N; ++j)
			if (v[j].size() != 0)
			{
				ok = false;
				break;
			}
		if (!ok)
		{
			cout << "Fegla Won";
		}
		else 
		{
			cout << ttl;
		}
		cout << endl;
	}
	return 0;
}

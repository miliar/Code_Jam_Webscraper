#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;
int D, res;
map<string,bool> used;
map<string,int> d;
void transform1 (string s, vector<int> &temp)
{
	temp.resize(s.length());
	for(int i=0;i<s.length();i++)
	{
		temp[i] = s[i] -'0';
	}
}
//---------------
string transform2 (vector<int> &temp)
{
	string s;// "                                                                   ";
	s.resize(temp.size(),' ');
	sort(temp.begin(), temp.end());
	for(int i=0;i<temp.size();i++)
		s[i] = temp[i] + '0';
	return s;
}
//------------------
queue<string> z;
void bfs (string p)
{
	used[p] = 1;
	z.push(p);
	d[p] = 0;
	while(!z.empty())
	{
		string hp = z.front();
		z.pop();
		vector<int> temp;
		transform1(hp,temp);
		vector<int> temp1;
		//???????? ???????? ???????? ????? ?????
			temp1 = temp;
			temp1[temp.size()-1]  = temp[temp.size()-1]/2;
			temp1.push_back(temp[temp.size()-1]/2 + temp[temp.size()-1]%2);
			string s1 = transform2(temp1);
			if(used[s1] == 0)
			{
				used[s1] = 1;
				d[s1] = d[hp] + 1;
				z.push(s1);
				/*int ok = 1;
				for(int i=0;i<s1.length();i++)
					if(s1[i] != '0')
					{ ok = 0; break; }
				if(ok == 1)
				{ res = d[s1]; return; }*/
			}
		//пробуємо ділити на 3
			temp1 = temp;
			temp1[temp.size()-1]  = temp[temp.size()-1]/3;
			temp1.push_back((temp[temp.size()-1]/3)*2 + temp[temp.size()-1]%3);
			s1 = transform2(temp1);
			if(used[s1] == 0)
			{
				used[s1] = 1;
				d[s1] = d[hp] + 1;
				z.push(s1);
			}
		//???????? ??????? ?? ??????? ??? ???????
			temp1 = temp;
			for(int i=0;i<temp.size();i++)
			{
				if(temp[i] == 0)
				{ continue; }
				else
					temp1[i] = temp[i] - 1;
			}
			s1 = transform2(temp1);
			if(used[s1] == 0)
			{
				used[s1] = 1;
				d[s1] = d[hp] + 1;
				z.push(s1);
				int ok = 1;
				for(int i=0;i<s1.length();i++)
					if(s1[i] != '0')
					{ ok = 0; break; }
				if(ok == 1)
				{ res = d[s1]; return; }
			}

	}
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	vector<int> P;
	for(int t1 = 1;t1<=T;t1++)
	{
		scanf("%d", &D);
		P.resize(D);
		//used.assign(D,0
		used.clear();
		d.clear();
		while(!z.empty())
			z.pop();
		for(int i=0;i<D;i++)
			scanf("%d", &P[i]);
		sort(P.begin(),P.end());
		string s;// = "                                                                                                                                                                                                                                                                                                                                             ";
		s.resize(D,' ');
		for(int i=0;i<D;i++)
			s[i] = P[i] + '0';
		bfs(s);
		printf("Case #%d: %d\n", t1, res);
	}
	system("Pause");
	return 0;
}

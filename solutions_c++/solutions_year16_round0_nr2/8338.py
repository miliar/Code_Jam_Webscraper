#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long LL;

//*******************
//*******************

map<vector<char>, int> M;
queue < pair<vector<char>, int > > q;
void add()
{
	while(!q.empty())
	{
		vector<char> v = q.front().first; int k=q.front().second; q.pop();
		if(M.find(v) != M.end())
			continue;
		M[v]=k;
		++k;
		for(int i=0; i<v.size(); i++)
		{
			vector<char> vec = v;
			reverse(vec.begin(), vec.begin()+i+1);
			for(int j=0; j<=i; j++)
			{
				if(vec[j] == '+')
					vec[j] = '-';
				else
					vec[j] = '+';
			}
			q.push({vec, k});
		}
	}
}

int cas = 1;
int u = 1;
void read() {
	string s;cin>>s;
	vector<char> vec(s.begin(), s.end());
	cout<<"Case #"<<cas<<": "<<M[vec]<<endl;
}

void solve() {
}

void clean() {
}

int main() {
  ios::sync_with_stdio(false);
  int z;
  cin >> z;
  	vector<char> vo;
  	for(int i=0; i<10; i++)
  	{
  		vo.push_back('+');
  		q.push({vo, 0});
  	}
  	add();
  	  // cout<<M.size()<<endl;

  for(;cas<=z; cas++) {
  
     read();
     solve();
     clean();
  }
  return 0;
}
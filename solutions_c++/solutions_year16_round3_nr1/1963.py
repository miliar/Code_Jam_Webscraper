#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
 
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define _D(p) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p)<<std::endl;
#define _D2(p,q) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p) << ", " #q " = "<<(q)<<std::endl;
#define _DN(v) std::cout<<"L"<<__LINE__<<" : " #v " = ["; rep(i,(v).size()) {std::cout<<v[i]<<(i==v.size()-1?"":", ");}std::cout<<"]"<<std::endl;
#define _DNN(v) std::cout<<"L"<<__LINE__<<" : " #v " = [" << std::endl; rep(i,(v).size()) {std::cout<<"	[";rep(j,(v)[0].size()){std::cout<<v[i][j]<<(j==v[0].size()-1?"":", ");}std::cout<<"],"<<std::endl;}std::cout<<"]"<<std::endl;
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};


class Party{
	public:
		char name;
		int num;
		Party(char n, int nu):name(n), num(nu){
		}
		bool operator<(const Party& right) const { return num<right.num; }
};

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		int N;
		cin >> N;
		std::vector<Party> v;
		for (int j = 0; j < N; ++j)
		{
			int a;
			cin >> a;
			v.push_back(Party('A'+j, a));
		}
		//cout << v.size() << endl;
		//for (int j = 0; j < v.size(); ++j)
		//{
		//	cout << "(" << v[j].name <<", " << v[j].num << "), ";
		//}
		bool flag = true;
		while(flag){
			sort(all(v));
			if(v[v.size()-1].num==v[v.size()-2].num){
				int sum = 0;
				for (int j = 0; j < v.size(); ++j)
				{
					sum += v[j].num;
				}
				if(sum == 3){
					cout << v[v.size()-1].name << " " ;
					v[v.size()-1].num--;
				}
				else{cout << v[v.size()-1].name << v[v.size()-2].name << " ";
				v[v.size()-1].num--;
				v[v.size()-2].num--;}
			}
			else{
				cout << v[v.size()-1].name << " " ;
				v[v.size()-1].num--;
			}
			flag = false;
			for (int j = 0; j < v.size(); ++j)
			{
				if (v[j].num != 0)
				{
					flag = true;
					break;
				}
			}
			if(!flag){
				cout << endl;
			}
		}
	}
	return 0;
}
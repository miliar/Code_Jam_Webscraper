#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char _buffer[2048];

#define FILE_NAME "A"
#define LL long long
#define ULL unsigned long long
#define CASET int _t=0, case_num;cin>>case_num;while(++_t<=case_num)

typedef vector<int> VI;
typedef vector<VI> VVI;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char dir[4] = {'E', 'S', 'W', 'N'};

bool solve()
{
	return false;
}	

int main()
{
	sprintf(_buffer, "%s.in", FILE_NAME);
	freopen(_buffer, "r", stdin);
	sprintf(_buffer, "%s.out", FILE_NAME);
	freopen(_buffer, "w", stdout);

	CASET
	{
		string input;
		cin>>input;
		map<char,int> dic;
		vector<int> ans;
		for(int i=0;i<input.length();i++){
			dic[input[i]]+=1;
		}
		int len = dic['Z'];
		for(int i=0;i<len;i++)
			ans.push_back(0);
		dic['Z']-=len;
		dic['E']-=len;
		dic['R']-=len;
		dic['O']-=len;
		len = dic['W'];
		for(int i=0;i<len;i++)
			ans.push_back(2);
			dic['T']-=len;
			dic['W']-=len;
			dic['O']-=len;
		
		len = dic['U'];
		for(int i=0;i<len;i++)
			ans.push_back(4);
			dic['F']-=len;
			dic['O']-=len;
			dic['U']-=len;
			dic['R']-=len;
		
		len = dic['X'];
		for(int i=0;i<len;i++)
			ans.push_back(6);
			dic['S']-=len;
			dic['I']-=len;
			dic['X']-=len;
		
		len = dic['G'];
		for(int i=0;i<len;i++)
			ans.push_back(8);
			dic['E']-=len;
			dic['I']-=len;
			dic['G']-=len;
			dic['H']-=len;
			dic['T']-=len;
		
		len = dic['O'];
		for(int i=0;i<len;i++)
			ans.push_back(1);
			dic['O']-=len;
			dic['N']-=len;
			dic['E']-=len;
		
		len = dic['F'];
		for(int i=0;i<len;i++)
			ans.push_back(5);
			dic['F']-=len;
			dic['I']-=len;
			dic['V']-=len;
			dic['E']-=len;
		
		len = dic['T'];
		for(int i=0;i<len;i++)
			ans.push_back(3);
			dic['T']-=len;
			dic['H']-=len;
			dic['R']-=len;
			dic['E']-=len*2;
		
		len = dic['S'];
		for(int i=0;i<len;i++)
			ans.push_back(7);
			dic['S']-=len;
			dic['E']-=len*2;
			dic['V']-=len;
			dic['N']-=len;
		
		len = dic['I'];
		for(int i=0;i<len;i++)
			ans.push_back(9);
			dic['N']-=len*2;
			dic['I']-=len;
			dic['E']-=len;
		
		
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<_t<<": ";
		for(int i=0;i<ans.size();i++)
			cout<<ans[i];
		cout<<endl;
	}
		
	return 0;
}
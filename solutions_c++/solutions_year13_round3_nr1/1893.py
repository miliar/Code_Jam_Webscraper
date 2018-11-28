#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<list>
#include<utility>
using namespace std;

bool IsVowel(char ch)
{
	if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u')
		return true;
	return false;
}
int main()
{
	int testCases;
	cin>>testCases;
	for(int i=0;i<testCases;++i)
	{
		string str;
		cin>>str;
		int n;
		cin>>n;
		deque<int>vowelList;
		for(int j=0;j<str.length();++j)
		{
			if(IsVowel(str[j]))
			{
				vowelList.push_back(j);
			}
		}
		vowelList.push_back(str.length()+n+1);
		int front=vowelList.front();
		vowelList.pop_front();
		int end=IsVowel(str[0])+n;
		long answer=0;
		for(int j=0;j<str.length();++j)
		{
			int start=j+IsVowel(str[j]);
			while(front-start <n and vowelList.size())
			{
				start=front+1;
				if(start>=str.length())
				{
					end=str.length();
					break;
				}
				front=vowelList.front();
				vowelList.pop_front();
			}
			end=start+n-1;
			if(end>str.length())
				end=str.length();
			answer+=((str.length()-end)*(start-j+1));
			j=start;
		}
		cout<<"Case #"<<i+1<<": "<<answer<<endl;
	}
	return 0;
} 
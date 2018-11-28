#include <bits/stdc++.h>
using namespace std;


int flipFun(string s, int end)
{
	int flips=0;
	while(end>-1 && s.at(end)=='+')
		end--;
	if(end==-1)
		return flips;
	if(s.at(end)=='-')
	{
		for(int i=0;i<=end-1;i++)
		{
			if(s.at(i)=='+')
				s[i]='-';
			else
				s[i]='+';
		}
	}
	//cout<<s<<endl;
	flips=flipFun(s,end-1);
	return flips+1;
}



int main(int argc, char const *argv[])
{
	int T;
	scanf("%d",&T);
	int flips;
	for(int z=0;z<T;z++)
	{
		string s;
		cin >> s;
		flips=flipFun(s,s.size()-1);
		cout<< "Case #"<<z+1<<": "<<flips<<endl;
	}
	return 0;
}
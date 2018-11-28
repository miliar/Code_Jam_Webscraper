#include<vector>
#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int countRequiredFrnds(string);
int main()
{
int T; scanf("%d",&T);
for(int i=1;i<=T; i++)
{
	int Smax;
	string s;
	cin>>Smax;	cin.clear(); cin.ignore(1,'\n');
	getline(cin,s);
	printf("Case #%d: %d\n",i,countRequiredFrnds(s));
}
cin.get(); cin.get();
return 0;
}

int countRequiredFrnds(string s)
{
	int requirement = 0;
	int got = s[0]-'0';
	for(int i=1;i<s.size();i++)
	{
		if(i>(got+requirement))				requirement++;
		got += s[i]-'0';
		if(got >= s.size())		return requirement;
	}
	return requirement;
}
/*
	Google Code Jam 2015 资格赛01题：
	魔术师猜数字：主要熟悉测试环境
	https://code.google.com/codejam/contest/2974486/dashboard#s=p0
 */

#include <iostream>


using namespace std;

void solution01(int case_num)
{
	int maxS;
	int kArr[1000] = {0};
	cin>>maxS;
	for (int i = 0; i < maxS+1; ++i)
	{
		char ch;
		cin>>ch;
		kArr[i] = ch-48;
	}

	int alreadyStrand = kArr[0];
	int needPeople = 0;
	for (int i = 1; i < maxS+1; ++i)
	{
		int needThisLevel = 0; 
		if(i > alreadyStrand)
			needThisLevel += i - alreadyStrand;
		//cout<<"level"<<i<<" "<<needPeople<<" "<<needThisLevel<<" "<<alreadyStrand<<" "<<kArr[i]<<endl;
		alreadyStrand += needThisLevel + kArr[i];
		needPeople += needThisLevel;
	}

	cout<<"Case #"<<case_num<<": "<<needPeople<<endl;
}

int main()
{
	int case_num;
	cin>>case_num;
	for (int t = 0; t < case_num; ++t)
	{
		solution01(t+1);
	}

	return 0;
}
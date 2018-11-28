#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(void)
{
	int test,count=0,num;
	float value;
	vector<float> v1,v2;
	int score1,score2;
	//ofstream cout("ansDL.out");
	//ifstream cin("D-large.in");
	cin>>test;
	while(count++<test)
	{
		score1=0;
		score2=0;
		cin>>num;
		bool flag=true;
		bool *flag1=new bool[num];
		bool *flag2=new bool[num];
		for(int i=0;i<num;i++)
			flag1[i]=false;
		for(int i=0;i<num;i++)
			flag2[i]=false;
		for(int i=0;i<num;i++)
		{
			cin>>value;
			v1.push_back(value);
		}
		for(int i=0;i<num;i++)
		{
			cin>>value;
			v2.push_back(value);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		for(int i=0;i<v1.size();i++)
		{
			for(int j=0;j<v2.size();j++)
				if(v2[j]>v1[i]&&flag2[j]==false)
				{
					flag1[i]=true;
					flag2[j]=true;
					break;
				}
			if(flag1[i]==false)
			{
				for(int k=0;k<num;k++)
					if(flag2[k]==false)
					{
						flag2[k]=true;
						break;
					}
				flag1[i]=true;
				score2++;
			}
		}
		while(v1.size()!=0)
		{
			flag=true;
			for(int i=0;i<v1.size();i++)
			{
				if(v1[i]<v2[i])
				{
					flag=false;
					break;
				}
			}
			if(!flag)
			{
				v1.erase(v1.begin());
				v2.erase(v2.end()-1);
			}
			else
			{
				score1=v1.size();
				break;
			}
		}
		cout<<"Case #"<<count<<": "<<score1<<' '<<score2<<endl;
		delete []flag1;
		delete []flag2;
		v1.clear();
		v2.clear();
	}
	return 0;
}
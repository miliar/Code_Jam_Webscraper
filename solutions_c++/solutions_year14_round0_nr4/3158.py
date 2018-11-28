// jam4.cpp : 定义控制台应用程序的入口点。
//

#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include <iomanip>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;
vector<float> naomi;
vector<float> ken;

int main()
{
	int m;
	int num;
	float weight;
	int nao_you,ke_you;
	fstream file1;
	file1.open("D-large.txt",ios::in);
	file1>>m;
	fstream file2;
	file2.open("d-output.txt",ios::out);
	for(int i = 0;i < m;i++)
	{
		file1>>num;
		for(int j = 0;j < num;j++)
		{
			file1>>weight;
			naomi.push_back(weight);
		}
		for(int j = 0;j < num;j++)
		{
			file1>>weight;
			ken.push_back(weight);
		}
		sort(naomi.begin(),naomi.end());
		vector<float>::iterator nao = naomi.begin();
		sort(ken.begin(),ken.end());
		vector<float>::iterator ke = ken.begin();
		int count = 0;
		for(int k = 0;k < num;k++)
		{
			float temp1 = *nao;
		    if(*ke < temp1)
			{
			    count++;
				ke++;
			}
			nao++;
		}
		ke_you = count;
		count = 0;
		nao = naomi.begin();
		ke = ken.begin();
		for(int k = 0;k < num;k++)
		{
			float temp1 = *ke;
		    if(*nao < temp1)
			{
			    count++;
				nao++;
			}
			ke++;
		}
		nao_you = num - count;
		file2<<"Case #";
		file2<<i+1;
		file2<<": ";
		file2<<ke_you;
		file2<<" ";
		file2<<nao_you;
		file2<<"\n";
		naomi.clear();
		ken.clear();
	}

	system("pause");
	return 0;
}




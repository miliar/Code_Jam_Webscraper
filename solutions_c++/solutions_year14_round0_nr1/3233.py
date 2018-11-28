
#define _CRT_SECURE_NO_WARNINGS


//source here
#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Case = 0; Case < T; Case++)
	{
		int a[4][4];
		int frow,srow;
		scanf("%d", &frow);
		vector<int> vec1,vec2;
		for (int i = 0; i < 4;i++)
		{
			for (int j = 0; j < 4;j++)
			{
				scanf("%d", &a[i][j]);
			}
		}
		for (int i = 0; i < 4; i++){
			vec1.push_back(a[frow-1][i]);
		}
		scanf("%d", &srow);
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &a[i][j]);
			}
		}
		for (int i = 0; i < 4; i++){
			vec2.push_back(a[srow - 1][i]);
		}
		vector<int> result;
		for (int i = 0; i < vec1.size(); i++)
		{
			if (find(vec2.begin(),vec2.end(),vec1[i])!=vec2.end())
			{
				result.push_back(vec1[i]);
			}
		}
		printf("Case #%d: ", Case + 1);
		if (result.size()>1)
		{
			printf("Bad magician!\n");
		}
		else if (result.size()==0)
		{
			printf("Volunteer cheated!\n");
		}
		else{
			printf("%d\n", result[0]);
		}
	}
	return 0;
}
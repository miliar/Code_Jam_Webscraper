
#define _CRT_SECURE_NO_WARNINGS


//source here
#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

int main(){
	//freopen("D-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Case = 0; Case < T; Case++)
	{
		int n;
		scanf("%d", &n);
		vector<double> v1, v2;
		int w1=0, w2 = 0;
		for (int i = 0; i < n;i++)
		{
			double temp;
			scanf("%lf", &temp);
			v1.push_back(temp);
		}
		sort(v1.begin(), v1.end());
		for (int i = 0; i < n; i++)
		{
			double temp;
			scanf("%lf", &temp);
			v2.push_back(temp);
		}
		sort(v2.begin(), v2.end(), greater<double>());
		for (int i = 0,j=n-1; i < n; i++)
		{
			if (v1[i]<v2[j])
			{
			}
			else{
				j--;
				w1++;
			}
		}
		sort(v2.begin(), v2.end());
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < v2.size();j++)
			{
				if (v2[j]>v1[i])
				{
					v2.erase(v2.begin()+j);
					break;
				}
			}
		}
		w2 = v2.size();
		printf("Case #%d: %d %d\n", Case + 1,w1,w2);
	}
	return 0;
}
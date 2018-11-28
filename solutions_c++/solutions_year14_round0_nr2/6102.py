// Problem B. Cookie Clicker Alpha.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
using namespace std;


int main()
{
	FILE *fp;
	fp = fopen("d:\\out.txt","w");
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		double c, f, x, min, time, temp, tp;
		scanf("%lf%lf%lf", &c, &f, &x);
		min = x / 2;
		tp = 2;
		temp = c / 2;
		time = temp + x / (tp + f);
		while (time < min)
		{
			min = time;
			tp += f;
			temp += c / tp;
			time = temp + x / (tp + f);
		}
		fprintf(fp, "Case #%d: %.7lf\n", i + 1, min);
	}
	getchar();
	getchar();
	return 0;
}


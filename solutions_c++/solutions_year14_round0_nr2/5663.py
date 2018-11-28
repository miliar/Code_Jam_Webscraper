#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<limits>

using namespace std;
typedef long long LL;
int main() {
	int caseNum;
	char dummy; //read the '\n' after the caseNum
	scanf("%d%c", &caseNum, &dummy);
	for (int caseCount = 1; caseCount <= caseNum; caseCount++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double rate = 2;
		double nowTime = 0;
		double minStop = numeric_limits<double>::max();
		double needTime;
		while (true) {
			needTime = x / rate;
			if (minStop > nowTime + needTime) {
				minStop = nowTime + needTime;
			} else {
				break;
			}
			//buy a farm
			nowTime += c / rate;
			rate += f;
		}
		printf("Case #%d: %.7lf\n", caseCount, minStop);
	}
	return 0;
}

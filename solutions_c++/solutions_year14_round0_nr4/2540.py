#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

int N;
vector<double> Naomi;
vector<double> Ken;

void Input()
{
	Naomi.clear();
	Ken.clear();
	cin>>N;
	for (int i = 0; i < N; i++) {
		double x;
		scanf("%lf", &x);
		Naomi.push_back(x);
	}
	for (int i = 0; i < N; i++) {
		double x;
		scanf("%lf", &x);
		Ken.push_back(x);
	}
}

void Solve(int t)
{
	sort(Naomi.begin(), Naomi.end());
	sort(Ken.begin(), Ken.end());

	int i = N - 1, j = N - 1;
	while (i >= 0 && j >=0) {
		if (Naomi[i] >= Ken[j]) {
			i--;
		}
		j--;	
	}
	int count_d = N - (i - j);

	i = 0; j = 0;
	while (i < N && j < N) {
		if (Naomi[i] <= Ken[j]) {
			i++;
		} 
		j++;
	}
	int count = j - i;
	printf("Case #%d: %d %d\n",t , count_d, count);
}

int main()
{
	int T;
	cin>>T;
	for (int i = 1; i <= T; i++) {
		Input();
		Solve(i);
	}
	return 0;
}

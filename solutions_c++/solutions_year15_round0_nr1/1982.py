#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

void test_case()
{
	int n;
	string s;
	cin >> n;
	cin >> s;
	int cnt = 0;
	int sum = 0;
	for (int i = 0; i <= n; i++)
	{
		int need = s[i] - '0';
		int lv = i;
		if (sum < lv){
			int added = lv - sum;
			cnt += added;
			sum += added;
		}
		sum += need;
	}
	cout << cnt << endl;
}
int main(){
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ",i+1);
		test_case();
	}
	return 0;
}
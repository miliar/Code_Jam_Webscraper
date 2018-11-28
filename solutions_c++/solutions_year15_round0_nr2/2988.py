#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<stdio.h>
#include<fstream>
using namespace std;

int fun(int num, int target) {
	int a = num / target;
	if(num % target != 0)
		a++;
	a--;
	return a;
}

int main() {
	ifstream fin("F:\\B-large.in");
	ofstream fout("out.txt");
	int k,d,tmp;
	int pi[1005];
	fin>>k;
	//cin>>k;
	for(int kk = 1; kk <= k; kk++) {
		memset(pi, 0, sizeof(pi));
		fin>>d;
		//cin>>d;
		int maxx = -1;
		for(int i = 0; i < d; i++) {
			fin>>tmp;
			pi[tmp]++;
			if(maxx == -1 || maxx < tmp)
				maxx = tmp;
		}
		int cur_num = 0;
		int ans = maxx;
		for(int i = maxx; i >= 2; i--) {
			int cur_ans = 0;
			for(int j = maxx; j > i; j--) {
				if(pi[j] == 0)
					continue;
				cur_ans += pi[j] * fun(j, i);
			}
			cur_ans += i;
			ans = min(ans, cur_ans);
		}
		//cout<<"Case #"<<kk<<": "<<ans<<endl;
		fout<<"Case #"<<kk<<": "<<ans<<endl;
	}
	fout.close();
	fin.close();

	return 0;
}
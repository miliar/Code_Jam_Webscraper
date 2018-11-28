#include <bits/stdc++.h>

using namespace std;
ifstream fin("test.in");
ofstream fout("test.out");

int control(int a){
	int c = 0,rs = 1;
	bool B[11] = {0,0,0,0,0,0,0,0,0,0,0};
	int n = 0;
	while(n < 10){
		c+=a;
		int b = c;
		while(b){
			if(!B[b%10]){
				B[b%10] =1;
				n++;
			}
			b/=10;
		}
		rs++;
	}
	return c;
}

int N;
int main(){
	fin >> N;
	for(int i = 1,x;i<=N;i++){
		fin >> x;
		fout << "Case #" << i << ": ";
		if(x==0)fout << "INSOMNIA";
		else fout << control(x);
		fout << '\n';
	}
}

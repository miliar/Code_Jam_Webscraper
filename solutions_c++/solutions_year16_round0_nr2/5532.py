#include<iostream>
#include<cstring>
#include<string>
using namespace std;
long long t[200], T;
string s;
void print(long long n){
	for (long long i = 0; i < n; ++i)
		cout << t[i];
	cout << endl;
};

long long fix(long long x, int c){
//	cout << "\nfix(" << x << ", " << c << ")\n";
	int newc= 1-c;
	int lastx = 0;
	for (int i = x; lastx==0 && i>=0; i--)
		if (t[i]==newc) lastx=i;
	if (lastx==0){
		if (t[0]==newc) return 1;
		return 0;
	};
	return 1+fix(lastx, newc);
};

int main(){
	cin >> T;
	for (long long j = 0; j < T; ++j) {
		cin >> s;
		cout << "Case #" << j+1 << ": ";
		long long last0=-1, ret=0;
		for (long long i = 0; i < s.size(); ++i){
			if (s.at(i)=='-'){
				t[i]=0;
				last0 = i;
			}
			else t[i]=1;
		};
		if (last0<0)
			ret = 0;
		else
			ret = fix(last0, 0)+1;
		/*
		cout << endl << ret << ":"; prlong long(s.size());
		while (last0>0){
			ret++;
			for (long long i = 0; i<= last0; ++i){
				long long l = i;
				long long p = last0 - i;
				if (l<p) {
					long long tmp = t[l];
					t[l]=t[p];
					t[p]=tmp;
					t[l]=1-t[l];
					t[p]=1-t[p];
				}
				else if (l==p) {
					t[l]=1-t[l];
				};
			};
			while (t[last0]==1 && last0>0) last0--;
		cout << endl << ret << ":"; prlong long(s.size());
		};
		if (last0==0 && t[0]==0) ret++;
		*/
		cout << ret << endl;

	};
};

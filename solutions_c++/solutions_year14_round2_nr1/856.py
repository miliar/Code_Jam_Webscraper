#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const int MNAX = 100;

string s[MNAX];
int a[MNAX];
int n;

int f1(){

	int best = 1000000000;

	for (int x=1;x<=100;++x){
		int tmp = 0;
		for (int i=0;i<n;++i){
			if (a[i]>x) tmp += a[i]-x;
			else tmp += x-a[i];
		}

		if (tmp<best) best = tmp;

	}

	return best;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	getchar();

	for (int t=1;t<=test;++t){
		string ans = "";
		int ansInt = 0;
		cin>>n;
		for (int i=0;i<n;++i){
			cin>>s[i];
		}

		while (true){
			for (int i=0;i<n;++i){
				a[i] = 0;
			}

			int numL = 0;
			for (int i=0;i<n;++i){
				if (s[i].length() == 0) numL++;
			}
			if (numL==n){
				break;
			}
			else if (numL>0){
				ans = "Fegla Won";
				break;
			}



			int num0 = 0;
			char ch = s[0][0];

			for (int i=0;i<n;++i){
				while (s[i].length() > 0 && s[i][0]==ch){
					a[i]++;
					s[i].erase(0,1);
				}

				if (a[i] == 0){
					num0++;
				}
			}
			if (num0>0 && num0<n){
				ans = "Fegla Won";
			}
			else{
				ansInt += f1();
			}



			if (ans != "") break;

		}


		if (ans == "")
			cout<<"Case #"<<t<<": "<<ansInt<<'\n';
		else
			cout<<"Case #"<<t<<": "<<ans<<'\n';
	}

	return 0;
}

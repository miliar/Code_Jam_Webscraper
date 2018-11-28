#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <sstream>
#include <iostream>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long int ll;
typedef pair<int, int> pii;
//freopen("inp.in","r", stdin);

bool seen[10];
int n, x, sol;
bool nots;

void getDigits(int num){
	do {
		int digit = num % 10;
		seen[digit] = true;
		num /= 10;
		//cout << num;
	} while (num > 0);
}

bool complete(){
	for(int i=0;i<10;i++){
		if(!seen[i])return false;
	}
	return true;
}


int main(){
	freopen("inp.in","r", stdin);
	freopen("out.p","w", stdout);
	scanf("%d", &n);
	int c = 0;
	while(n--){
		c++;
		scanf("%d", &x);
		nots = false;
		for(int i=0;i<10;i++) seen[i] = false;
		if(x==0) {
			nots = true;
		}
		else{
			int i = 1;
			//x = 1213189;
			while(true){
				getDigits(i * x);
				if(i > 1000000000){ nots = true; break;}
				if(complete())break;
				i++;
			}
			sol = (i) * x;
		}
		if(nots) printf("Case #%d: INSOMNIA\n",c);
		else printf("Case #%d: %d\n",c ,sol);


	}
	return 0;
}

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

string l;
int n, len, r;

int main(){
	freopen("inp.in","r", stdin);
	freopen("out.p","w", stdout);
	scanf("%d", &n);
	int c = 0;
	while(n--){
		c++;
		cin >> l;
		len = l.size();
		r = 0;
		int stack = 0;
		int stack2 = 0;

		for(int i = 0; i < len; i++){
			if(l[i] == '-'){
				if(stack2 > 0 && stack == 0){
					stack2 = 0;
					r++;
				}
				stack++;
			}
			else{
				if(stack > 0 && stack2 == 0){
					stack = 0;
					r++;
				}
				stack2++;
			}
		}
		if(stack)r++;

		printf("Case #%d: %d\n",c ,r);

	}
	return 0;
}

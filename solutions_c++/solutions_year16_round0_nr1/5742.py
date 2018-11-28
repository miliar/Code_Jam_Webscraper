#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#define lli long long int
#define ii pair<int,int>
#define mp make_pair
#define mod 1000000007
#define inf 999999999

using namespace std;

int A[10];
int t,n,ans;

string s;

int main() {
	// freopen("inp", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>t;

	for(int a=1;a<=t;a++) {
		cin>>n;

		if(n==0) {
			printf("Case #%d: INSOMNIA\n",a);
			continue;
		}

		memset(A,0,sizeof A);

		ans = 0;
		int val = 0;

		int num = 0;
		while(val<10) {
			num += n;

			int num1 = num;

			while(num1 != 0) {
				if(A[num1%10] == 0) {
					A[num1%10] = 1;
					val++;
				}
				num1 /= 10;
			}

		}

		printf("Case #%d: %d\n",a,num);
	}




	return 0;
}
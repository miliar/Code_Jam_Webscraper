#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <math.h>
#include <time.h>
#include <set>
#include <utility>
#include <map>
#include <stdio.h>
#include <assert.h>
#include <limits.h>
 
using namespace std;

 
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
#define var(a,b) __typeof(b) a = b
#define rep(i,n) for(int i = 0;(i) < (n); ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it) for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define all(v) v.begin(),v.end()



int main(){
	int t;

	freopen("A-small-attempt1(1).in","r",stdin);
	freopen("ans.out","w",stdout);

	cin >> t;

	for(int i = 1; i <= t; i++){
		int a,b,x;
		cin >> a;
		int arr[5];
		for(int j = 1; j <= 4; j++){
			for(int k = 1; k <= 4; k++){
				if(j == a){
					cin >> arr[k];
				}
				else cin >> x;
			}
		}

		cin >> b;
		int arr2[5];
		for(int j = 1; j <= 4; j++){
			for(int k = 1; k <= 4; k++){
				if(j == b){
					cin >> arr2[k];
				}
				else cin >> x;
			}
		}

		int num = 0;
		int flag = 0;
		for(int j = 1; j <= 4; j++){
			for(int k = 1; k <= 4; k++){
				if(arr[j] == arr2[k]){
					flag++;
					num = arr[j];
				}
			}
		}

		if(flag == 0){
			printf("Case #%d: Volunteer cheated!\n",i);
		}else if(flag == 1){
			printf("Case #%d: %d\n",i,num);
		}else if(flag >= 2){
			printf("Case #%d: Bad magician!\n",i);
		}
	}
	// printf("\b");
	return 0;
}
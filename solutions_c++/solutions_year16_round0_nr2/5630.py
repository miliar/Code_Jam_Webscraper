#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 20350
#define ll long long int
#define INF 0xffffff
#define PI acos(-1)
#define MOD 1000000007LL
 
using namespace std;

int T;
string pilha;

int main(){
	cin >> T;
	for(int test = 1; test <= T; test++){
		cin >> pilha;
		int ans = 0;
		bool first = 0;
		for(int i = 0; i < pilha.size(); i++){
			int j = i;
			while(j < pilha.size() && pilha[j] == '-'){
				j++;
			}
			if(j != i){
				if(first == 0){
					ans++;
				}else{
					ans += 2;
				}
				i = j - 1;
			}
			first = 1;
		}
		cout << "Case #"<< test << ": " << ans << endl;
	}
	return 0;
}

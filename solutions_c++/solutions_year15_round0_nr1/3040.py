#include<iostream>
#include<cstdio>
#include<string>
#define GI ({int t; scanf("%d", &t); t;}) 
using namespace std;

int main(){

	int t;
	t = GI;

	for(int z = 1; z <= t; z++)
	{
		int mx; 
		mx = GI;
		string s; 
		cin >> s;
		int res = 0;
		int ppl = 0;
		for(int i = 0; i <= mx; i++){
			if( ppl < i && s[i] > '0'){
				res += i - ppl;
				ppl += i - ppl;
			}
			ppl += (s[i] - '0');
			//cout << ppl << " " << res << " " << i << endl;
		}

		printf("Case #%d: %d\n", z, res);
	}

	return 0;

}
// Monjurul Huda Munna
// Daffodil International University

#include <bits/stdc++.h>

using namespace std;

typedef long long int lld;

#define Max 10000009


int main(){


 //freopen("input_RevengeOfThePancakes.txt", "r", stdin);
//	freopen("result_RevengeOfThePancakes.txt", "w", stdout);


    int i, j, k, num, test, kase = 0;
	string str;
	scanf ("%d", &test);
	while(test--){
		cin >> str;
		int len = str.length();
		int res = 0;
		i = 0;
		if(str[0] == '-'){
			res++;
			i++;
			while(i<len && str[i]=='-') i++;
		} 
		for( i=i ; i<len ; i++ ){
			if(str[i] == '-'){
				res += 2;
				while(i+1<len && str[i+1]=='-') i++;
			}
			
		}
		
		printf ("Case #%d: %d\n", ++kase, res);
	}


    return 0;
}


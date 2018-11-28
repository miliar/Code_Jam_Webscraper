#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include <cinttypes>
#include <vector>

typedef int64_t ii;
using std::vector;

char str[10005];
ii X, L;

char charAt(ii i){
	return str[i % L];
}

char multiply(char a, char b){
	char sign1 = a >= 0 ? 1 : -1;
	char sign2 = b >= 0 ? 1 : -1;
	char s = sign1 * sign2;
	if(a < 0) a = -a;
	if(b < 0) b = -b;
	
	switch(a){
		case '1':
			switch(b){
				case '1': return s * '1';
				case 'i': return s * 'i';
				case 'j': return s * 'j';
				case 'k': return s * 'k';
			}
		case 'i':
			switch(b){
				case '1': return s * 'i';
				case 'i': return s * -'1';
				case 'j': return s * 'k';
				case 'k': return s * -'j';
			}
		case 'j':
			switch(b){
				case '1': return s * 'j';
				case 'i': return s * -'k';
				case 'j': return s * -'1';
				case 'k': return s * 'i';
			}
		case 'k':
			switch(b){
				case '1': return s * 'k';
				case 'i': return s * 'j';
				case 'j': return s * -'i';
				case 'k': return s * -'1';
			}
	}
	
	printf("%c * %c\n", a, b);
	puts("WTF");
	return 0;
}

char multiplyRange(ii start, ii end){
	char cur = '1';
	for(ii i = start; i < end; ++i){
		cur = multiply(cur, charAt(i));
	}
	return cur;
}

int main(){
	int t, T;
	ii i;
	
	scanf("%d", &T);
	for(t = 1; t <= T; ++t){
		scanf("%" PRId64 "%" PRId64, &L, &X);
		scanf(" %s", str);
		
		char cur;
		
		// First we scan from left to right, marking points where we result in i
		vector<ii> iPoints;
		cur = '1';
		for(i = 0; i < X * L; ++i){
			cur = multiply(cur, charAt(i));
			if(cur == 'i'){
				iPoints.push_back(i + 1);
			}
		}
		
		// Them we do it from right to left, looking for k
		vector<ii> kPoints;
		cur = '1';
		for(i = X * L - 1; i >= 0; --i){
			cur = multiply(charAt(i), cur);
			if(cur == 'k'){
				kPoints.push_back(i);
			}
		}
		
		for(size_t a = 0; a < iPoints.size(); ++a){
			for(size_t b = 0; b < kPoints.size(); ++b){
				//if(kPoints[b] <= iPoints[a]) continue;
				char r = multiplyRange(iPoints[a], kPoints[b]);
				if(r == 'j'){
					printf("Case #%d: YES\n", t);
					goto NextTest;
				}
			}
		}
		
		printf("Case #%d: NO\n", t);
		
		NextTest:;
	}
	
	return 0;
}



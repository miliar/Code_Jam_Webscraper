#include <cstdio>
#include <iostream>
#include <string>
#include <cassert>
using namespace std;

char reduce(char a, char b) {
	char ret = 0;
	char sign = 1;
	if (a < 0) {
		a = -a;
		sign *= -1;
	}
	if (b < 0) {
		b = -b;
		sign *= -1;
	}
	if (a == 1) {
		ret = b;
	}
	if (a == 2) {
		if (b==1) ret = 2;
		if (b==2) ret = -1;
		if (b==3) ret = 4;
		if (b==4) ret = -3;
	}
	if (a == 3) {
		if (b==1) ret = 3;
		if (b==2) ret = -4;
		if (b==3) ret = -1;
		if (b==4) ret = 2;
	}
	if (a == 4) {
		if (b==1) ret = 4;
		if (b==2) ret = 3;
		if (b==3) ret = -2;
		if (b==4) ret = -1;
	}
	ret = ret * sign;
	assert(ret != 0);
	return ret;
}



int main(void) {
	int T;
	cin >> T;
	int length, repeat;
	char c, *ptr;
	char *cstr = new char [1024*1024];
	string base, full;
	bool sol;
	
	for (int t=1; t<=T; t++) {
		cin >> length >> repeat;
		base = "";
		for (int i=0; i<length; i++) {
			cin >> c;
			c = c - 'i' + 2;	//i -> 2, j -> 3, k -> 4
			base += c;
		}
		full = base;
		for (int i=1; i<repeat; i++) full += base;
		strcpy(cstr, full.c_str());
		
		ptr = cstr;
		length = strlen(ptr);
	//	for (int i=0; ptr[i]!=0; i++) printf("%d", ptr[i]); printf("\n");
		
		if (length < 3) {
			sol = false;
			goto done;
		}
		
		//find i
		while (length > 3 && ptr[0] != 2) {
			c = reduce(ptr[0], ptr[1]);
			ptr[1] = c;
			ptr = &ptr[1];
		//	for (int i=0; ptr[i]!=0; i++) printf("%d", ptr[i]); printf("\n");
			length--;
		}
		if (ptr[0] != 2) {
			sol = false;
			goto done;
		}
	//	printf("\n");
		
		//find j
		ptr = &ptr[1];
		length--;
		while (length > 2 && ptr[0] != 3) {
			c = reduce(ptr[0], ptr[1]);
			ptr[1] = c;
			ptr = &ptr[1];
		//	for (int i=0; ptr[i]!=0; i++) printf("%d", ptr[i]); printf("\n");
			length--;
		}
		if (ptr[0] != 3) {
			sol = false;
			goto done;
		}
	//	printf("\n");
		
		//find k -- must consume the rest of the string
		ptr = &ptr[1];
		length--;
		while (length > 1) {
			c = reduce(ptr[0], ptr[1]);
			ptr[1] = c;
			ptr = &ptr[1];
		//	for (int i=0; ptr[i]!=0; i++) printf("%d", ptr[i]); printf("\n");
			length--;
		}
		if (ptr[0] != 4) {
			sol = false;
			goto done;
		}
	//	printf("\n");
		
		sol = true;
		done:
		printf("Case #%d: %s\n", t, (sol) ? "YES" : "NO");
	}
	return 0;
}
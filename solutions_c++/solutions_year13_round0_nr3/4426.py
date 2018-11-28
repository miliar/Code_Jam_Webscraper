#include <algorithm>
#include <climits>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;


bool isPalindrome(int n)
{
	string ns;
	while(n != 0)
	{
		ns += ('0' + n%10);
		n /= 10;
	}

	for(int i=0;i<ns.size()/2;i++)
		if(ns[i] != ns[ns.size()-i-1])
			return false;

	return true;
}

int main(void)
{
	FILE* fin = fopen("C-small-attempt0.in", "r");
	FILE* fout = fopen("C-small-attempt0.out", "w");

	int numTests;
	fscanf(fin, "%d\n", &numTests);

	for(int testIndex=0;testIndex<numTests;testIndex++)
	{
		int a, b;
		fscanf(fin, "%d %d", &a, &b);

		int res = 0;

		for(int i=sqrt(a)-1;i<=sqrt(b)+1;i++) {
			if(isPalindrome(i)) {
				int ii = i*i;
				if(isPalindrome(ii) && ii >= a && ii <= b)
					res++;
			}
		}

		fprintf(fout, "Case #%d: %d\n", testIndex+1, res);
	}

	//for(int i=0;i<1000;i++)
	//{
	//	if(isPalindrome(i)) {
	//		int ii = i*i;
	//		if(isPalindrome(ii)) {
	//			printf("FS: %d (from %d)\n", ii, i);
	//		}
	//		else {
	//			printf("P: %d\n", i);
	//		}
	//	}
	//}

	fclose(fin);
	fclose(fout);

	return 0;
}
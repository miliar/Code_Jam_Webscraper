/*********************************ENTER THE DRAGON**********************************/

#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <set>
#include <map>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>
#include <cassert>
#include <climits>
using namespace std;

/************************************************************************************/

#define from_file 1

int main()
{
   //if (from_file) {
	   FILE *in_, *out_;
	   in_ = fopen("A-large.in", "r");
	   out_= fopen("out.txt", "w");
   //}
   
   int t;
   if (from_file) fscanf(in_, "%d", &t);
   else scanf("%d", &t);
   
   for (int T = 1; T <= t; T++) {
   	    int n;
   	    if (from_file) fscanf(in_, "%d", &n);
        else scanf("%d", &n);
        
        if (n == 0) {
        	
        	if (from_file) {
        		fprintf(out_, "Case #%d: INSOMNIA\n", T);
        		printf("Case #%d: INSOMNIA\n", T);
        	} else {
        		printf("Case #%d: INSOMNIA\n", T);
        	}
        	
        } else {
        	
        	set< int > nums;
        	for (int i = 1; ; i++) {
        		 long long cur = 1LL * i * n;
        		 while (cur > 0) {
        		 	  nums.insert( (int) (cur % 10) );
        		 	  cur /= 10;
        		 }
        		 if (nums.size() == 10) {
        		 	 if (from_file) {
		        		fprintf(out_, "Case #%d: %lld\n", T, 1LL * i * n);
		        		printf("Case #%d: %lld\n", T, 1LL * i * n);
		        	 } else {
		        		printf("Case #%d: %lld\n", T, 1LL * i * n);
		        	 }
		        	 break;
        		 }
        	}
        }
   }
   return 0;
}




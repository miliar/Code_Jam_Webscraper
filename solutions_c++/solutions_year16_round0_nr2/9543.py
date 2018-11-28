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

const int maxn = 100100;
char a[maxn];

int main()
{
   FILE *in_, *out_;
   in_ = fopen("B-large.in", "r");
   out_= fopen("out.txt", "w");
   
   int t;
   if (from_file) fscanf(in_, "%d", &t);
   else scanf("%d", &t);
   
   for (int T = 1; T <= t; T++) {
   	    int n, ans = 0;
   	    if (from_file) fscanf(in_, "%s", &a);
        else scanf("%s", &a);
        
        n = strlen(a);
        
        for (int k = n - 1; k > 0; k--) {
				if (a[k] == '-') {
					if (a[0] == '+') {
						ans += 2;
						for (int f = 0; f < k; f++) {
							if (a[f] == '-') {
								break;
							} else {
								a[f] = '-';
							}
						}
					}
					else {
						ans += 1;
					}
					int l1 = 0;
					int r1 = k;
					while (l1 <= r1) {	
 
						if(l1 != r1) {
							if (a[l1] == '+')
							{
								a[l1] = '-';
							}
							else
							{
								a[l1] = '+';
							}
							
							if (a[r1] == '+')
							{
								a[r1] = '-';
							}
							else
							{
								a[r1] = '+';
							}
						}
						else
						{
							if (a[l1] == '-')
							{
								a[l1] = '+';
							}
							else
							{
								a[l1]='-';
							}
						}
						char temp = a[l1];
						a[l1] = a[r1];
						a[r1] = temp;
 
						l1++;
						r1--;
					}
				}
			}
			if (a[0] == '-')
			{
				ans++;
			}
			fprintf(out_, "Case #%d: %d\n", T, ans);
            printf("Case #%d: %d\n", T, ans);
   }
   return 0;
}




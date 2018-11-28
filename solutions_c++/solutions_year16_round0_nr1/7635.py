#include <stdio.h>
#include <string.h>
#include <set>
using namespace std;

int main() {
		int n, i;
		scanf("%d",&n);
		int Case = 1, mulBy, pSize;
		unsigned long long int input, val;
		while (Case <= n) {
				scanf("%llu",&input);	
				int digits[] = {0,1,2,3,4,5,6,7,8,9};
				set<int> VisitedSet(digits,digits+10);


				int mulBy = 0;
				if (input == 0) {
						printf("Case #%d: INSOMNIA\n",Case );

				}else {
						do {
								mulBy++;
								val = input * mulBy;
								while (val) {
										VisitedSet.erase(val%10);
										val = val / 10;
								}
						}while(!VisitedSet.empty()); 
						{
								printf("Case #%d: %llu\n",Case, input*mulBy);
						}
				}
				Case++;		
		}
		return 0;
}

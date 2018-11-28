#include <stdio.h>
#include <string.h>
int main() {
		int n, i;
		int len;
		int order;
		int addS[2] = {1, -1};
		int addE[2] = {-1, 1};
		char CharS[2] ={'+', '-'};
		char CharE[2] = {'-' , '+'};
		char input[101];
		int start,end, temp, Count;
		scanf("%d",&n);
			int Case = 1;
		while (Case <= n) {
				scanf("%s",input);	
				len = strlen(input);
				order = 1;
				start = len - 1;
				end = 0;
				Count = 0;
				while (start != end) {
						if (CharS[order] == input[start]) {
								temp = end;	
								while (CharE[order] == input[temp])
										temp += addE[order];
								if (temp != end) {
										end = temp;
										Count++;
								}

								temp = start;
								start = end;
								end = temp;
								Count++;
								order = (order + 1) % 2;
						} else {	
								start = start + addS[order];
						}
				}
				if (input[start] == CharS[order]) {
					Count++;
				}	
			printf("Case #%d: %d\n",Case, Count);
			Case++;		
		}


		return 0;
}

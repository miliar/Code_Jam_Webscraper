#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main()
{
	//FILE *in = fopen("input.txt", "r");
	FILE *in = fopen("1.in", "r");
	FILE *out = fopen("output.txt", "w");
	int t, i, n, sum=0, addK=0, q;
	string str;
    fscanf(in, "%d", &t);
  	for (q=1;q<=t; q++) 
	{
		sum=0;
		addK=0;
		fscanf(in, "%d", &n);
		char ch;
		i=0;
		while (fscanf(in, "%c", &ch) && ch!='\n')
		{
			if (ch!='0' && ch!=' '){
				if (sum>=i) sum+=ch-'0';
				else{
					addK+=i-sum;
					sum=i;
					sum+=ch-'0';
				}
			}
			if (ch!=' ') i++;
		}
    	fprintf(out, "Case #%d: %d\n", q, addK);
  	}
	fclose(in);
    fclose(out);
return(0);
}

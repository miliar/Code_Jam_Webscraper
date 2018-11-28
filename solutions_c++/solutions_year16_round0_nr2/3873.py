#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	 char str[128];
	 int num;
	 scanf("%d", &num);
	 int casenum = 0;

	 for(int i=0;i<num;i++)
	 {

	 	for(int j=0;j<128;j++) str[j] = '\0';
	 	scanf("%s", str);
	 	int length = strlen(str);
	 	int seg = 0;
	 	int last = 0;
	 	for(int i=1;i<length;i++)
	 	{
	 		if(str[i] != str[i-1])
	 			seg ++;
	 	}
	 	if(str[length-1]  == '-')
	 		last = 1;

	 	casenum++;
	 	printf("Case #%d: %d\n",casenum,seg+last);
	 }
}
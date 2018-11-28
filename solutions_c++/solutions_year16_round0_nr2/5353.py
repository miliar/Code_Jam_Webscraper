#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int main()
{
	FILE* In=fopen("B.in","r");if(!In) return 1;
	FILE* Out=fopen("B.res","w");if(!Out) return 2;

	int nCount;
	char str[101];

	fscanf(In,"%d",&nCount);
	for(int i=0;i<nCount;i++)
	{
		fprintf(Out,"Case #%d: ",i+1);
		fscanf(In,"%s",str);

		int nL=strlen(str);
		char cur=str[0];
		int Total=0;

		for(int j=1;j<nL;j++)
		{
			if(cur!=str[j]) {cur=str[j];Total++;}
		}

		if(cur=='-') Total++;
		fprintf(Out,"%d\n",Total);
	};
	fclose(In);
	fclose(Out);
	return 0;
}
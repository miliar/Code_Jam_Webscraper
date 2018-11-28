#include <stdio.h>
#include <stdlib.h>
#include <string>

void main()
{
	FILE *f=fopen("../B-large.in","r");
	if (!f) {
		return;
	}
	int numTasks;
	fscanf(f,"%d",&numTasks);
	char *line;
	line=(char*)malloc(sizeof(char)*102);
	for (int i=0;i<numTasks;i++) {
		fscanf(f,"%s",line);
		int numChars=strlen(line), numSwaps=0;
		char lastChar=line[0];
		for (int j=1;j<numChars;j++) {
			if (line[j]!=lastChar) {
				numSwaps++;
				lastChar=line[j];
			}
		}
		if (lastChar=='-') {
			numSwaps++;
		}
		printf("Case #%d: %d\n",i+1,numSwaps);
	}
}

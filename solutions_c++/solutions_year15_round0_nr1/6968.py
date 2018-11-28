/** @file pat-qualification-a.cpp
  * @author Patrick Lewis
  * @date 2015/04/10
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int ComputeClappers(int*, int, int, int, int&);

int clapperCount;

int main(int argc, char *argv[])
{
    char *fileToUse, *workingPtr, lineBuffer[2048], inputFile[] = "A-small-attempt0.in", countString[2] = {0, 0}, shyLevelCount[5] = {0, 0, 0, 0, 0};
    FILE *datFile;

    int targetLines, targetShyness, linesRan = 0, shynessRan, caseNumber=1, inviteCount;
    int *shyBuffer;

    (argc < 2) ? fileToUse = inputFile : fileToUse = argv[1];

    // open file
    if((datFile = fopen(fileToUse, "r")) == NULL)
    {
	fprintf(stderr, "failed to open file: %s\n", fileToUse);
	return 1;
    }

    // failed to read anything for whatever reason
    if(fgets(lineBuffer, 2048, datFile) == NULL)
    {
	fprintf(stderr, "nothing could be read\n");
	goto END;
    }
    
    targetLines = atoi(lineBuffer);

    // parse file
    while(!feof(datFile))
    {
	clapperCount = 0;
	memset(lineBuffer, 0, 2048);
	if(fgets(lineBuffer, 2048, datFile) == NULL)
	    break;

	workingPtr = strchr(lineBuffer, ' ');
	memset(shyLevelCount, 0, 5);
	strncpy(shyLevelCount, lineBuffer, workingPtr - lineBuffer);
	shyLevelCount[4] = 0;
	targetShyness = strtol(shyLevelCount, NULL, 10);

	//if((targetShyness > 0) && (targetShyness < 1001))
	//  printf("targetShyness: %d\n", targetShyness);
	  
	targetShyness++;
	workingPtr++;
	shyBuffer = new int[targetShyness];

	for(int i=0; i<targetShyness; i++)
	{
	    strncpy(countString, workingPtr++, 1);
	    countString[1] = 0;	    
	    shyBuffer[i] = atoi(countString);
	}

	inviteCount = 0;
	if((shynessRan = ComputeClappers(shyBuffer, 0, targetShyness, 0, inviteCount)) != (targetShyness))
	    printf("shynessRan differs from targetShyness: %d : %d\n", shynessRan, targetShyness);

	linesRan++;

	delete[] shyBuffer;

	printf("Case #%d: %d\n", caseNumber++, inviteCount);
    }

    if(linesRan != targetLines)
	printf("linesRan differs from targetLines: %d : %d\n", linesRan, targetLines);

END:
    fclose(datFile);
    return 0;
}


int ComputeClappers(int *array, int index, int size, int accumulator, int &inviteCount)
{
    // done
    if(index == size)
	return accumulator;

    // add clappers as necessary
    if(clapperCount < index)
    {
	int diff = index - clapperCount;
	//printf("Invite clappers: %d\n", diff);
	inviteCount += diff;
	clapperCount += diff;
    }

    clapperCount += array[index];
    return ComputeClappers(array, index + 1, size, ++accumulator, inviteCount);
}

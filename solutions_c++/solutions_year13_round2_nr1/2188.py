#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;



int did(vector<int>* pStk, int currentMote, int ptr)
{
	if(ptr == (*pStk).size()) return 0;

	int absortMote = (*pStk)[ptr];
	//printf("ptr:%d %d\n",ptr,absortMote);

	if(absortMote < currentMote ) return did(pStk, currentMote+absortMote, ptr+1);

	else {
		int addmote = 99999, delmote;
		if(currentMote!=1) addmote = did(pStk, currentMote+currentMote-1, ptr) + 1;
		delmote = did(pStk, currentMote, ptr+1) + 1;
		//printf("separate: %d %d\n", addmote, delmote);
		return (addmote<delmote) ? addmote : delmote;
	}
}

int main()
{
	FILE *fp, *fop;
	int testCast, mainMote, moteNumber;
	int motes;
	vector<int> stk;

	fp = fopen("input.txt","r");
	fop = fopen("output.txt","w");
	
	fscanf(fp,"%d",&testCast);
	//printf("%d\n",testCast);

	for(int i=1;i<=testCast;i++) {
		fscanf(fp,"%d %d",&mainMote, &moteNumber);
		//printf("%d %d\n",mainMote, moteNumber);
		for(int j=0;j<moteNumber;j++) {
			fscanf(fp, "%d", &motes);
			if(motes < mainMote) mainMote+=motes;
			else stk.push_back(motes);
		}
		sort(stk.begin(),stk.end());

		fprintf(fop,"Case #%d: %d\n",i,did(&stk, mainMote, 0));

		stk.clear();
	}
	//getchar();
	//getchar();

	fclose(fp);
	fclose(fop);
	return 0;
}
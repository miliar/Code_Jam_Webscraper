#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<math.h>
#include<stdlib.h>
using namespace std;

map<int,bool> myMap;

bool isPalindrome(int A)
{
	char str[11]={0,};
	sprintf(str,"%d",A);
	int digit = strlen(str);

	if(digit==1)
		return true;

	int i=0;
	digit--;
	while(i<digit)
	{
		if(str[i++]!=str[digit--])
			return false;
	}
	return true;
}

void createMap(int A, int B)
{
	int upper = sqrt(B);
	for(int i=A;i<=upper;i++)
		if(isPalindrome(i)==true and isPalindrome(i*i)==true && i*i<=B)
			myMap[i*i]=true;
}

void solve(int t, int A, int B)
{
	FILE * fpOut = fopen("/Users/adarshkumarsharma/cpp/Code/CodeJam/FairAndSquare/src/C-small-attempt0.out","a+");
	map<int,bool>::iterator it;
	int count=0;
	for(it=myMap.begin();it!=myMap.end();it++)
	{
		if(it->first>B)
			break;

		if(it->first>=A)
			count++;
	}

	fprintf(fpOut,"Case #%d: %d\n",t,count);
	fclose(fpOut);
}


int main()
{
	createMap(1,1000);
	FILE * fpIn = fopen("/Users/adarshkumarsharma/cpp/Code/CodeJam/FairAndSquare/src/C-small-attempt0.in","r");
	int T;
	fscanf(fpIn,"%d",&T);

	for(int t=0;t<T;t++)
	{
		int A,B;
		fscanf(fpIn,"%d %d", &A, &B);
		solve(t+1,A,B);
	}

	fclose(fpIn);

}




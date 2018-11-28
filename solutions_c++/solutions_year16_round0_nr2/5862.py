
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

using namespace std;


int ProcessInput();
char S[101];
char st, cur;
int Len, i, flip_count;

int main()
{

	int testcases, i;

	cin >> testcases;

	for(i=0; i < testcases; i++) {
		cout<<"Case #"<<i + 1<<": ";
		ProcessInput();
	}

return 0;
}

 
int ProcessInput()
{
cin >> S; 
Len = strlen(S);

i = 0;
st = S[i];
flip_count = 0;

while(i < Len)
{
	i ++;
	if(i == Len) 
		break;
	cur = S[i];
	if(st == cur)
		continue;
	else
	{
		flip_count ++;
		st = cur;
	}
}
if( st == '-') flip_count ++;
cout <<flip_count<<endl;

return 0; 
}


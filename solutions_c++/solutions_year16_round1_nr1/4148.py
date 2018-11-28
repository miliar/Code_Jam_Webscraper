
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string.h>

using namespace std;

char S[1001];
char LastWord[2002];
int Length, i, first, last;

int ProcessInput();

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
Length = strlen(S);

 
first = 1000;
last = 1000;
LastWord[first] = S[0];
LastWord[last] = S[0];
for(i=1; i < Length; i++) {
	if(S[i] - LastWord[first] >= 0) {
		first --;
		LastWord[first] = S[i];
	}
	else {
		last ++;
		LastWord[last] = S[i];
	}
}

for(i=first; i <=last; i++)
	cout<<LastWord[i];
cout<<endl;

return 0; 
}


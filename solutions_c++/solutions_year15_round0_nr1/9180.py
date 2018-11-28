
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
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

#define MAXSHY 1000 
int Smax;
char str[MAXSHY +1];
int alreadyStanding;
int invite;
int k;
int add;

int ProcessInput()
{


cin >> Smax;
cin >> str;

alreadyStanding = 0;
invite = 0;

for(int k=0; k<=Smax; k++)
{
	add = str[k] - '0';
	if( add == 0)
		continue;

	if(alreadyStanding < k) { 
		invite += k-alreadyStanding;
		alreadyStanding = k;
	}

	alreadyStanding += add;
}
cout << invite << endl;
return 0;

}


#include<iostream>
#include <stdio.h>
#include<stdlib.h>
#include<stack>
#include<map>
#include<vector>
#include<list>
#include<limits.h>
#include<string.h>
#include <algorithm>
using namespace std;
int main() {

int arr1[4][4], arr12[4][4], flag, sec, i, j, k, t,n,m;
cin >> t;
for(m=1;m<=t;m++)
{
n = 0;
cin >> flag;


for(i=0; i<4; i++)
{
for(j=0; j<4;j++)
{
cin >> arr1[i][j];
}
}
cin >> sec;



for(i=0; i<4; i++)
{
for(j=0; j<4;j++)
{
cin >> arr12[i][j];
}
}

for (i = 0; i<4; i++)
{
for (j = 0; j<4; j++)
{
if (arr1[flag - 1][i] == arr12[sec - 1][j])
{
n++; k = arr1[flag - 1][i];
break;
}
}
}
cout << "Case #" << m << ": ";
switch (n)
{
case 0: cout << "Volunteer cheated!"; break;
case 1: cout << k; break;
default: cout << "Bad magician!";
}
cout << endl;
}
return 0;
}

#include <iostream>
using namespace std;
 
int main() {

int arr[4][4], brr[4][4], first, sec, i, j, k, t,n,m;
cin >> t;
for(m=1;m<=t;m++)
{
n = 0;
cin >> first;


for(i=0; i<4; i++)
{
for(j=0; j<4;j++)
{
cin >> arr[i][j];
}
}
cin >> sec;



for(i=0; i<4; i++)
{
for(j=0; j<4;j++)
{
cin >> brr[i][j];
}
}

for (i = 0; i<4; i++)
{
for (j = 0; j<4; j++)
{
if (arr[first - 1][i] == brr[sec - 1][j])
{
n++; k = arr[first - 1][i];
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
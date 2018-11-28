#include <fstream>
#include <iostream>
using namespace std;

ifstream fin("data.txt");

int main() {
int N;
int r1 = 0, r2 = 0;
int a[4];
int b[4];
int dumb = 0;

fin >> N;
int tc = 1,i=1, j=1,k=1;
for (tc = 1; tc <= N; tc++) {
	fin >> r1;
	for(i  = 1; i <= 16; i++) { 
		fin >> dumb;
		if(i == (r1-1)*4+1) a[1] = dumb;
		if(i == (r1-1)*4+2) a[2] = dumb;
		if(i == (r1-1)*4+3) a[3] = dumb;
		if(i == (r1-1)*4+4) a[4] = dumb;
	}

	fin >> r2;
	for(i  = 1; i <= 16; i++) { 
		fin >> dumb;
		if(i == (r2-1)*4+1) b[1] = dumb;
		if(i == (r2-1)*4+2) b[2] = dumb;
		if(i == (r2-1)*4+3) b[3] = dumb;
		if(i == (r2-1)*4+4) b[4] = dumb;
	}
for (i = 1; i <= 4; i++) {
// cout << a[i] << " " << b[i] << endl;
}
int count = 0;
int ans = 0;
for (int f = 1; f <= 4; f++)
  for (int k = 1; k <=4; k++)
{
	if(a[f] == b[k]) {count++; ans = a[f];}
}
if (count == 1)
cout << "Case #" << tc << ": " << ans << endl;
else if (count > 1)
cout << "Case #" << tc << ": " << "Bad magician!" << endl;
else 
cout << "Case #" << tc << ": " << "Volunteer cheated!" << endl;
}
return 0;
}

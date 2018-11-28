#include <fstream>
#include <iostream>
using namespace std;

ifstream fin("test.in");

int main() {
int N, ans1 = 0, ans2 = 0;
int a[4];
int b[4];
int temp = 0;

fin >> N;
int n = 1,i=1, j=1,k=1;
for (n = 1; n <= N; n++) {
	fin >> ans1;
	for(i=1; i <= 16; i++) { 
		fin >> temp;
		for(j = 1; j <=4; j++)
		if(i == (ans1-1)*4+j) a[j] = temp;
	}
	fin >> ans2;
	for(i=1; i <= 16; i++) { 
		fin >> temp;
		for(j = 1; j <=4; j++)
		if(i == (ans2-1)*4+j) b[j] = temp;
	}

int cc = 0;
int ans = 0;
for (i = 1; i <= 4; i++)
  for (j = 1; j <=4; j++)
	if(a[i] == b[j]) {cc++; ans = a[i];}

if (cc == 1)
cout << "Case #" << n << ": " << ans << endl;
else if (cc > 1)
cout << "Case #" << n << ": " << "Bad magician!" << endl;
else 
cout << "Case #" << n << ": " << "Volunteer cheated!" << endl;
}
return 0;
}

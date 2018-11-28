#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <list>
#include <vector>
#ifdef __linux
#include <stdint.h>
#else
#include <cstdint>
#include <windows.h>
#endif
using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void t1(int seq)  {
	int a,b;
	int s[8]={0};
	int x[4][4]={0};
	int i(0),j(0);
	cin>>a;a--;
	for (i=0;i<4;++i)
		for (j=0;j<4;++j)
			cin>>x[i][j];
	for (i=0;i<4;++i)
		s[i]=x[a][i];
	
	cin>>b; b--;
	for (i=0;i<4;++i)
		for (j=0;j<4;++j)
			cin>>x[i][j];
	for (i=0;i<4;++i)
		s[i+4]=x[b][i];

	qsort (s, 8, sizeof(int), compare);

	for (j=-1,i=0;i<7;++i)
		if (s[i]==s[i+1])
			if (j==-1) j=i;
			else {cout<<"Case #"<<seq<<": Bad magician!\n"; return;}
	if (j==-1)
		cout<<"Case #"<<seq<<": Volunteer cheated!\n";
	else
		cout<<"Case #"<<seq<<": "<<s[j]<<endl;
	return;
}

int main()  {
	int n;
	cin>>n;
	for (int i(0);i<n;++i)
		t1(i+1);
	
	return 0;
}

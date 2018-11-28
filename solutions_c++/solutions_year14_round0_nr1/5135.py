#include <stdio.h>
#include <iostream>
#include <cmath>
#include <fstream>
#define lldd long long int
using namespace std;
void input(int a[])
{
	for(int i=0;i<4;i++)
		scanf("%d",&a[i]);
}
int main()
{
int t;
scanf("%d",&t);
ofstream fout;
	fout.open("question1.txt");
for(int i=1;i<=t;i++)
{
	int f,s,ff[4],ss[4],temp[4];
	scanf("%d",&f);
	f--;
	for(int j=0;j<4;j++)
		if(j==f)
			input(ff);
			else
			input(temp);
	scanf("%d",&s);
	s--;
	for(int j=0;j<4;j++)
			if(j==s)
			input(ss);
			else
			input(temp);
			
	int req_no=-1;
	int count=0;
	for(int m=0;m<4;m++)
		for(int n=0;n<4;n++)
			if(ff[m]==ss[n])
			{
				req_no=ff[m];
				count++;
				break;
			}
	
	if(req_no==-1)
		fout<<"Case #"<<i<<": Volunteer cheated!\n";
	else if(count>1)
		fout<<"Case #"<<i<<": Bad magician!\n";
	else
		fout<<"Case #"<<i<<": "<<req_no<<endl;
}
return 0;	
}
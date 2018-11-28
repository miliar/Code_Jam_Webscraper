/*
	Author: Zhaohai Nathaniel Lee <Nathanielben@gmail.com> @ inspiratune.com
*/

// Include the header files
#include <fstream>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdbool>

//Set the namespace
using namespace std;

#define IN "A-small-attempt6.in"
#define OUT "out"

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int i,j,n,m,t,sum,p,
	a[10][10],b[10][10];
bool c[20];

int pre()
{
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	memset(c,0,sizeof(c));
	sum=0;
	return 0;
}

int init()
{
	scanf("%d",&n);

	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		scanf("%d",&a[i][j]);

	scanf("%d",&m);

	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		scanf("%d",&b[i][j]);

	return 0;
}

int main (int argc, char const *argv[])
{
	ifstream cin (IN);
	ofstream cout (OUT);
	freopen (IN, "r", stdin);
	freopen (OUT, "w", stdout);
	int casi;
	scanf("%d",&t);
for(casi=1;casi<=t;casi++)
{
	pre();
	init();
	for(i=1;i<=4;i++)
	c[a[n][i]]=true;
	for(i=1;i<=4;i++)
	if(c[b[m][i]])
	{
		sum++;
		p=b[m][i];
	}
	if(sum==1) printf("Case #%d: %d\n",casi,p);
	else if(sum==0) printf("Case #%d: Volunteer cheated!\n",casi);
	else printf("Case #%d: Bad magician!\n",casi);

}
	fclose (stdin);
	fclose (stdout);
	cin.close ();
	cout.close ();
	return 0;
}
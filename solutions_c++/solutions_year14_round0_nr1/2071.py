#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cctype>
#include <ctime>
#include <strstream>
#define min(a,b) ((a) < (b) ? (a) : (b)) 
#define max(a,b) ((a) > (b) ? (a) : (b)) 
using namespace std;
int m1[4][4],m2[4][4];
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int ki,i,j,s,r;
	int a1,a2;
	scanf("%d",&cas);
	for(ki=1;ki<=cas;ki++)
	{
		printf("Case #%d: ",ki);
		cin>>a1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>m1[i][j];
		cin>>a2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>m2[i][j];
		a1--;
		a2--;
		s=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(m1[a1][i]==m2[a2][j])
				{
					s++;
					r=m1[a1][i];
				}
		if(!s)puts("Volunteer cheated!");
		else if(s==1)cout<<r<<endl;
		else puts("Bad magician!");
	}
	return 0;
}
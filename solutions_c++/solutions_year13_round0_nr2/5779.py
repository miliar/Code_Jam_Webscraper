#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{

freopen("B-large.in","r",stdin);
freopen("BB.out","w",stdout);
long t,i,j,k,n,m,MAT[100][100],value;

bool Pos=true,col,row;

cin>>t;

for(long cas=0;cas<t;cas++)
{

	cin>>n>>m;
for(i=0;i<n;i++)
	for(j=0;j<m;j++)
		cin>>MAT[i][j];

Pos =true;
for(i=0;i<n && Pos;i++)
	for(j=0;j<m;j++)
	{
		value=MAT[i][j];
		col=false;
		for(k=0;k<n;k++)
		if(value<MAT[k][j])
		col=true;

		row=false;

		for(k=0;k<m;k++)
			if(value<MAT[i][k])
				row=true;
		if(col && row)
		{ 
			Pos=false; 
			break;
		}
	}

if(Pos)
	printf("Case #%d: YES\n",cas+1);
else
	printf("Case #%d: NO\n",cas+1);

}

return 0;
}
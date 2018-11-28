#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
int T;
int a[4][4], b[4][4],ans1,ans2,val,ans[101];

cin>>T;
for(int m=0;m<T; m++)
{
int cnt =0;
val = 0;
	cin>>ans1;
	ans1-=1;
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	cin>>a[i][j];

	cin>>ans2;
	ans2-=1;
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	cin>>b[i][j];

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(a[ans1][i] == b[ans2][j])
			{
			val = a[ans1][i];
			cnt++;
			break;
			}
		}
	}
if(cnt == 0)
ans[m]=17;
else if(cnt == 1)
ans[m]=val;
else
ans[m]=18;
}

for(int i=0;i<T;i++)
{
if(ans[i]<=16)
cout<<"Case #"<<(i+1)<<": "<<ans[i]<<"\n";
else if(ans[i]==17)
cout<<"Case #"<<(i+1)<<": Volunteer cheated!\n";
else
cout<<"Case #"<<(i+1)<<": Bad magician!\n";
}
return 0;
}

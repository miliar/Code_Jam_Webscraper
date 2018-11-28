#include <iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

int main() {
	// your code goes here
int test,ca=0,n,m,i,j,count=0;
vector<int>v1,v2;
cin>>test;
while(test--)
{
v1.clear();
v2.clear();
 count=0;
cin>>m;
int a[4][4];
for(i=0;i<4;i++)
for(j=0;j<4;j++)
cin>>a[i][j];
for(i=0;i<4;i++)
v1.push_back(a[m-1][i]);
cin>>m;
int b[4][4];
for(i=0;i<4;i++)
for(j=0;j<4;j++)
cin>>b[i][j];
for(i=0;i<4;i++)
v2.push_back(b[m-1][i]);
//sort(v1.begin(),v1.end());
//sort(v2.begin(),v2.end());
//for(i=0;i<v1.size();i++)
//cout<<v1[i];
//cout<<endl;
//for(i=0;i<v2.size();i++)
//cout<<v2[i];
//cout<<endl;
int temp=0;;
for(i=0;i<v1.size();i++)
{
for(j=0;j<v2.size();j++)
{
if(v1[i]==v2[j])
{
temp=v1[i];
++count;
}
}

}
if(count==1)
printf("Case #%d: %d\n",++ca,temp);
else if(count>1)
printf("Case #%d: Bad magician!\n",++ca);
else if(count==0)
printf("Case #%d: Volunteer cheated!\n",++ca);
}

	return 0;
}

#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;
map<int,int> mp;
int main() {
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++)
	{
		mp.clear();
		int f,s;
		int a[4][4],b[4][4];
		scanf("%d",&f);
		for(int l=0;l<4;l++)
			for(int j=0;j<4;j++)
			{
				scanf("%d",&a[l][j]);
				if(l==f-1)
					mp[a[l][j]]++;
			}
		scanf("%d",&s);
		int count=0,temp;
		for(int l=0;l<4;l++)
			for(int j=0;j<4;j++)
			{
				scanf("%d",&b[l][j]);
				if(l==s-1)
				{
					if(mp.count(b[l][j])!=0)
					{
						count++;
						temp=b[l][j];
					}
				}	
			}
		printf("Case #%d: ",i);
		if(count==0)
			printf("Volunteer cheated!\n");
		else if(count>1)
			printf("Bad magician!\n");
		else if(count==1)
			printf("%d\n",temp);
			
	}
	return 0;
}

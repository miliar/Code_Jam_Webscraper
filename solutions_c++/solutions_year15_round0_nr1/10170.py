#include <bits/stdc++.h>
using namespace std;

int main() {
	char str[1005];
	int t,stn,max,i,fr,j;
	scanf("%d",&t);
	j=1;
	while(t--){
		scanf("%d %s",&max,str);
		stn=str[0]-'0';
		fr=0;
		
		for(i=1;i<=max;i++)
		{
			if(stn<i)
			{
				fr=fr+(i-stn);
				stn=stn+(str[i]-'0')+(i-stn);
				//printf("%d ",fr);
			}
			else
			{
				stn=stn+(str[i]-'0');
			}
		}
		printf("Case #%d: %d\n",j,fr);
		j++;
	}
	return 0;
}
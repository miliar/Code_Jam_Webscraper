#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int main()
{
	int	n,i=0,j,index = 0,R;
    freopen("g:/input.txt","r",stdin);
    freopen("g:/output.txt","w",stdout);
	cin>>n;
	double b[1005],c[1005];
	bool b_ex[1005],c_ex[1005];
	while(n--)
	{
		cin>>R;
		for(i=0;i<R;i++)
			cin>>b[i];

		for(i=0;i<R;i++)
			cin>>c[i];

		sort(b,b+R);
		sort(c,c+R);
		memset(b_ex,true,sizeof(b_ex));
		int naomi_dwar = 0,ken_dwar=0;

		for(i=0 ; i<R ;)
		{
			for(j=0 ; j<R ; j++)
			{
				if(b_ex[j])
				{
					if(b[j] > c[i])
					{
					b_ex[j] = false;
					naomi_dwar++;
					i++;
					break;
					}
				}
			}
			if(j == R)
				i=R;
		}
        ken_dwar= R - naomi_dwar;

		int naomi_war = 0,ken_war = 0;
		memset(c_ex,true,sizeof(c_ex));
		for(j=0 ; j<R ; )//naomi
		{
			for(i=0 ; i<R ;i++)//ken
			{
				if(c_ex[i])
				{
					if(b[j] < c[i])
					{
					c_ex[i] = false;
					ken_war++;
					j++;
					break;
					}
				}
			}
			if(i == R)
				j=R;
		}
naomi_war = R - ken_war;
			printf("Case #%d: ",++index);
			printf("%d %d\n",naomi_dwar,naomi_war);
	}
	return 0;
}

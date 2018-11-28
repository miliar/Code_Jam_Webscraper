#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int main()
{
	int t, r[16], v[16], res[100], r0, r1, i, j, flag[100], k;
	cin>>t;
	if(t<1 || t>100)
		exit(0);
	for(i=0;i<t;i++)
	{	flag[i]=0;
		cin>>r0;
		for(j=0;j<16;j+=4)
			scanf("%d %d %d %d", &r[j], &r[j+1], &r[j+2], &r[j+3]);
		cin>>r1;
		for(j=0;j<16;j+=4)
			scanf("%d %d %d %d", &v[j], &v[j+1], &v[j+2], &v[j+3]);
		if(r0>4||r0<1||r1>4||r1<1)
			exit(0);
		for(j=0;j<16;j++)
			if(r[j]<1||r[j]>16||v[j]<1||v[j]>16)
				exit(0);	
		for(j=1;j<5;j++)
		{
			for(k=1;k<5;k++)
			{
				if(r[(r0*4)-j]==v[(r1*4)-k])
				{
					flag[i]++;
					res[i]=r[(r0*4)-j];
				}
			}
		}
	}
	for(i=0;i<t;i++)
	{
		if(flag[i]==0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if(flag[i]==1)
			cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
		else
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
	return 0;
}

			

#include<bits/stdc++.h>
using namespace std;
int a,b,c,halo[1000],hasil[10];
char arr[1000];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("outputlargea","w",stdout);
	scanf("%d",&a);
	for(int d=1;d<=a;d++)
	{
		memset(halo,0,sizeof(halo));
		memset(hasil,0,sizeof(hasil));
		scanf("%s",&arr);
		for(int e=0;e<=strlen(arr)-1;e++)
		{
			halo[arr[e]]++;
			//printf("%d",arr[e]);
		}
		//printf("%d",halo['z']);
		///*		
		//printf("%d %d %d %d",halo['T'],halo['H'],halo['R'],halo['E']);
		hasil[0]=halo['Z'];
		//printf("%d",hasil[0]);
		hasil[2]=halo['W'];
		hasil[4]=halo['U'];
		hasil[6]=halo['X'];
		hasil[8]=halo['G'];
		halo['O']=halo['O']-halo['Z']-halo['W']-halo['U'];
		halo['E']=halo['E']-halo['Z']-halo['G'];
		halo['R']=halo['R']-halo['Z']-halo['U'];
		halo['T']=halo['T']-halo['W']-halo['G'];
		halo['F']=halo['F']-halo['U'];
		halo['S']=halo['S']-halo['X'];
		halo['I']=halo['I']-halo['X']-halo['G'];
		halo['H']=halo['H']-halo['G'];
		//printf("%d %d %d %d",halo['T'],halo['H'],halo['R'],halo['E']);
		hasil[1]=halo['O'];
		halo['O']=0;
		halo['N']=halo['N']-halo['O'];
		halo['E']=halo['E']-halo['O'];
		//printf("%d %d %d %d",halo['T'],halo['H'],halo['R'],halo['E']);
		hasil[5]=halo['F'];
		halo['I']=halo['I']-halo['F'];
		halo['V']=halo['V']-halo['F'];
		halo['E']=halo['E']-halo['F'];
		//printf("%d %d %d %d",halo['T'],halo['H'],halo['R'],halo['E']);
		hasil[9]=halo['I'];
		halo['N']=halo['N']-2*halo['I'];
		halo['E']=halo['E']-halo['I'];
		//printf("%d %d %d %d",halo['T'],halo['H'],halo['R'],halo['E']);
		hasil[7]=halo['V'];
		halo['E']=halo['E']-2*halo['V'];
		halo['S']=halo['S']-halo['V'];
		halo['N']=halo['N']-halo['V'];
		hasil[3]=halo['R'];
		halo['T']=hasil['T']-hasil['R'];
		halo['H']=hasil['H']-hasil['R'];
		halo['E']=hasil['E']-hasil['R'];
		//printf("%d %d %d %d",halo['T'],halo['H'],halo['R'],halo['E']);
		//printf("%d",hasil[3]);
		int n;
		printf("Case #%d: ",d);
		for(int g=0;g<=9;g++)
		{
			n++;
			if (hasil[g]!=0)
			{
				for(int v=1;v<=hasil[g];v++)
				{
					printf("%d",g);	
				}
			}
				
		}
		printf("\n");
		//*/
	}
}

#include<string.h>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
int main(){
	freopen("D:\\Users\\Song\\Downloads\\Code\\input.txt","r",stdin);
	freopen("D:\\Users\\Song\\Downloads\\Code\\output.txt","w",stdout);
	int T,count=0;
	scanf("%d",&T);
	int N,i,j,lk,k,flag,total;
	char table[128][128];
	int tablen[128][128];
	int min[128],max[128];
	char dict[128];
	//
	for(count=1;count<=T;count++){
		for(i=0;i<128;i++)
			for(j=0;j<128;j++){
				tablen[i][j]=0;
				}
		scanf("%d",&N);
		for(i=0;i<N;i++)
			scanf("%s",table[i]);
		//
		flag=0;
		lk=k=0;
		for(i=0;i<N;i++)
		{
			lk=k;
			k=0;
			for(j=0;j<strlen(table[i]);j++)
			{
				if(j!=0&&table[i][j]!=table[i][j-1])
				{
					k++;
				}
				if(i!=0&&table[i][j]!=dict[k])
				{
					flag=1;
				}
				tablen[i][k]++;
				dict[k]=table[i][j];
			}	
			if(i!=0&&k!=lk)
				flag=1;
		}

		printf("Case #%d: ",count);
		if(flag==1)
		{
			printf("Fegla Won\n");
			continue;
		}
		for(i=0;i<128;i++)
		{
			min[i]=500;
			max[j]=0;
		}
		for(i=0;i<=k;i++)
		{
			for(j=0;j<N;j++){
				if(min[i]>tablen[j][i])
					min[i]=tablen[j][i];
				if(max[i]<tablen[j][i])
					max[i]=tablen[j][i];
			}
		}
		total=0;
		int tmp=0;
		int tmin=500;
		for(i=0;i<=k;i++)
		{
			tmin=500;
			for(int l=min[i];l<=max[i];l++){
				tmp=0;
				for(j=0;j<N;j++)
				{
					if(tablen[j][i]>l)
						tmp+=(tablen[j][i]-l);
					else
						tmp+=(l-tablen[j][i]);
				}
				if(tmin>tmp)
					tmin=tmp;
			}
			total+=tmin;
		}

		printf("%d\n",total);

	}
	return 0;
}
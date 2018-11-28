#include<cstdio>
#include<cstdlib>
#include<cstring>
struct Card
{
	int fr,sr;
}card[16];
int main()
{
	int T,fr,sr,count;
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int ri=0;ri<T;ri++)
	{
		memset(card,0,sizeof(card));
		scanf("%d",&fr);
		for (int i=0;i<4;i++)
		 for (int j=0;j<4;j++)
		 {
			int tmp;
			scanf("%d",&tmp);
			if (i+1==fr)
			card[tmp-1].fr=1;
		 }
		scanf("%d",&sr);
		for (int i=0;i<4;i++)
		 for (int j=0;j<4;j++)
		 {
			int tmp;
			scanf("%d",&tmp);
			if (i+1==sr)
			card[tmp-1].sr=1;
		 }
		count=0;
		for (int i=0;i<16;i++)
		if (card[i].fr==1&&card[i].sr==1)
		count++;
		if (count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",ri+1);
			continue;
		}
		else
		if (count>1)
		{
			printf("Case #%d: Bad magician!\n",ri+1);
			continue;
		}
		else
		{
			for (int i=0;i<16;i++)
			if (card[i].fr==1&&card[i].sr==1)
			printf("Case #%d: %d\n",ri+1,i+1);
		}
	}
	return 0;
//	fclose(stdin);
//	fclose(stdout);
}

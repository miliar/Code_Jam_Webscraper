#include <stdio.h>
#include <string.h>
#include <malloc.h> 

struct First
{
	int anwser1;
	int firstarr[4][4];
	struct First *next;
};

struct Second
{
	int anwser2;
	int secondarr[4][4];
	struct Second *next;
};

First* InitFirstNode()
{
	First *Pointer;
	Pointer = (First*)malloc(sizeof(First));
	for (int n = 0;n<4;n++)
	{
		for (int m = 0;m<4;m++)
		{
			Pointer->firstarr[n][m]=0;
		}
	}
	return Pointer;
}

Second* InitSecondNode()
{
	Second *Pointer;
	Pointer = (Second*)malloc(sizeof(Second));
	return Pointer;
}


void main()
{


	FILE *fp1,*fp2;
	int count;
	int test[17];
	fp1 = fopen("input.txt","r");
	fscanf(fp1,"%d",&count);
	int *point;
	point = new int[count*34];
	for (int i=0;i<count*34;i++)
	{
		fscanf(fp1,"%d",point+i);
//		printf("%d\n",*(point+i));
	}

	First *p,*hp;
	Second *q,*hq;

	hp=p=InitFirstNode();
	hq=q=InitSecondNode();
	p->next=NULL;
	q->next=NULL;

	for (int k=0;k<count*34;)
	{
		
		if ((k%34)<17)
		{
			p=p->next=InitFirstNode();
			p->anwser1=point[k++];

			for (int n = 0;n<4;n++)
			{
				for (int m = 0;m<4;m++)
				{
					p->firstarr[n][m]=point[k+n*4+m];
				}
			}
			k+=16;

		}
		else
		{
			q=q->next=InitSecondNode();

			q->anwser2=point[k++];

			for (int n = 0;n<4;n++)
			{
				for (int m = 0;m<4;m++)
				{
					q->secondarr[n][m]=point[k+n*4+m];
				}
			}
			k+=16;

		}
		p->next=NULL;
		q->next=NULL;
		//			printf("This is %d\n",k);
		
	}

	p=hp->next;
	q=hq->next;
	fclose(fp1);

	fp2 = fopen("black.txt","w");
	int t=0;
	while(p&&q)
	{
		t++;
		bool bad=true;
		int result[4]={0};

		for (int i = 0;i<4;i++)
		{
			result[i]=p->firstarr[p->anwser1-1][i];
		}
		//for (int i = 0;i<4;i++)
		//{
		//	for (int k = 0;k<4;k++)
		//	{
		//		if ((p->firstarr[i][k]) - (q->secondarr[i][k]))
		//			bad=false;
		//	}
		//}
		//if (bad)
		//{
		//	fprintf(fp2,"Case #%d:Bad magician!",t);
		//}

		int coef=0;
		int j;
		int i;
		int para;
		bool right = true;
		for (i = 0;i<4;i++)
		{	
				
			for (j=0;j<4;j++)
			{
				if (!(q->secondarr[q->anwser2-1][i]-result[j]))
				{
//					fprintf(fp2,"Case #%d: %d\n",t,result[j]);
					para=result[j];
					coef++;
					right = false;						
				}
			}

		}


		if((coef-1)&&coef>0)
		{
			fprintf(fp2,"Case #%d: Bad magician!\n",t);			
		}
		else if(!(coef-1))
		{
			fprintf(fp2,"Case #%d: %d\n",t,para);
		}
		//if(coef>1)
		//{
		//	fprintf(fp2,"Case #%d: Bad magician!",t);
		//	break;
		//}
		else if (!coef)
		{
			fprintf(fp2,"Case #%d: Volunteer cheated!\n",t);
		}


		p = p->next;
		q = q->next;
		printf("this is %d\n",t);
	}
	fclose(fp2);

}
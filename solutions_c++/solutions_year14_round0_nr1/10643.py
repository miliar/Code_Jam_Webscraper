#include<stdio.h>
#include<conio.h>
void main()
{
	int case1, i, j, ans1, ans2, a[4][4], b[4][4];
	int cnt,num,total;
	FILE *ifp, *ofp;

	ifp=fopen("input.txt","r");
	ofp=fopen("output.txt","w");
	fscanf(ifp,"%d",&total);
	for(case1=1; case1<=total; case1++)
	{
	cnt=0;
	num=0;
	fscanf(ifp,"%d",&ans1);
	for (i=0;i<=3;i++)
	for (j=0;j<=3;j++)
	fscanf(ifp,"%d",&a[i][j]);
	fscanf(ifp,"%d",&ans2);
	for (i=0;i<=3;i++)
	for (j=0;j<=3;j++)
	fscanf(ifp,"%d",&b[i][j]);
	for(i=0;i<=3;i++)
	{
	for (j=0;j<=3;j++)
	{
	if(a[ans1-1][i]==b[ans2-1][j])
	{
	cnt=cnt+1;
	num=a[ans1-1][i];
	break;
	}
	}
	}
	if(cnt==1)
	fprintf(ofp,"case #%d: %d\n",case1,num);
	else if (cnt==0)
	fprintf(ofp,"case #%d: Volunteer cheated!\n",case1);
	else if(cnt>1)
	fprintf(ofp,"case #%d: Bad magician!\n",case1);

	}
	getch();
}
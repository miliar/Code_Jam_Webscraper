#include<bits/stdc++.h>
int main()
{
	int i,j,p,d,k,l[21],n,t,T,x,r,c,a[21][21][21];
	l[1]=2;
	l[2]=3;
	l[3]=5;
	l[4]=7;
	l[5]=9;
	l[6]=11;
	l[7]=13;
	l[8]=15;
	l[9]=17;
	l[10]=19;
	l[11]=20;
	l[12]=20;
	l[13]=20;
	l[14]=20;
	l[15]=20;
	l[16]=20;
	l[17]=20;
	l[18]=20;
	l[19]=20;
	l[20]=20;
	for(i=1;i<21;++i)
		for(j=i;j<21;++j)
			for(k=1;k<21;++k)
			{
				d=i*j;
				if(d%k==0 && k<=l[i] && k<=j)
					a[i][j][k]=1;
				else
					a[i][j][k]=0;
			}

	scanf("%d",&T);
	for(t=1;t<=T;++t)
	{
		scanf("%d%d%d",&x,&r,&c);
		i=r<c?r:c;
		j=r>c?r:c;
		r=i;
		c=j;
		d=a[r][c][x];
		if(d==1)
			printf("Case #%d: GABRIEL\n",t);
		else
			printf("Case #%d: RICHARD\n",t);
	}
	return 0;
}

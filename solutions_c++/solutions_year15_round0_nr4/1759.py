#include<stdio.h>
#include<string.h>

int a[4][4][4]={{{1,0,0,0}, //1*1
				{1,1,0,0}, //1*2
				{1,0,0,0},  //1*3
				{1,1,0,0}},  //1*4
				
				{{1,1,0,0}, //2*1
				{1,1,0,0},  //2*2
				{1,1,1,0},   //2*3
				{1,1,0,0}},  //2*4
				
				{{1,0,0,0}, //3*1
				{1,1,1,0}, //3*2
				{1,0,1,0}, //3*3
				{1,1,1,1}},  //3*4
				
				{{1,1,0,0},//1*4
				{1,1,0,0},  //2*4
				{1,1,1,1},  //3*4
				{1,1,0,1}}
				};

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output1.txt","w",stdout);
	int num=0;
	int d,x,y=0;
	scanf("%d",&num);
	for(int i=0;i<num;i++)
    {
	  scanf("%d%d%d",&d,&x,&y);
      if(a[x-1][y-1][d-1]==1)
      {
      	printf("Case #%d: GABRIEL\n",i+1);
      }
      else
      {
      	printf("Case #%d: RICHARD\n",i+1);
      }
	}
	return 0;
}
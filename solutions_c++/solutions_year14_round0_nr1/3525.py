#include <iostream>
#include <fstream>
using namespace std;
#include <stdio.h>
#include <stdlib.h>
#define M 3
#define N 4
 
#include <stdio.h>
#include <stdlib.h>
int insert_sort(int *p, int count)
{
    int i, j, tmp;
    if(p == NULL || count < 0) return 0;    //
    for(i=1; i<count; i++){
        tmp = p[i];
        j = i-1;
        while(tmp<p[j] && j>=0){ // 此处一个空
            p[j+1] = p[j];
            --j;
        }
       p[j+1] = tmp;  // 此处一个空
    }
    return 1;
}
double myabs(double a)
{
	return a>0?a:-a;
}
int myabs(int a)
{
	return a>0?a:-a;
}
double Min9Exp(char *list) // the max length of the expression is 13 
{
	int i,j=0,flag =0,a,b,len=0,as=1,bs=1;
	double difftmp=100000;
	int res=0;
    char tmp;

		a=0;b=0;flag = 0;
		for(j=0;j<13;j++)
		{
			if (flag == 0 && list[j] != '\0')
			{

				if(a==0&&as==1)
				{
					if(list[j] == '-')
					{
						as = -1;
					}
					else
					{
						as = 1;
						a = a*10 + list[j]-'0';
					}

				}
				else
				{
					
					if(list[j] == '+' ||list[j] == '-'||list[j] == '*'||list[j] == '/')
			     	{
						tmp = list[j];
						flag = 1;
						continue;
					}
					else
					{
						a = a*10 + list[j]-'0';
					}
				}
				
			}
			else
			{
				if(b==0 && list[j] != '\0' && bs ==1)
				{
					if(list[j] == '-')
					{
						bs = -1;
					}
					else
					{
						bs = 1;
						b = b*10 + list[j]-'0';
					}

				}
				else if (list[j] != '\0')
				{
					b = b*10 + list[j] -'0';
				}
				else
				{
					break;
				}
			}
		}
	
       switch(tmp)
	   {
	   case '+': difftmp = myabs(as*a + bs*b - 9);break;
	   case '-': difftmp = myabs(as*a - bs*b - 9);break;
	   case '*': difftmp = myabs(as*a * bs*b - 9);break;
	   case '/': difftmp = myabs((double)as*a/bs/b - 9);break;
	   }
	  
	
	return difftmp;
	
}
void bubble_sort(int *p,int num)
{
	int k,i,j;
	double temp;
	for(i=0;i<num-1;i++)
	{
		for(j=i+1;j<num;j++)
		{
			if(p[j]<p[i])
			{
				for(k=0;k<3;k++)
				{
					temp = p[i];
					p[i] = p[j];
					p[j] = temp;
				}
			}
		}
	}
}
int main()
{
    int CaseNum,Para1,Para2,tmp;
	int resultM[4];
	int mx[4];
	int mx2[4];
	int i=0,j=0;
	
   ifstream fin("A-small-attempt2.in",ifstream::in);
    if(!fin)
      return EXIT_FAILURE;
 
	fin>>CaseNum;
	int record[1000];
	if (CaseNum>=1 && CaseNum < 1000)
	{
        for(i=0;i<CaseNum;i++)
		{
			for(j=0;j<34;j++)
			{
				if(j==0)
				{	fin>>Para1;  }
				else if(j<=16)
				{
					if(j>=((Para1-1)*4+1) && j<=4*Para1)
					{
						fin>>mx[j-((Para1-1)*4+1)];
					}
					else
					{fin>>tmp;}
				}	
				
				if(j==17)
				{   fin>>Para2;  }
				else if (j>17)
				{
					if(j>=(17+(Para2-1)*4+1) && j<=(17+4*Para2))
					{
						fin>>mx2[j-((Para2-1)*4+1+17)];
					}
					else
					{fin>>tmp;}
				}
				
			}
			bubble_sort(mx,4);
			bubble_sort(mx2,4);

            for(j = 0;j<4;j++)
			{
				resultM[j]=0;
			}
			int pos =0;
			for(int p1=0;p1<4;p1++)
			{
				for(int p2=0;p2<4;p2++)
				{
					if(mx[p1]==mx2[p2])
					{	resultM[pos] = mx[p1];
					    pos++;
					    break;
					}
				}
			}
			int sum=0;
			for(j=0;j<4;j++)
			{
				if(resultM[j]!=0)
				{	sum++; }
			}
		    switch (sum)
			{case 1: record[i] = resultM[0];break;
			 case 0: record[i] = 0;break;
			 default: record[i] = -1;break;
			}
		}
	}
  ofstream fout("A-small-attempt2.out",ofstream::out);
	for(i=0;i<CaseNum;i++)
	{
		if(record[i]==0)
			fout << "Case #" << i+1 << ": "<<"Volunteer cheated!"<<endl;
		else if(record[i]==-1)
			fout << "Case #" << i+1 << ": "<<"Bad magician!"<<endl;
		else
			fout << "Case #" << i+1 << ": "<<record[i]<<endl;
	}
	system("pause");
    return 0;
}
#include<iostream>
#include<fstream>

using namespace std;


int max(int x,int y)
{
	return x>y?x:y;
}
int min(int x,int y)
{
	return y>x?x:y;
}
void quickSort(double a[],int left,int right)
{
   int i,j;
   double temp;
   i=left;
   j=right;
   temp=a[left];
   if(left>right)
      return;
   while(i!=j)/*ÕÒµ½×îÖÕÎ»ÖÃ*/
   {
      while(a[j]>=temp && j>i)
         j--;
      if(j>i)
         a[i++]=a[j];

      while(a[i]<=temp && j>i)
          i++;
      if(j>i)
          a[j--]=a[i];
   }
   a[i]=temp;
   quickSort(a,left,i-1);/*µÝ¹é×ó±ß*/
   quickSort(a,i+1,right);/*µÝ¹éÓÒ±ß*/
}

int main()
{
	int CaseNum;
	int casenum;
	int N;
	double Naomi[1000];
	double Ken[1000];
	int record[1000];
	int C,NC;
	  ifstream fin("D-large.in",ifstream::in);
 if(!fin)
   return EXIT_FAILURE; 
  ofstream fout("D-large.out",ofstream::out);
	fin>>CaseNum;
	int i,j;
	for(casenum=0;casenum<CaseNum;casenum++)
	{
		fin>>N;
		for(i=0;i<N;i++)
			fin>>Naomi[i];
		for(i=0;i<N;i++)
			fin>>Ken[i];

		quickSort(Naomi,0,N-1);
		quickSort(Ken,0,N-1);

        C=0;i=0;j=0;
		while(j<N)
		{
			if(Naomi[i]<Ken[j])
			{ i++;
				j++;
			}
			else
			{
				j++;C++;
			}
		}


		NC =0;i=N-1;j=N-1;int len=N;
		while(len>0)
		{

			if(Naomi[i]>Ken[j])
			{NC++;len--;i--;j--;}
			else
			{len--;j--;}
		}
		
        record[casenum*2] = NC;
		record[casenum*2+1] =C;

	}
	for(casenum=0;casenum<CaseNum;casenum++)
	{
		fout<<"Case #"<<casenum+1<< ": "<<record[casenum*2]<<" "<<record[casenum*2+1]<<"\n";
	}
	system("pause");
	return 0;
}


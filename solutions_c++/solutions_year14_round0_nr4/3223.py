#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
#include<algorithm>
#include<set>
#include<deque>
#include<map>
#include<math.h>
using namespace std;

#define InputOutputToFile

void merge(double arr[],int min,int mid,int max)
{
  double tmp[1005];
  int i,j,k,m; 
  j=min;
  m=mid+1;
  for(i=min; j<=mid && m<=max ; i++)
  {
     if(arr[j]<=arr[m])
     {
         tmp[i]=arr[j];
         j++;
     }
     else
     {
         tmp[i]=arr[m];
         m++;
     }
  }
  if(j>mid)
  {
     for(k=m; k<=max; k++)
     {
         tmp[i]=arr[k];
         i++;
     }
  }
  else
  {
     for(k=j; k<=mid; k++)
     {
        tmp[i]=arr[k];
        i++;
     }
  }
  for(k=min; k<=max; k++)
     arr[k]=tmp[k];
}

void part(double arr[],int min,int max)
{
	int mid;
	if(min<max)
	{
		mid=(min+max)/2;
		part(arr,min,mid);
		part(arr,mid+1,max);
		merge(arr,min,mid,max);
	}
}




int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 

	//cout.txt file using c library
	//FILE* fp=fopen("C:\\Programming_VS2010\\InterviewStreet\\InsertionSort\\cout.txt","w");
#endif

	int run = 0;
	cin>>run;
	int cs = 1;
	int count=0;
	
	double *N;
	double *K;
	//double *Nt;
	//double *Kt;

	int i=0;
	int j=0;
	int dwin=0;
	int nwin=0;

	bool itrFlg = false;
	while(run--)
	{
		if(itrFlg)
		{
			N=NULL;
			K=NULL;
			//Nt=NULL;
			//Kt=NULL;
			count=0;
			i=0;
			j=0;
			dwin=0;
			nwin=0;
			cout<<endl;
			//fprintf(fp,"\n");
		}
		itrFlg = true;

		cin>>count;
		N=(double*)malloc(count*sizeof(double));
		K=(double*)malloc(count*sizeof(double));
		//Nt=(double*)malloc(count*sizeof(double));
		//Kt=(double*)malloc(count*sizeof(double));

		for(i=0;i<count;i++)
			cin>>N[i];
		for(i=0;i<count;i++)
			cin>>K[i];
		
		part(N,0,count-1);
		part(K,0,count-1);
		
		//Deceitful War
		/*
		for(i=0;i<count;i++)
		{
			Nt[i]=N[i];
			Kt[i]=K[i];
		}
		*/
		i=0,j=0;
		int tmp=count;
		while(tmp>0)
		{
			if( N[i] > K[j] )
			{
				dwin++;
				i++;
				j++;
			}
			else
			{
				i++;
			}
			tmp--;
		}


		//Normal War
		i=j=count-1;
		tmp=count;
		while(tmp>0)
		{
			if(N[i]>K[j])
			{
				nwin++;
				i--;
			}
			else
			{
				i--;
				j--;
			}
			tmp--;
		}

		cout<<"Case #"<<cs<<": "<<dwin<<" "<<nwin;
		cs++;

		//logs-start
		/*cout<<"Naomi Data"<<endl;
		for(i=0;i<count;i++)
			cout<<"N["<<i<<"] :: "<<N[i]<<endl;

		cout<<"Ken Data"<<endl;
		for(i=0;i<count;i++)
			cout<<"K["<<i<<"] :: "<<K[i]<<endl;*/
		//logs-end
		
	}

	//fflush(fp);
	//fclose(fp);
	return 0;
}
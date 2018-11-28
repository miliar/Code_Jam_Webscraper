#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <iomanip>

using namespace std;

double naomi[1000];
double ken[1000];

void sort(int N)
{
  double temp;
  int i,j;
  for(i=0;i<N-1;i++)      
  {
         for(j=i+1;j<N;j++)      
         {
          if(naomi[i]>naomi[j])                         
            {
             temp=naomi[i];
             naomi[i]=naomi[j];
             naomi[j]=temp;                                    
            }
          
         }
  }
}

void sortb(int N)
{
  double temp;
  int i,j;
  for(i=0;i<N-1;i++)      
  {
         for(j=i+1;j<N;j++)      
         {
          
          if(ken[i]>ken[j])                         
            {
             temp=ken[i];
             ken[i]=ken[j];
             ken[j]=temp;                                    
            }
         }
  }
}



int main()
{
	
	int i,j,l;
	int caseT=1;
	int loocount;
	int N,k;
	int a=0;
	int y=0,z=0;
	double ken2[1000];
	ifstream in;
	ofstream out;
	in.open("D-large.in");
	out.open("out.out");
	in >> loocount;
	while(caseT<=loocount)
    {
      for(i=0;i<1000;i++)
      {
       naomi[i]=0.0;
       ken[i]=0.0;                   
      }
      in >> N;
      k=N-1;
      a=0;
      for(i=0;i<N;i++)
      {
       in >> naomi[i];
      }
      for(i=0;i<N;i++)
      {
       in >> ken[i];
      }
      sortb(N);
      
      
      for(i=0;i<N;i++)
      {
         ken2[i]=ken[i];   
      }
      j=0;
      for(i=0;i<N;i++)
      {
       if(naomi[i]>ken2[k])
       {                   
                           z++;
                           j++;
       }
       else
       {
           a=j;
        while(naomi[i]>ken2[a]) 
        {
         a++;                        
        }
        for(l=a;l<k;l++)
        {
         ken2[l]=ken2[l+1];                
        }   
        k--;
       }
      }
      a=0;
      sort(N);
      k=N-1;
      for(i=0;i<N;i++)
      {
       if(naomi[i]<ken[a])                                //cannot win
       {
        k--;                                                   
       }
       else
       {
           j=a;
        while(naomi[i]<ken[j])
        {
         j++;                      
        }    
        for(l=j;l<k;l++)
        {
         ken[l]=ken[l+1];                
        }
        k--;
        y++;
       }
      }
      
      out << "Case #" << caseT << ": " << y << ' ' << z <<endl;
      y=0;
      z=0;
      caseT++;
    }  
	in.close();
	out.close();
	return 0;
}



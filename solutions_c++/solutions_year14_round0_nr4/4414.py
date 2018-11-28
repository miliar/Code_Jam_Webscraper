#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int sort(long double*,int);
    ifstream fin("abc2.txt");
    ofstream fout("ex2.txt",ios::app);
    int loop;
	fin>>loop;
	for(int i=1;i<=loop;i++)
	{
      int length;     
      fin>>length;
      int k;
      long double naomi[length],ken[length];
      for(k=0;k<length;k++)
      {
                           fin>>naomi[k];
      }
      for(k=0;k<length;k++)
      {
                           fin>>ken[k];
      }
      
      //Sorting
      int m, n, flag = 1;    
      long double temp;              
      for(m = 1;m <=length && flag==1; m++)
     {
          flag = 0;
          for (n=0; n < (length -1); n++)
         {
               if (naomi[n+1] < naomi[n])      
              { 
                    temp = naomi[n];            
                    naomi[n] = naomi[n+1];
                    naomi[n+1] = temp;
                    flag = 1;               
               }
          }
      }
      flag =1;                
      for(m = 1;m <=length && flag==1; m++)
     {
          flag = 0;
          for (n=0; n < (length -1); n++)
         {
               if (ken[n+1] < ken[n] )     
              { 
                    temp = (ken[n]);            
                    (ken[n]) = (ken[n+1]);
                    (ken[n+1]) = temp;
                    flag = 1;               
               }
          }
      }
     
      int plus=0,minus=0;
		for(int j=length-1;(plus+minus)<length;j--)
        {
			if(naomi[j+minus]>ken[j])
            {
				plus++;
			}
			else
            {
				minus++;			
			}
		}
		fout<<"Case #"<<i<<": "<<plus<<" ";
	  int score=0,reject=0;
		for(int j=length-1;(score+reject)<length;j--)
        {
			if(ken[j+reject]>naomi[j])
            {
				score++;
			}
			else
            {
				reject++;
			}
			
		}
		fout<<reject<<"\n";
    }
    return 0;
}



 
 
      
         
     
            

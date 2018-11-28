#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin("abc1.txt");
    ofstream fout("ex1.txt",ios::app);
    int loop;
	fin>>loop;
	for(int i=1;i<=loop;i++)
	{       
            int count=0;
            int A1,A2,A[16],B[16],A3;
            fin>>A1;
            for(int j=0;j<16;j++)
            {
                 fin>>A[j];
            }
            fin>>A2;
            for(int k=0;k<16;k++)
            {
                 fin>>B[k];
            }
            for(int m=4*A1-4;m<=4*A1-1;m++)
            {
                 for(int n=4*A2-4;n<=4*A2-1;n++)
                 {
                         if(A[m]==B[n])
                         {
                                       count++;
                                       A3=A[m];
                         }
                 }
            }
            if(count==1) fout<<"Case #"<<i<<": "<<A3<<"\n";
            else if(count>1) fout<<"Case #"<<i<<": "<<"Bad magician!"<<"\n";
            else fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<"\n";
     }
return 0;
}
            
                                       
                         
            
            
            
                             
                              
                              
            
            

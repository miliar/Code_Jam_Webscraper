#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;


int main()
{
        fstream fin;
        fstream fout;
        fin.open("B-large.in",ios::in);   
        fout.open("2.txt",ios::out);
    int T,N = 1;
    fin >> T;
    
    while(T--)
    {
     
        int D,ans = 0;
        fin >> D;
        int iD[3000];
        int lc = 0, nc = 0,maxi = 0,counter = 0,max = 0,cD[3000],num[3000];
        for(int i = 0; i < 3000;i++)num[i] = 0;

        for(int i = 0; i < D;i++){
                fin >> iD[i];
                if(iD[i] >= max)max = iD[i];
                num[iD[i]]++;
        }
        int g = 0;
        
        for(int i = 1;i <= max; i++)
        {
           int C = 0,ng;

           for(int j = i+1;j <= max;j++)
           {
                if(j%i == 0)
                {
                       C += (( j/i )- 1) * num[j];
                }
                else 
                {
                     C += (j/i) * num[j]; 
                }
           }
           ng = C+i;
           if(i == 1)g = ng;
           else if(g >= ng)g = ng;
           
        }
        
       fout << "Case #" << N++ << ": " <<  g << endl;
    }
    
    
    system("pause");
    
}

#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

int senate[26];
int N, p, i, j, big, second, sum, count=0;

int main()
{
fstream fin;
ofstream fout;
fin.open("input1.txt");
fout.open("output.txt");
fin>>N;
cout<<N<<endl;
for(i=0; i<N; i++)
{
    fout<<"Case #"<<i+1<<": "; 
    fin>>p;
    sum=0;
    
    second=0;
    for(j=0; j<p; j++)
    {
        fin>>senate[j];
        cout<<senate[j]<<" ";
        sum+=senate[j];  
            
    }
    
    cout<<sum;  
    cout<<endl;
    
   while(sum>0)
   {
         big=0;  
         count=0;
   		 for(j=1; j<p; j++)
    {
        if(senate[j]>senate[big])
        {
        	big=j;
        }
    }
    for(j=0; j<p; j++)
    {
        if(j!=big&&senate[j]>=senate[second])
        {
        	second=j;
        }
    }	
    if(second==big)
    second==-1;
    cout<<"Big "<<big<<" Second "<<second<<"\n";	
    senate[big]--;
    sum--;
    fout<<char(big+65);
    if(senate[big]<=(sum-1)&&second!=-1&&sum!=2)
    {
    	senate[second]--;
    	sum--;
    	fout<<char(second+65);   
   }
   fout<<" ";
   }
   fout<<"\n";
}    

return 0;
}

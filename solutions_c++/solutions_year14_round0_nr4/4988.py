#include<iostream>
#include<fstream>
using namespace std;

int main()
{
  

ifstream in;
in.open("a.txt");
ofstream out;
out.open("output.txt");


int N;
int C;
int a=0;
double S[100];
double H[100];
in>>N;
for(int ii=0; ii<N; ii++)
{
	in>>C;
	for(int x=0; x<C; x++)
	{
		in>>S[x];
	}
	
	for(int x=0; x<C; x++)
	{
		in>>H[x];
	}
	
	double max;
	int loc=0;
	double temp=0;
	for(int i=0;i<C;i++)
	{
      for(int j=i+1;j<C;j++)
	  {
           if(S[i]>S[j])
		   {
               temp=S[i];
              S[i]=S[j];
              S[j]=temp;
           }
      }
  }
  for(int i=0;i<C;i++)
	{
      for(int j=i+1;j<C;j++)
	  {
           if(H[i]>H[j])
		   {
               temp=H[i];
              H[i]=H[j];
              H[j]=temp;
           }
      }
  }
	int win1=0;
	int ch=1;
	int s=C, h=C;
	s--;
	h--;
	while(1)
	{
		if(S[s]>H[h])
		win1++;
		else h--;
		
		if(s<1)
		break;
		s--;
	}
	
	
	int win2=0;
	s=C;
	h=C;
	s--;
	h--;
	while(1)
	{
		if(S[s]>H[h])
		{win2++;
		s--;
		}
		 
		
		if(h<1)
		break;
		h--;
	}
	out<<"Case #"<<ii+1<<": "<<win2<<" "<<win1<<"\n";
	
	
	
}	

}
#include<fstream>
#include<iostream>
#include<vector>
using namespace std;
int rest;
int num[10]; 
long long test(long long a);
void readd(long long b);
int main()
{
	
   ifstream fin("d:/A-large.in");
   ofstream fout("d:/q1.txt");
   int n;
   fin>> n;
   long long a;
   long long m=n;
   while(n--)
   {
   	  fin>>a;
	  if(test(a)==0) 
	  fout << "Case #"<<m-n<<": INSOMNIA\n";    	
   	 else
   	  fout << "Case #"<<m-n<<": "<<test(a)<<"\n";
   	
   	
   //	n--;
   }
   
   
   
   
   
   fin.close();
   fout.close();
   return 1;
   	
	
	
	
}



void readd(long long b)
{   long long r=0;
	while(b)
	{
	r=b%10;
	if(num[r]==0) num[r]=1,rest--;
	b=b/10;
	}
	
	cout << rest<<" ";
}

long long test(long long a)
{ long long N=0;  
if(a==0) return 0;   
rest=10;
	for(int i=0;i<10;i++) num[i]=0;
//	readd(a);
	while(rest)
	{    N+=a;
		readd(N);
		
	}
	
	return N;
	
	
}

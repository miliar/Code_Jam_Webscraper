#include "iostream"
#include "fstream"
#include "iomanip"
#include<conio.h>
#include<stdlib.h>
using namespace std;
int compare (const void * a, const void * b)
{
  if ( *(double*)a <  *(double*)b ) return -1;
  if ( *(double*)a == *(double*)b ) return 0;
  if ( *(double*)a >  *(double*)b ) return 1;
}
int main()
{
	int t,i,j,k,a,b,n,n1,n2,score,ptr,l,m;
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin>>t;
    for(i=0;i<t;i++)
    {
    	fin>>a>>b>>k;
    	score=0;
    	for(l=0;l<a;l++)
    		for(m=0;m<b;m++)
    			if((l&m)<k)
	    			score++;
    	fout<<"Case #"<<i+1<<": "<<score<<endl;
    }
    cout<<"ok";
    getch();
}

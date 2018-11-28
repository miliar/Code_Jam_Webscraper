#include <iostream>
#include <fstream>
using namespace std;

int a[102][102],n,m,t,test=1;


int main()
{  int i,j,k;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
	fin>>t;
	while(test<=t)
	{
	fin>>n>>m;
	for(i=0;i<n;i++)
		{
		for(j=0;j<m;j++)
		  fin>>a[i][j];
		}
	int f=0,temp=0;
	for(i=0;i<n;i++)
		{ 
		for(j=0;j<m;j++)
			{f=0;
			int temp=a[i][j];
			    for(k=0;k<m;k++)
			    	{if(a[i][k]>temp)
			    			{f+=1;break;}
			    	}
			    
			    for(k=0;k<n;k++)  
			        if(a[k][j]>temp) 
			          		{f+=1;break;}
               //cout<<f<<" ";
			   if(f==2) break;
			}
		if(f==2) break;
		}
		if(f==2) {fout<<"Case #"<<test<<": NO\n";}
		else fout<< "Case #"<<test<<": YES\n";
		test++;
		//cout<<"\n";
		}
return 0;

}
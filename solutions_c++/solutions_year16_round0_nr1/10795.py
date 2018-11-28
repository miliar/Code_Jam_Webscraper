
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
int main()
{

    ifstream fin("input.in");
    ofstream fout("output.out");
 long n;
 
    //-- check if the files were opened successfully 
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int i, j,k;  
    
    for (i = 0; i < numCase; i++)
    { 
    bool a[10]={0,0,0,0,0,0,0,0,0,0};
	  fin >> n;
    int j=0;
    while(1)
    { 
    
    	if(n==0)
    {	fout <<"Case #"<<i+1<<": INSOMNIA"<<endl;
 		break;
		}	
	long z= (j+1)* n;
	long x= (j+1)* n;
    while(x>=1)
    {
    a[x%10]=1;
    x=x/10;
	}
    
    if((a[1]==1)&& (a[0]==1)&&(a[2]==1)&&(a[3]==1)&&(a[4]==1)&&(a[5]==1)&&(a[6]==1)&&(a[7]==1)&&(a[8]==1)&&(a[9]==1))
 	{ 
	 	fout <<"Case #"<<i+1<<": "<<z<<endl;
 		break;
	} 
		j=j+1; 
	}
	}
         
     
    fin.close();
    fout.close();
    return 0;
}

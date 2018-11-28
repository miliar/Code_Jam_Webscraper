#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
using namespace std;
int main()
{  
	char input[] ="B-large.in";
	char output[]="B-large-output.in";
	int T,D,P[1000];
	ifstream infile;
    ofstream outfile;
    infile.open(input, ios::in);
    infile>>T;
    int S=T;
    
    outfile.open(output, ios::out);
    while(T--)
    {
    	infile>>D;
    	int s=0;
        int c;
    	for(int i=0;i<D;i++)
    	{   
    		infile>>c;
    		if (c>s)
    		   s=c;
    		P[i]=c;
    	}
        int best=s;
        for (int i=1;i<=s;i++)
        {   int k=0;
            for(int j=0;j<D;j++)
            {
                if((P[j]-i)>0)
                {   if(P[j]%i==0)
                        k-=1;
                    k+=(P[j]/i);
                }     
            }k+=i;
            if (k<best)
                best=k;
        }
        outfile<<"Case #"<<S-T<<": "<<best<<endl;
    }
    infile.close();
    outfile.close();
}
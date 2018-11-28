#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int testcase,a=1,p,j,cas=0,res;
	int orignal[4][4],trivert[4][4];
	
	ofstream outfile("output.txt");
	ifstream infile("input.txt");
	
	
	infile>>testcase;
	
	do{
		res=0,cas=0;
			infile>>p;
		for(int k=0; k<4 ; k++)
	    {
	    	
			for(int i=0; i<4; i++)
			{
			infile>>orignal[k][i];
	    	}
	    }
	    
	    infile>>j;
	    	    
		for(int k=0; k<4 ; k++)
	    {
	    	
			for(int i=0; i<4; i++)
			{
			infile>>trivert[k][i];
	    	}
	    }
	    
	    
	    for(int m=0; m<4 ; m++)
	    {
	    
		for(int k=0; k<4 ; k++)
	    {
	    	if(orignal[p-1][k]==trivert[j-1][m])
	    	{
	    		res=orignal[p-1][k];
	    		cas++;
	    	}
	    }
	    }
	    
	    outfile<<"Case #"<<a <<": ";
	    if(cas==0)
	    {
	    	outfile<<"Volunteer cheated!"<<endl;
	    }
	    else if(cas==1)
	    {
	    	outfile<<res<<endl;
	    }
	    else if(cas>=2)
	    {
	    	outfile<<"Bad magician!"<<endl;
	    }
	    
	    
		a++;
	}while(a<=testcase);
}

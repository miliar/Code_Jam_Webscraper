#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	freopen("A-small-attempt1.in", "r", stdin);
	//freopen("demo.in", "r", stdin);
 	freopen("At1.out", "w", stdout);
    int T,r1,r2;
    cin >> T;
    int in1[4][4],in2[4][4];
    int row1[4],row2[4];
    for(int k=1;k<=T;k++)
    {
    	cin >> r1;
    	for(int i=0;i<4;i++)
    	{
    		for(int j=0;j<4;j++)
		    	cin >> in1[i][j];	    			    	
	    	if(r1==(i+1))
				for(int j=0;j<4;j++)	    	
	    			row1[j]=in1[i][j];
	    }
    	cin >> r2;
    	for(int i=0;i<4;i++)
    	{ 
    		for(int j=0;j<4;j++)
		    	cin >> in2[i][j];	    	
	    	if(r2==(i+1))
				for(int j=0;j<4;j++)	    	
	    			row2[j]=in2[i][j];		        	
		} 
		int num=0;
		int out;
		for(int i=0;i<4;i++)
    	{ 
    		for(int j=0;j<4;j++)
    		{
		    	if(row1[i]==row2[j])
	    		{
		    		num++;
		    		out = row1[i];
		    	}
		    }
    	}
	    if(num==1)
	    	cout <<"Case #"<<k<<": "<<out<<endl;
		else if(num==0)
		   	cout <<"Case #"<<k<<": Volunteer cheated!"<<endl;  		
	   	else
	   		cout <<"Case #"<<k<<": Bad magician!"<<endl;
    }
	return 0;
}

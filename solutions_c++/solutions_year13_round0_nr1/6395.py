#include <fstream>
#include <iostream>

using namespace std;

void printResult(int,ofstream&);

int main()
{
	int N;
	ifstream fi("A-large.in");
	ofstream fo("output.txt");
	
	if(!fo || !fi)
		cout<<"File did not open!";

	fi>>N;
	int n = 1, i, j, result = 0;
	char board[5][5] = {"\0","\0","\0","\0"},line;
	while(n<=N)
	{
		int dc = 0;
	  
		for(i = 0 ; i < 4 ; i++)
		{
		  fi.get(line);
		  for(j = 0 ; j < 4 ; j++)
		     fi.get(board[i][j]);
		}
		
		//check row-wise
		for(i = 0 ; i < 4 && !result; i++)
		{
		    int xc = 0, oc = 0, t = 0;
		    
		    for(j = 0 ; j < 4 ; j++)
		      switch(board[i][j])
		      {
			case 'X':
			  xc ++; break;
			case 'O':
			  oc ++; break;
			case 'T':
			  t ++; break;
			case '.':
			  dc ++;
			  
		      }
		      
		   if(xc == 4 || xc + t == 4)
		      result = 1;
		     
		      
		    else if(oc == 4 || oc + t == 4)
		      result = 2;
		    
		}
		
		//check column-wise
		for(i = 0 ; i < 4 && !result ; i++)
		{
		    int xc = 0, oc = 0, t = 0;
		    
		    for(j = 0 ; j < 4 ; j++)
		      switch(board[j][i])
		      {
			case 'X':
			  xc ++; break;
			case 'O':
			  oc ++; break;
			case 'T':
			  t ++; break;
			case '.':
			  dc ++;
			  
		      }
		      
		    if(xc == 4 || xc + t == 4)
		      result = 1;
		     
		      
		    else if(oc == 4 || oc + t == 4)
		      result = 2;
		    
		}
		
		//check principal diagonal
		int xc = 0, oc = 0, t = 0;
		for(i = 0 ; i < 4 && !result ; i++)
		  switch(board[i][i])
		      {
			case 'X':
			  xc ++; break;
			case 'O':
			  oc ++; break;
			case 'T':
			  t ++; break;
			case '.':
			  dc ++;
			  
		      }
		      
		    if(xc == 4 || xc + t == 4)
		      result = 1;
		     
		      
		    else if(oc == 4 || oc + t == 4)
		      result = 2;
		      
		
		//check secondary diagonal
		xc = 0, oc = 0, t = 0;
		for(i = 0, j = 3 ; i < 4 && !result ; i++ , j --)
		  switch(board[i][j])
		      {
			case 'X':
			  xc ++; break;
			case 'O':
			  oc ++; break;
			case 'T':
			  t ++; break;
			case '.':
			  dc ++;
			  
		      }
		      
		    if(xc == 4 || xc + t == 4)
		      result = 1;
		     
		      
		    else if(oc == 4 || oc + t == 4)
		      result = 2;
	
		
		if(!result)
		{
		  if(!dc)
		    result = 3;
		  else
		    result = 4;
		  
		}		    
		      
		fo<<"Case #"<<n<<": ";
		printResult(result, fo);
		n++;
		result = 0;
		fi.get(line);

	}
		
	fi.close();
	fo.close();	

	return 0;

}

void printResult(int n, ofstream &fo)
{
	switch(n)
	{
	  case 1:
	    fo<<"X won\n";
	    break;
	  case 2:
	    fo<<"O won\n";
	    break;
	  case 3:
	    fo<<"Draw\n";
	    break;
	  case 4:
	    fo<<"Game has not completed\n";
	    break;
	    
	}
	
}
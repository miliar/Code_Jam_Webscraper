#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>

using namespace std;

int main(int argc, char **argv )
{
	int number_of_lines;
    string filename(argv[1]);
    string line;
    char temp;
    ifstream myfile(filename.c_str());
    ofstream myfileOut("output.out");
    if (myfile.is_open()) 
    {
        //first read the number of lines
        getline (myfile,line);
        number_of_lines = atoi(line.c_str());
        //make vector of vectors
        vector< vector<char> > cases(number_of_lines);
        //go for all lines and translate to Googlerese
        std::vector<char> v(16,'.');
		for (int i=0; i<number_of_lines; i++) 
            {
            	
            	// v.clear();
            	for (int k = 0; k < 4; ++k)
            	{
            		getline (myfile,line);
                	for (int j=0; j<line.length(); j++) {
                    //change every char
                   	 temp=line[j];
                   	 v[k*4+j]=temp;
                    	if (temp!='\n') {
                    	}
                	}
            	}
            	cases[i]=v;
                getline (myfile,line);
                // myfileOut << "Case #"<<i+1<<": "<< line<<endl;
            }
        myfile.close();
        if (myfileOut.is_open())
    {
    	int nesto = 0; //1 dobio X, 2 dobio O, 3 nije gotovo
        for (int i = 0; i < cases.size(); ++i)
        {
        	nesto = 0;
        	cout << "case " << i<<endl;
        	//Check Rows
        	for (int j = 0; j < 16; j+=4)
        	{
        		if( (cases[i][j]  == 'X' && cases[i][j+1]  == 'X' && cases[i][j+2] == 'X' && cases[i][j+3] == 'X') || (cases[i][j]  == 'T' && cases[i][j+1]  == 'X' && cases[i][j+2] == 'X' && cases[i][j+3] == 'X')  || (cases[i][j]  == 'X' && cases[i][j+1]  == 'T' && cases[i][j+2] == 'X' && cases[i][j+3] == 'X') || (cases[i][j]  == 'X' && cases[i][j+1]  == 'X' && cases[i][j+2] == 'T' && cases[i][j+3] == 'X') || (cases[i][j]  == 'X' && cases[i][j+1]  == 'X' && cases[i][j+2] == 'X' && cases[i][j+3] == 'T'))
        		{
        			//dobio je X
        			nesto = 1;
        			break;
        		}
				
				else if( (cases[i][j]  == 'O' && cases[i][j+1]  == 'O' && cases[i][j+2] == 'O' && cases[i][j+3] == 'O') || (cases[i][j]  == 'T' && cases[i][j+1]  == 'O' && cases[i][j+2] == 'O' && cases[i][j+3] == 'O')  || (cases[i][j]  == 'O' && cases[i][j+1]  == 'T' && cases[i][j+2] == 'O' && cases[i][j+3] == 'O') || (cases[i][j]  == 'O' && cases[i][j+1]  == 'O' && cases[i][j+2] == 'T' && cases[i][j+3] == 'O') || (cases[i][j]  == 'O' && cases[i][j+1]  == 'O' && cases[i][j+2] == 'O' && cases[i][j+3] == 'T') )
				{
					//dobio je 0
					nesto = 2;
					
					break;
				}
        	}
        	if (nesto==1)
        	{
        		myfileOut << "Case #" << i+1 << ": X won" <<endl;
        		continue;
        	}
        	if (nesto==2)
        	{
        		myfileOut << "Case #" << i+1 << ": O won" <<endl;
        		continue;
        	}
        	//Check cols
        	for (int j = 0; j < 4; j++)
        	{
        		if( (cases[i][j]  == 'X' && cases[i][j+4]  == 'X' && cases[i][j+8] == 'X' && cases[i][j+12] == 'X') || (cases[i][j]  == 'T' && cases[i][j+4]  == 'X' && cases[i][j+8] == 'X' && cases[i][j+12] == 'X')  || (cases[i][j]  == 'X' && cases[i][j+4]  == 'T' && cases[i][j+8] == 'X' && cases[i][j+12] == 'X') || (cases[i][j]  == 'X' && cases[i][j+4]  == 'X' && cases[i][j+8] == 'T' && cases[i][j+12] == 'X') || (cases[i][j]  == 'X' && cases[i][j+4]  == 'X' && cases[i][j+8] == 'X' && cases[i][j+12] == 'T'))
        		{
        			//dobio je X
        			nesto = 1;
        			break;
        		}
				
				else if(  (cases[i][j]  == 'O' && cases[i][j+4]  == 'O' && cases[i][j+8] == 'O' && cases[i][j+12] == 'O') || (cases[i][j]  == 'T' && cases[i][j+4]  == 'O' && cases[i][j+8] == 'O' && cases[i][j+12] == 'O')  || (cases[i][j]  == 'O' && cases[i][j+4]  == 'T' && cases[i][j+8] == 'O' && cases[i][j+12] == 'O') || (cases[i][j]  == 'O' && cases[i][j+4]  == 'O' && cases[i][j+8] == 'T' && cases[i][j+12] == 'O') || (cases[i][j]  == 'O' && cases[i][j+4]  == 'O' && cases[i][j+8] == 'O' && cases[i][j+12] == 'T') )
				{
					//dobio je 0
					nesto = 2;
					break;
				}
        	}
        	if (nesto==1)
        	{
        		myfileOut << "Case #" << i+1 << ": X won" <<endl;
        		continue;
        	}
        	if (nesto==2)
        	{
        		myfileOut << "Case #" << i+1 << ": O won" <<endl;
        		continue;
        	}
        	//check diags
        	//1
        	if( (cases[i][0]  == 'X' && cases[i][5]  == 'X' && cases[i][10] == 'X' && cases[i][15] == 'X') || (cases[i][0]  == 'T' && cases[i][5]  == 'X' && cases[i][10] == 'X' && cases[i][15] == 'X')  || (cases[i][0]  == 'X' && cases[i][5]  == 'T' && cases[i][10] == 'X' && cases[i][15] == 'X') || (cases[i][0]  == 'X' && cases[i][5]  == 'X' && cases[i][10] == 'T' && cases[i][15] == 'X') || (cases[i][0]  == 'X' && cases[i][5]  == 'X' && cases[i][10] == 'X' && cases[i][15] == 'T'))
        		{
        			//dobio je X
        			nesto=1;
        		}
				
				else if( (cases[i][0]  == 'O' && cases[i][5]  == 'O' && cases[i][10] == 'O' && cases[i][15] == 'O') || (cases[i][0]  == 'T' && cases[i][5]  == 'O' && cases[i][10] == 'O' && cases[i][15] == 'O')  || (cases[i][0]  == 'O' && cases[i][5]  == 'T' && cases[i][10] == 'O' && cases[i][15] == 'O') || (cases[i][0]  == 'O' && cases[i][5]  == 'O' && cases[i][10] == 'T' && cases[i][15] == 'O') || (cases[i][0]  == 'O' && cases[i][5]  == 'O' && cases[i][10] == 'O' && cases[i][15] == 'T') )
				{
					//dobio je 0
					nesto=2;
				}

			if (nesto==1)
        	{
        		myfileOut << "Case #" << i+1 << ": X won" <<endl;
        		continue;
        	}
        	if (nesto==2)
        	{
        		myfileOut << "Case #" << i+1 << ": O won" <<endl;
        		continue;
        	}
        	//2
			if( (cases[i][3]  == 'X' && cases[i][6]  == 'X' && cases[i][9] == 'X' && cases[i][12] == 'X') || (cases[i][3]  == 'T' && cases[i][6]  == 'X' && cases[i][9] == 'X' && cases[i][12] == 'X')  || (cases[i][3]  == 'X' && cases[i][6]  == 'T' && cases[i][9] == 'X' && cases[i][12] == 'X') || (cases[i][3]  == 'X' && cases[i][6]  == 'X' && cases[i][9] == 'T' && cases[i][12] == 'X') || (cases[i][3]  == 'X' && cases[i][6]  == 'X' && cases[i][9] == 'X' && cases[i][12] == 'T'))
        		{
        			//dobio je X
        			nesto=1;
        		}
				
				else if( (cases[i][3]  == 'O' && cases[i][6]  == 'O' && cases[i][9] == 'O' && cases[i][12] == 'O') || (cases[i][3]  == 'T' && cases[i][6]  == 'O' && cases[i][9] == 'O' && cases[i][12] == 'O')  || (cases[i][3]  == 'O' && cases[i][6]  == 'T' && cases[i][9] == 'O' && cases[i][12] == 'O') || (cases[i][3]  == 'O' && cases[i][6]  == 'O' && cases[i][9] == 'T' && cases[i][12] == 'O') || (cases[i][3]  == 'O' && cases[i][6]  == 'O' && cases[i][9] == 'O' && cases[i][12] == 'T'))
				{
					//dobio je 0
					nesto=2;
				}

        	if (nesto==1)
        	{
        		myfileOut << "Case #" << i+1 << ": X won" <<endl;
        		continue;
        	}
        	if (nesto==2)
        	{
        		myfileOut << "Case #" << i+1 << ": O won" <<endl;
        		continue;
        	}
        	//check if not completed
        	for (int j = 0; j < cases[i].size(); ++j)
        	{
        		if (cases[i][j]=='.')
        		{
        			//not completed
        			nesto=3;
        			break;
        		}
        	}
        	if (nesto==3)
        	{
        		myfileOut << "Case #" << i+1 << ": Game has not completed" <<endl;
        		continue;
        	}
        	//check if draw
        	//draw
        	myfileOut << "Case #" << i+1 << ": Draw" <<endl;
        	
        }
    }
    myfileOut.close();
    // cout << "vektor " << cases.size() << " mali " << cases[0].size() <<endl;
        for (int i = 0; i < cases.size(); ++i)
        {
        	for (int j = 0; j < cases[i].size(); ++j)
        	{
        		printf("%c",cases[i][j]);
        		if (j%4==3)
        		{
        			// printf("\n");
        		}
        	}
        	printf("\n");
        }   
    }
    

	     
        
    return 0;
}
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


int main()
{

	ifstream infile("A-large.in");
	ofstream	 fout("A-large.out");
	string line;
	int Test,cases;
        getline(infile, line);
	istringstream iss(line);
	iss >> Test;
	
	for(cases=0;cases<Test;cases++)
	{

		string l[4];
		int i,j,sum=0,nofinish=0;
		int win=0,draw=0;
		for(i=0;i<4;i++)
		{
			getline(infile, l[i]);
		}
		getline(infile,line);
		//horizontal		
		
		for(i=0;i<4;i++){
		sum=0;
		for(j=0;j<4;j++)
			sum+=l[i][j];
		if(sum==352||sum==348)
		{	win=1;
			break;
		}
		else if(sum==316||sum==321)
		{	
			win=-1;
			break;
		}
		else if(sum<316)
			++nofinish;
		}
		
		//vertical
		for(i=0;i<4;i++){
                sum=0;
                for(j=0;j<4;j++)
                        sum+=l[j][i];
                if(sum==352||sum==348)
                {	win=1;
                        break;
                }
                else if(sum==316||sum==321)
                {       
                        win=-1;
                        break;
                }
                else if(sum<316)
                        ++nofinish;
                }

		//diagonal 1
		sum=0;
                sum=l[0][0]+l[1][1]+l[2][2]+l[3][3];
                if(sum==352||sum==348)
                {	win=1;
                }
                else if(sum==316||sum==321)
                {       
                        win=-1;
                        
                }
                else if(sum<316)
                        ++nofinish;
                
		// diagonal 2
		
		sum = l[0][3]+l[1][2]+l[2][1]+l[3][0];
		 if(sum==352||sum==348)
                {       win=1;
                       	
                }
                else if(sum==316||sum==321)
                {       
                        win=-1;
                        
                }
                else if(sum<316)
                        ++nofinish;
                 
		if(win==1)
		fout<<"Case #"<<(cases+1)<<": X won"<<endl;
		else if(win==-1)
		fout<<"Case #"<<(cases+1)<<": O won"<<endl;
		else if(win==0&&(nofinish>0))
		fout<<"Case #"<<(cases+1)<<": Game has not completed"<<endl;
		else
		fout<<"Case #"<<(cases+1)<<": Draw"<<endl;

}
}	

	

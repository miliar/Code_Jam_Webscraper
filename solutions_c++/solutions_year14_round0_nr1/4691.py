/*
ID: k.kamal1
PROG: test
LANG: C++     
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	int val[4][4] = {0};
    	int curR;
    	fin >> curR;
    	curR--;
    	for(int rC = 0; rC < 4; rC++)
    	{
    		for(int colC = 0; colC < 4; colC++)
    		{
    			fin >> val[rC][colC];
    		}
    	}

		int vTmp[4][4] = {0};
    	int curTmp;
    	fin >> curTmp;
    	curTmp--;
    	for(int rC = 0; rC < 4; rC++)
    	{
    		for(int colC = 0; colC < 4; colC++)
    		{
    			fin >> vTmp[rC][colC];
    		}
    	}
    	int ret = -1;
    	bool fou = false;
    	for(int ct = 0; ct <= 3; ct++)
    	{
    		int curVal = val[curR][ct];
    		for(int ctc = 0; ctc <= 3; ctc++)
    		{
   				if(vTmp[curTmp][ctc] == curVal)
				{
					if(!fou)
					{
						ret = vTmp[curTmp][ctc];
						fou = true;	
					}
					else 
					{
						ret = -3;
						break;
					}
					
				} 			
    		}
    	}
    	fout << "Case #" << cnt + 1 << ": ";
    	if(ret == -1)
    		fout << "Volunteer cheated!" << endl;
    	else if(ret == -3)
			fout << "Bad magician!" << endl;
    	else 
			fout << ret << endl;
    	
    	
    }
    //fout << a+b << endl;
    return 0;
}

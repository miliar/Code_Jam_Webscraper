#include <iostream>
#include <fstream>

int main(int argc, char **argv)
{
    std::ifstream inf("magician.in.txt");
    std::ofstream outf("magician.out.txt");
    
    int testCount;
    inf >> testCount;
    
    for(int i = 0; i < testCount; i++)
    {
        int row1, row2;
	int arrang1[4][4];
	int arrang2[4][4];
	
	inf >> row1;
	for(int j = 0; j < 16; j++)
	{
	    inf >> arrang1[j / 4][j % 4];
	}
	inf >> row2;
	for(int j = 0; j < 16; j++)
	{
	    inf >> arrang2[j / 4][j % 4];
	}
	
	int *selectedRow = &arrang1[row1 - 1][0];
	bool find = false;
	bool single = true;
	int card;
	for(int j = 0; j < 4; j++)
	{
	    for(int k = 0; k < 4; k++)
	    {
	        if(selectedRow[j] == arrang2[row2 - 1][k])
		{
		    if(find == false)
		    {
		        card = selectedRow[j];
			find = true;
		    }
		    else
		    {
		        single = false;
		    }
		}
	    }
	}
	if(find)
	{
           if(!single)
	   {
	       outf << "Case #" << i + 1 << ": Bad magician!" << std::endl;
	   }
	   else
	   {
	       outf << "Case #" << i + 1 << ": " << card << std::endl;
	   }
	}
	else
	{
	    outf << "Case #" << i + 1 << ": Volunteer cheated!" << std::endl;
	}
    }
    
    inf.close();
    outf.close();
    
    return 0;
}

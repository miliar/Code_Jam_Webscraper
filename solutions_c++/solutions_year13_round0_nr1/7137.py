#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    int T;
    int XO; //1 for X and 0 for O 
    bool dot;
    ifstream in1;
    in1.open("A-large.in");
    ofstream out;
    out.open("A-large.out");
    in1 >> T;
    char inp [4][4];
    for (int i=0; i <T; i++)
    {
	XO = 2;
	dot = 0;
	for (int j=0;j<4;j++)
	{
	    
	    for (int k=0; k<4 ; k++)
	    {
		in1 >> inp[j][k];
	
	    }}
	    for (int j=0; j<4; j++)
	    {
	    if ( (inp[j][0] == inp[j][1]) && (inp[j][1] == inp[j][2]) && (inp[j][2]==inp[j][3]) && (inp[j][0]!='.'))
	    {
		if (inp[j][0] == 'X')
		    XO = 1;
		else
		    XO = 0;
		break;
	    }
	    else if ( (inp[j][0] == inp[j][1]) && (inp[j][1] == inp[j][2]) && (inp[j][3]=='T') && (inp[j][0]!='.'))
	    {
		if (inp[j][0] == 'X')
		    XO = 1;
		else
		    XO = 0;
		break;
	    }
	    else if ( (inp[j][0] == inp[j][1]) && (inp[j][2] == 'T') && (inp[j][1]==inp[j][3])&& (inp[j][0]!='.'))
	    {
		if (inp[j][0] == 'X')
		    XO = 1;
		else
		    XO = 0;
		break;
	    }
	    else if ( (inp[j][0] == inp[j][2]) && (inp[j][1] == 'T') && (inp[j][2]==inp[j][3])&& (inp[j][0]!='.'))
	    {
		if (inp[j][0] == 'X')
		    XO = 1;
		else
		    XO = 0;
		break;
	    }
	    else if ( (inp[j][0] == 'T') && (inp[j][1] == inp[j][2]) && (inp[j][2]==inp[j][3])&& (inp[j][1]!='.'))
	    {
		if (inp[j][1] == 'X')
		    XO = 1;
		else
		    XO = 0;
		break;
	    }
	}
	if (XO == 0)
	    out << "Case #" << i+1 << ": O won" << endl;
	else if (XO == 1)
	    out << "Case #" << i+1 << ": X won" << endl;
	else
	{
	XO =2;
	    for (int m=0; m<4; m++)
	    {
	
		if ( (inp[0][m] == inp[1][m]) && (inp[1][m] == inp[2][m]) && (inp[2][m]==inp[3][m]) && (inp[0][m]!='.'))
	    {
		if (inp[0][m] == 'X')
		    XO = 1;
		else
		    XO = 0;
		break;
	    }
	    else if ( (inp[0][m] == inp[1][m]) && (inp[1][m] == inp[2][m]) && (inp[3][m]=='T') && (inp[0][m]!='.'))
	    {
		if (inp[0][m] == 'X')
		    XO = 1;
		else
		    XO = 0;
		    break;
	    }
	    else if ( (inp[0][m] == inp[1][m]) && (inp[2][m] == 'T') && (inp[1][m]==inp[3][m])&& (inp[0][m]!='.'))
	    {
		if (inp[0][m] == 'X')
		    XO = 1;
		else
		    XO = 0;
		    
		    break;
	    }
	    else if ( (inp[0][m] == inp[2][m]) && (inp[1][m] == 'T') && (inp[2][m]==inp[3][m])&& (inp[0][m]!='.'))
	    {
		if (inp[0][m] == 'X')
		    XO = 1;
		else
		    XO = 0;
		    break;
	    }
	    else if ( (inp[0][m] == 'T') && (inp[1][m] == inp[2][m]) && (inp[2][m]==inp[3][m])&& (inp[1][m]!='.'))
	    {
		if (inp[1][m] == 'X')
		    XO = 1;
		else
		    XO = 0;
		    break;
	    }
	    }
	    if (XO == 0)
		out << "Case #" << i+1 << ": O won" << endl;
	else if (XO == 1)
		    out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[0][0] == inp [1][1]) && (inp[1][1] == inp[2][2]) && (inp[2][2] == inp[3][3]) && (inp[0][0] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[0][0] == inp [1][1]) && (inp[1][1] == inp[2][2]) && (inp[2][2] == inp[3][3]) && (inp[0][0] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[0][0] == 'T') && (inp[1][1] == inp[2][2]) && (inp[2][2] == inp[3][3]) && (inp[1][1] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[0][0] == 'T') && (inp[1][1] == inp[2][2]) && (inp[2][2] == inp[3][3]) && (inp[1][1] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[1][1] == 'T') && (inp[0][0] == inp[2][2]) && (inp[2][2] == inp[3][3]) && (inp[0][0] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[1][1] == 'T') && (inp[0][0] == inp[2][2]) && (inp[2][2] == inp[3][3]) && (inp[0][0] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[2][2] == 'T') && (inp[1][1] == inp[0][0]) && (inp[0][0] == inp[3][3]) && (inp[1][1] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[2][2] == 'T') && (inp[1][1] == inp[0][0]) && (inp[0][0] == inp[3][3]) && (inp[1][1] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[3][3] == 'T') && (inp[1][1] == inp[2][2]) && (inp[2][2] == inp[0][0]) && (inp[1][1] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[3][3] == 'T') && (inp[1][1] == inp[2][2]) && (inp[2][2] == inp[0][0]) && (inp[1][1] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[0][3] == inp [1][2]) && (inp[1][2] == inp[2][1]) && (inp[2][1] == inp[3][0]) && (inp[0][3] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[0][3] == inp [1][2]) && (inp[1][2] == inp[2][1]) && (inp[2][1] == inp[3][0]) && (inp[0][3] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[0][3] == 'T') && (inp[1][2] == inp[2][1]) && (inp[2][1] == inp[3][0]) && (inp[1][2] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[0][3] == 'T') && (inp[1][2] == inp[2][1]) && (inp[2][1] == inp[3][0]) && (inp[1][2] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[1][2] == 'T') && (inp[0][3] == inp[2][1]) && (inp[2][1] == inp[3][0]) && (inp[0][3] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[1][2] == 'T') && (inp[0][3] == inp[2][1]) && (inp[2][1] == inp[3][0]) && (inp[0][3] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[2][1] == 'T') && (inp[1][2] == inp[0][3]) && (inp[0][3] == inp[3][0]) && (inp[1][2] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[2][1] == 'T') && (inp[1][2] == inp[0][3]) && (inp[0][3] == inp[3][0]) && (inp[1][2] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else if ((inp[3][0] == 'T') && (inp[1][2] == inp[2][1]) && (inp[2][1] == inp[0][3]) && (inp[1][2] == 'X'))
		    	out << "Case #" << i+1 << ": X won" << endl;
	else if ((inp[3][0] == 'T') && (inp[1][2] == inp[2][1]) && (inp[2][1] == inp[0][3]) && (inp[1][2] == 'O'))
		    	out << "Case #" << i+1 << ": O won" << endl;
	else 
	{
	for (int j=0; j<4;j++)
	for (int k=0; k<4 ;k++){
		if (inp[j][k] != 'X' && inp[j][k]!= 'O' && inp[j][k]!='T')
		{
		    dot = 1;
		    break;}}
	if (dot == 1)
			out << "Case #" << i+1 << ": Game has not completed" << endl;
	else
	    		out << "Case #" << i+1 << ": Draw" << endl; }
}
}
out.close();
in1.close();
return 0;
}

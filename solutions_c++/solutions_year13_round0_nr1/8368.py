#include<iostream>
#include<fstream>
#include<string>

using namespace std;

void main()
{
	
	ifstream in("A-small-attempt1.in");
	ofstream out("results.txt");
    int count, a;
	in>>a;
	string table[4];
	for(count=1; count<=a; ++count)
	{
		for(int i=0; i<4; ++i)
			in>>table[i];

	    bool results[4] = {false, false, false, false};
	    char temp;
	    int i, j, countSpace=0;
	    for(i=0; i<4;++i)
	    {
		    for(j=0; j<4;++j)
		    {
			    temp = table[i][j];
			    if(temp =='.')
			    {
				    break;
			    }
			    else if(temp == 'X')
			    {
				    if(    ((table[0][j]=='X'||table[0][j]=='T') 
					    && (table[1][j]=='X' || table[1][j]=='T') 
					    && (table[2][j]=='X' || table[2][j]=='T') 
					    && (table[3][j]=='X' || table[3][j]=='T'))  || 
					    ((table[i][0]=='X' || table[i][0]=='T') 
					    && (table[i][1]=='X' || table[i][1]=='T') 
					    && (table[i][2]=='X' || table[i][2]=='T')
					    && (table[i][3]=='X' || table[i][3]=='T'))   )
					    results[0] = true;
				    else if( i == j && (table[0][0]=='X' || table[0][0] == 'T')
					    && (table[1][1]=='X' || table[1][1]=='T')
					    && (table[2][2]=='X' || table[2][2]=='T')
					    && (table[3][3]=='X' || table[3][3]=='T')  )
					    results[0] = true;
				    else if(i+j==3 && (table[0][3]=='X' || table[0][3] == 'T')
					    && (table[1][2]=='X' || table[1][2]=='T')
					    && (table[2][1]=='X' || table[2][1]=='T')
					    && (table[3][0]=='X' || table[3][0]=='T')  )
					    results[0] = true;
			    }

			    else if(temp == 'O')
			    {
				    if(    ((table[0][j]=='O'||table[0][j]=='T') 
					    && (table[1][j]=='O' || table[1][j]=='T') 
					    && (table[2][j]=='O' || table[2][j]=='T') 
					    && (table[3][j]=='O' || table[3][j]=='T'))  || 
					    ((table[i][0]=='O' || table[i][0]=='T') 
					    && (table[i][1]=='O' || table[i][1]=='T') 
					    && (table[i][2]=='O' || table[i][2]=='T')
					    && (table[i][3]=='O' || table[i][3]=='T'))   )
					    results[1] = true;
				    else if( i == j && (table[0][0]=='O' || table[0][0] == 'T')
					    && (table[1][1]=='O' || table[1][1]=='T')
					    && (table[2][2]=='O' || table[2][2]=='T')
					    && (table[3][3]=='O' || table[3][3]=='T')  )
					    results[1] = true;
				    else if(i+j==3 && (table[0][3]=='O' || table[0][3] == 'T')
					    && (table[1][2]=='O' || table[1][2]=='T')
					    && (table[2][1]=='O' || table[2][1]=='T')
					    && (table[3][0]=='O' || table[3][0]=='T')  )
					    results[1] = true;
			    }

			    if(results[0] || results[1])
				    break;
		    }
		    if(results[0] || results[1])
			    break;
	    }

	    if(results[0])
		    out<<"Case #"<<count<<":"<<" X won"<<endl;
	    else if(results[1])
		    out<<"Case #"<<count<<":"<<" O won"<<endl;
	    else
	    {
		    for(i=0; i<4; ++i)
		    {
			    for(j=0; j<4; j++)
			    {
				    if(table[i][j] == '.')
					    countSpace++;
			    }
		    }
		    if(countSpace == 0)
		    {
			    results[2] = true;
			    out<<"Case #"<<count<<":"<<" Draw"<<endl;
		    }
		    else
		    {
			    results[3] = true;
			    out<<"Case #"<<count<<":"<<" Game has not completed"<<endl;
		    }
	    }
	}
}
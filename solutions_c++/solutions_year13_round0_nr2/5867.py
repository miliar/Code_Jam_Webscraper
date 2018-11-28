#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>



int 
main()
{
    using namespace std;

    int lines[100];
    int cols[100];
    int more_lines[100];
    int more_cols[100];
    int lawn[100][100];

    int nb_cas;
    cin >> nb_cas;



    for(int cas = 0; cas < nb_cas; cas++)
    {
	cout << "Case #" << cas+1 << ": ";
	int size_m, size_n;
	cin >> size_n >> size_m;
	
	for(int i=0; i<size_n; i++)
	{
	    lines[i] = -1;
	    more_lines[i] = -1;
	}
	for(int i=0; i<size_m; i++)
	{
	    cols[i] = -1;
	    more_cols[i] = -1;		    
	}

	bool is_ok = true;
	for(int i=0; i<size_n; i++)
	{
	    for(int j=0; j<size_m; j++)
	    {
		cin >> lawn[i][j];
		more_lines[i] = more_lines[i] < lawn[i][j] ? lawn[i][j] : more_lines[i];
		more_cols[j]  = more_cols[j]  < lawn[i][j] ? lawn[i][j] : more_cols[j];
		if(i > 0)
		{
		    if(lawn[i-1][j] > lawn[i][j])
		    {
			if(lines[i] != -1 && lines[i] != lawn[i][j])
			{
			    is_ok = false;
			    break;
			}
			else
			    lines[i] = lawn[i][j];			
		    }
		    else if(lawn[i-1][j] < lawn[i][j])
		    {
			if(lines[i-1] != -1 && lines[i-1] != lawn[i-1][j])
			{
			    is_ok = false;
			    break;
			}
			else
			    lines[i-1] = lawn[i-1][j];
		    }
		}
		if(j > 0)
		{
		    if(lawn[i][j-1] > lawn[i][j])
		    {
			if(cols[j] != -1 && cols[j] != lawn[i][j])
			{
			    is_ok = false;
			    break;
			}
			else
			    cols[j] = lawn[i][j];			
		    }
		    else if(lawn[i][j-1] < lawn[i][j])
		    {
			if(cols[j-1] != -1 && cols[j-1] != lawn[i][j-1])
			{
			    is_ok = false;
			    break;
			}
			else
			    cols[j-1] = lawn[i][j-1];
		    }
		}
	    }
	}

	for(int i =0; i<size_n; i++)
	{
	    for(int j =0; j<size_m; j++)
	    {
		if((cols[j] != -1 && lawn[i][j] > cols[j]) || (lines[i] != -1 && lawn[i][j] > lines[i]))
		    is_ok = false;
		else if(lawn[i][j] < more_lines[i] && lawn[i][j] < more_cols[j])
		{
		    // cout << "lawn lower " << i << ":" << j << "--->lines:" << more_lines[i] << "--->cols:" << more_cols[i] << endl;
		    is_ok = false;
		}
	    }
	}
	// for(int i = 0; i<size_n; i++)
	// {
	//     cout << "line " << i << ":" << lines[i] << endl;

	// }

	// for(int j = 0; j<size_m ; j++)
	// {
	//     cout << "col " << j << ":" << cols[j] << endl;


	// }
	
	if(is_ok)
	    cout << "YES";
	else
	    cout << "NO";
	cout << endl;


    }
    
    return 0;
}

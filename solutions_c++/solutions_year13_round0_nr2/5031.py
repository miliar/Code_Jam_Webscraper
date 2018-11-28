#include<iostream>
#include<stdio.h>
#include<string>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int lawn[100][100];

void initlawn()
{
    for (int i=0; i<100; i++)
    {
        for (int j=0; j<100; j++)
        {
            lawn[i][j] = 100;
        }
    }
}

bool possible(int N, int M)
{
	int rowmin = 100;
	int rowsum = 0;
	int colsum = 0;
	int minx = 100, miny = 100;
	int rowmax = 0;

	for (int i = 0; i<N; i++)
	{
		// get rowmax
		rowmax = 0;
		for (int j = 0; j<M; j++)
		{
			if (lawn[i][j] > rowmax)
			{
				rowmax = lawn[i][j];
			}
		}
		// check element less than rowmax
		for (int j=0; j<M; j++)
		{
			if (lawn[i][j] < rowmax)
			{// check if the min in column
				for ( int k = 0; k<N; k++)
				{
					if (lawn[k][j] > lawn[i][j])
					{return false;}
				}
			}
		}
	}
	return true;
}


int main()
{
    ifstream infile;
    infile.open("B-large.in", ifstream::in);
    ofstream outfile;
    outfile.open("B-large.out", ofstream::out);


     int T, N, M;
     char line[10001];

      if (!infile.is_open())
    {
        cout<<"Failed open file"<<endl;
        return 0;
    } 

    initlawn();

    infile.getline(line,10001);
    sscanf(line, "%d", &T);
    cout<<T<<endl;

    int curmin = 100;
    int minrow = 100, mincol = 100;
    int curh = 0;
    char *infosplits;

	for (int l=0; l<T; l++)
    {
        infile.getline(line,10001);
        infosplits = strtok(line, " "); 
        sscanf(infosplits, "%d", &N);
        infosplits = strtok(NULL, " "); 
        sscanf(infosplits, "%d", &M);

        curmin = 100; curh = 0;

    	for (int row = 0; row<N; row++)
    	{
    		infile.getline(line,10001);
            infosplits = strtok(line, " "); 
            
    		for (int col = 0; col<M; col++)
    		{
                sscanf(infosplits, "%d", &curh);
    			lawn[row][col] = curh;
    			cout<<lawn[row][col];
                infosplits = strtok(NULL, " "); 
    		}
    		cout<<'\n';
    	}
        // check if possible
		if (possible(N, M))
		{outfile<<"Case #"<<l+1<<": "<<"YES\n";}
		else
		{outfile<<"Case #"<<l+1<<": "<<"NO\n";}
    }


    infile.close();
    outfile.close();
    return 0;
}
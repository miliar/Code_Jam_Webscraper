#include <iostream>
#include<fstream>
#include<vector>
using namespace std;

bool compare(vector< vector<int> > ,vector< vector<int> >,int x , int y);
int main ()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B_result.out");
		int T ; 
		fin>>T;
		for(int ss = 0  ; ss < T ; ss++)
		{
			int max=0;
			int N, M;
			fin>>N>>M;
			vector< vector<int>> grass;
			for(int i = 0 ; i< N ; i++)
			{
				vector < int > x; 
				for(int j = 0 ; j < M ; j++)
				{
					int temp; 
					fin>>temp;
					if(temp > max) max = temp;
					x.push_back(temp);
				}
				grass.push_back(x);
			}
			vector< vector<int>> o_grass;
			for(int i = 0 ; i< N ; i++)
			{
				vector < int > x; 
				for(int j = 0 ; j < M ; j++)
				{				
					x.push_back(max);
				}
				o_grass.push_back(x);
			}
			fout<<"Case #"<<ss+1<<": ";
			if(compare(o_grass,grass,0,0))	fout<<"YES"<<endl;
			else fout<<"NO"<<endl;
		}
		
		


	return 0 ; 
}

bool compare(vector< vector<int> > o_grass,vector< vector<int> > grass, int x , int y)
{
	for(int i  =x; i < grass.size() ; i ++ ) 
	{
		for(int j  =y; j < grass[0].size() ; j ++ ) 
	   {
		if(grass[i][j] < o_grass[i][j])
		{
			// Cut Row return it 
			vector< vector<int> > row = o_grass;
			vector< vector<int> > col = o_grass;
			bool row_c = true;
			bool col_c = true;
			for(int ii = 0 ; ii < row[i].size(); ii++)
			{
				if(row[i][ii] >= grass[i][j])
					row[i][ii] = grass[i][j];
				else row_c = false;
			}
			// cut column return it
			for(int ii = 0 ; ii < row.size(); ii++)
			{
				if(col[ii][j] >= grass[i][j])
					col[ii][j] = grass[i][j];
				else
				col_c = false;
			}
			if(col_c && row_c )
			{
				return compare(row , grass , 0 , 0 ) ||compare(col , grass , 0 , 0 );
			}
			else if(col_c)
				return compare(col , grass , 0 , 0 );
			else if ( row_c)
				return compare(row , grass , 0 , 0 );
			else return false;
			
		}
		else if ( grass[i][j] > o_grass[i][j])
			return false;		
		}
		
	}
		
	
	return true;
}
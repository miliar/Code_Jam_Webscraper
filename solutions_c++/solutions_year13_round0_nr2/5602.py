#include <vector>
#include <iostream>

using namespace std;

typedef unsigned short int cell_t;


enum direction
  {
    NORTH=0,
    EST,
    SOUTH,
    WEST
  };

vector< vector<cell_t> > readLawnPadding(unsigned int N,unsigned int M)
{
  vector< vector<cell_t> > ret;
  ret.reserve((N+1)*(M+1));
  // push N lines of M+2 columns (extended padding)
  for (unsigned int i=0;i<N;i++)
    {
      vector<cell_t> line;
      for (unsigned int j=0;j<M;j++)
	{
	  cell_t curCell;
	  cin>>curCell;
	  line.push_back(curCell);
	  if (j==0)
	    // second time push the first element
	    line.push_back(curCell);
	  else if (j==M-1)
	    // second time push the last element
	    line.push_back(curCell);

	}
      ret.push_back(line);
      if (i==0)
	// second time push the first element
	ret.push_back(line);
      else if (i==N-1)
	// second time push the last element
	ret.push_back(line);
    }
  return ret;
}

void getNESWneighbors(vector< vector<cell_t> > lawn,unsigned int i,unsigned int j,cell_t* ret)
{
  // north
  ret[0]=lawn[i-1][j];
  // est
  ret[1]=lawn[i][j+1];
  // south
  ret[2]=lawn[i+1][j];
  // west
  ret[3]=lawn[i][j-1];
}

void printLawn(vector< vector<cell_t> > lawn)
{
  for (unsigned int i=0;i<lawn.size();i++)
    {
      for (unsigned int j=0;j<lawn[i].size();j++)
	{
	  cout<<lawn[i][j]<<" ";
	}
      cout<<endl;
    }
  cout<<endl;
}

bool fullLowGrassLine(vector< vector<cell_t> > lawn, unsigned int i)
{
  for (unsigned int j=0;j<lawn[i].size();j++)
    {
      if (lawn[i][j]>1)
	return false;
    }
  return true;
}

bool fullLowGrassColumn(vector< vector<cell_t> > lawn, unsigned int j)
{
  for (unsigned int i=0;i<lawn.size();i++)
    {
      if (lawn[i][j]>1)
	return false;
    }
  return true;
}

void printState(vector< vector<cell_t> > lawn)
{
  for (unsigned int i=1;i<lawn.size()-1;i++)
    {
      for (unsigned int j=1;j<lawn[i].size()-1;j++)
	{
	  if (lawn[i][j]==1)
	    {
	      // low grass
	      // cell_t neighbors[4];
	      // getNESWneighbors(lawn,i,j,neighbors);
	      // if (
	      // 	  ((neighbors[NORTH]==1) && (neighbors[SOUTH]==1))
	      // 	  ||
	      // 	  ((neighbors[EST]==1) && (neighbors[WEST]==1)))
	      // 	continue;
	      if(fullLowGrassLine(lawn,i) || fullLowGrassColumn(lawn,j))
		continue;
	      else
		{
		  cout<<"NO";
		  return;
		}
	    }
	}
    }
  // no wrong low grass case
  cout<<"YES";
  return;
}

int main ()
{
  unsigned int tcases;
  cin>>tcases;
  for (unsigned int i=0;i<tcases;i++)
    {
      unsigned int N,M;
      cin>>N;
      cin>>M;
      vector< vector<cell_t> > lawn=readLawnPadding(N,M);
      cout<<"Case #"<<i+1<<": ";
      printState(lawn);
      cout<<endl;
      // printLawn(lawn);
    }
  return 0;
}

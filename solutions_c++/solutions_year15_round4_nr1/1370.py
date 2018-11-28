#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int check(const vector<vector<char> >& vec, int j, int k)
{
  if(vec[j][k]=='.')
    {return 0;}
  if(vec[j][k]=='^')
    {
      for(int l=0; l < j; ++l)
	{
	  if(vec[l][k]!='.')
	    {return 0;}
	}
      for(int l=j+1;l<vec.size();++l)
	{
	  if(vec[l][k]!='.')
	    {return 1;}	  
	}
      for(int l=0;l<vec[0].size();++l)
	{
	  if(l!=k && vec[j][l]!='.')
	    {return 1;}	  
	}
      return -1;
    }
  if(vec[j][k]=='v')
    {
      for(int l=j+1; l < vec.size(); ++l)
	{
	  if(vec[l][k]!='.')
	    {return 0;}
	}
      for(int l=0;l<j;++l)
	{
	  if(vec[l][k]!='.')
	    {return 1;}	  
	}
      for(int l=0;l<vec[0].size();++l)
	{
	  if(l!=k && vec[j][l]!='.')
	    {return 1;}	  
	}
      return -1;
    }
  if(vec[j][k]=='>')
    {
      for(int l=k+1; l < vec[0].size(); ++l)
	{
	  if(vec[j][l]!='.')
	    {return 0;}
	}
      for(int l=0;l<k;++l)
	{
	  if(vec[j][l]!='.')
	    {return 1;}	  
	}
      for(int l=0;l<vec.size();++l)
	{
	  if(l!=j && vec[l][k]!='.')
	    {return 1;}	  
	}
      return -1;
    }
  if(vec[j][k]=='<')
    {
      for(int l=0; l < k; ++l)
	{
	  if(vec[j][l]!='.')
	    {return 0;}
	}
      for(int l=k+1;l<vec[0].size();++l)
	{
	  if(vec[j][l]!='.')
	    {return 1;}	  
	}
      for(int l=0;l<vec.size();++l)
	{
	  if(l!=j && vec[l][k]!='.')
	    {return 1;}	  
	}
      return -1;
    }
}

int main()
{
  int cnt;
  cin >> cnt;
  for(int i = 0; i < cnt; ++i)
    {
      int R,C;
      cin >> R >> C;
      vector<vector<char> > vec(R, vector<char>(C));
      for(int j = 0; j < R; ++j)
	{
	  for (int k= 0; k < C; ++k)
	    {
	      char temp;
	      cin >> temp;
	      vec[j][k]=temp;
	    }
	}
      int tot=0;
      for(int j = 0; tot>=0 && j < R; ++j)
	{
	  for(int k = 0; tot>=0 && k < C; ++k)
	    {
	      if(check(vec,j,k)==0)
		{
		}
	      else if(check(vec,j,k)==1)
		{tot++;}
	      else
		{
		  tot=-1;
		}
	    }
	}
      cout << "Case #" << i+1 << ": "; 
      if(tot<0)
	{
	  cout <<  "IMPOSSIBLE" << endl;
	}
      else
	{
	  cout << tot << endl;
	}
    }
}

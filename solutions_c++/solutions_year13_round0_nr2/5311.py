#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
void print(vector<vector<int> >& t)
{
  for(int i=0;i<t.size();i++)
  {
    for(int j=0;j<t[i].size();j++)
    {
      cout<<t[i][j]<<" ";
    }
    cout<<endl;
  }
  cout<<endl;
}

void print(vector<bool>& t)
{
    for(int i=0;i<t.size();i++)
  {
    cout<<t[i]<<" ";
  }
  cout<<endl;
}
int main()
{
  int T;
  cin>>T;
  vector<bool> results(T,false);
  vector<vector<int> > lawnu;
  vector<int> killer;
  string temp;
  char *pend;
  cin.ignore();
  for(int i=0;i<T;i++)
  {
      if(!lawnu.empty())
      {
	lawnu.clear();
      }
      
      getline(cin,temp);
      int rows= strtol(temp.c_str(),&pend,10);
      int cols= strtol(pend,NULL,10);
      for(int j=0;j<rows;j++)
      {
	temp.clear();
	getline(cin,temp);
	pend=(char *)malloc(temp.length()+1);
	char* poi=pend;
	strcpy(pend,temp.c_str());
	killer.clear();
	for(int k=0;k<cols;k++)
	{
	  killer.push_back(strtol(pend,&pend,10));
	}
	lawnu.push_back(killer);
	free(poi);
      }
      
      vector<int> maxrows;
      vector<int> maxcols;
      for(int y=0;y<lawnu.size();y++)
      {
	maxrows.push_back(*max_element(lawnu[y].begin(),lawnu[y].end()));
      }
      for(int y=0;y<cols;y++)
      {
	int maxc=0;
	for(int z=0;z<rows;z++)
	{
	  if(lawnu[z][y]>maxc)
	  {
	    maxc=lawnu[z][y];
	  }
	}
	maxcols.push_back(maxc);
      }
      bool flag=true;
      for(int y=0;y<rows;y++)
      {
	for(int z=0;z<cols;z++)
	{
	  if(lawnu[y][z]<maxrows[y] && lawnu[y][z]<maxcols[z])
	  {
	    flag=false;
	  }
	}
      }
      results[i]=flag;
   }
   
for(int i=0;i<T;i++)
{
  switch(results[i])
  {
    case 0: cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
            break;
    case 1: cout<<"Case #"<<i+1<<": "<<"YES"<<endl;
	    break;
  }
}
//print(results);
  
}


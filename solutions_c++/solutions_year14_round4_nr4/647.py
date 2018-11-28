#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>


using namespace std;

int tr(vector<string>& tmp)
{
  set<string> myset;
  for(int i=0;i<tmp.size();i++)
    {
      string x="";
      for(int j=0;j<tmp[i].size();j++)
	{
	  x+=tmp[i][j];
	  myset.insert(x);
	}
    }
  return myset.size()+1;
}

int maketrie(vector<vector<string> >& tmp)
{
  int s = 0;
  for(int i=0;i<tmp.size();i++)
    s+=tr(tmp[i]);
  return s;
}


int main()
{
  ios::sync_with_stdio(false);
  int T;cin>>T;int I=1;
  while(I<=T)
    {
      int m,n;
      vector <string> str;
      cin>>n>>m;
      for(int i=0;i<n;i++)
	{
	  string tmp;
	  cin>>tmp;
	  str.push_back(tmp);
	}
      int mprim  =m;
      vector <vector<string> > sets(m);
      for(int i=1;i<n;i++)
	mprim*=m;
      int tedad = 0;
      int maximum = -1;
      for(int i=0;i<mprim;i++)
	{
	  for(int j=0;j<m;j++)
	    sets[j].clear();
	  int tmp = i;
	  for(int j=0;j<n;j++)
	    {
	      sets[tmp%m].push_back(str[j]);
	      tmp/=m;
	    }
	  bool b=0;
	  for(int j=0;j<m;j++)
	    if(sets[j].size()==0)
	      b=1;
	  if(b) continue;
	  int trie = maketrie(sets);/*
	  cerr<<"sets are :"<<endl;
	  for(int j=0;j<sets[0].size();j++)
		cerr<<sets[0][j]<<" ";
	  cerr<<endl;
	  cerr<<"trie is : "<<trie<<endl;
	      */
	  if(trie>maximum)
	    {
	      maximum = trie;
	      tedad=1;
	    }
	  else
	    {
	      if(maximum == trie)
		tedad++;
	    }
	}
      cout<<"Case #"<<I<<": "<<maximum<<" "<<tedad<<endl;
      I++;
    }
  return 0;
}

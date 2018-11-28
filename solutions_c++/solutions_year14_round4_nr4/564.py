#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <utility>
#include <queue>
#include <stack>
#include <string>

using namespace std;

int myPow(int a, int b)
{
  int ans=1;
  for(int i = 0; i < b; ++i)
    {
      ans*=a;
    }
  return ans;
}

struct Trie
{
  Trie()
    :cnt(0), vec(26, NULL) {}  
  int cnt;
  vector<Trie*> vec;
  ~Trie()
  {
    for(int i = 0; i < vec.size(); ++i)
      {
	if(vec[i]==NULL)
	  {continue;}
	else
	  {
	    delete vec[i];
	  }
      }
  }
  void insert(string str)
  {
    if(str.size()==0)
      {return;}
    int id=str[0]-'A';
    if(vec[id]==NULL)
      {
	vec[id]=new Trie();
	vec[id]->insert(str.substr(1));
      }
    else
      {
	vec[id]->insert(str.substr(1));
      }
    cnt=0;
    for(int i = 0; i < vec.size(); ++i)
      {
	if(vec[i]==NULL)
	  {continue;}
	else
	  {
	    cnt+=1;
	    cnt+=vec[i]->cnt;
	  }
      }
  }
};



int main()
{
  int tot;
  cin >> tot;
  for(int i = 0; i < tot; ++i)
    {
      cerr << i << endl;
      int M, N;
      cin >> M >>N;
      vector<string> vec;
      for(int j = 0; j < M; ++j)
	{
	  string str;
	  cin >> str;
	  vec.push_back(str);
	}
      int result=0;
      int totCnt=0;
      for(int j = 0; j < myPow(N, M); ++j)
	{
	  int curr=j;
	  vector<Trie> tree(N);
	  for(int k = 0; k < M; ++k)
	    {
	      int p=curr%N;
	      curr/=N;
	      tree[p].insert(vec[k]);
	    }
	  int ans=0;
	  for(int k = 0; k < N; ++k)
	    {
	      if(tree[k].cnt==0)
		{ans=-1; break;}
	      ans+=tree[k].cnt;
	    }
	  if(result<ans)
	    {
	      result=ans;
	      totCnt=1;
	    }
	  else if(result == ans)
	    {++totCnt;}
	}
      cout << "Case #" << i+1 << ": " << (N+result) % 1000000007 << " " << totCnt;
      cout << endl;
    }
}

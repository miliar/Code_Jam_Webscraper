#include <iostream>
#include <vector>
#include <bitset>

using namespace std;
const int MAXKEY = 20;

struct state
{
  state()
    :keys(MAXKEY, 0), costs(MAXKEY, 0) {}
  vector<int> keys;
  vector<int> costs;
};

bool valid(const vector<state>& chests, int old, int newN)
{
  for(int i = 0; i < MAXKEY; ++i)
    {
      if(chests[old].keys[i] < chests[newN].costs[i])
	{return false;}
    }
  return true;
}

int dp(const vector<state>& chests, vector<int>& move, int st, int N, vector<int>& visited)
{
  visited[st] = 1;
  if(st == (1<<N)-1)
    {
      move[st] = 1;
      return 1;
    }
  int hasNext = 0;
  for(int i = 0; i < N; ++i)
    {
      if(st&(1<<i))//already visited
	{continue;}
      if(!visited[st|(1<<i)] && valid(chests, st, st|(1<<i)))
	{
	  hasNext=dp(chests, move, st|(1<<i), N, visited);
	  if(hasNext)
	    {
	      move[st]=1;
	      break;
	    }
	}
    }
  return hasNext;
}

int main()
{
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i)
    {
      int K, N;
      cin >> K >> N;
      vector<state> chests(1<<N);
      for(int j = 0; j < K; ++j)
	{
	  int type;
	  cin >> type;
	  --type;
	  chests[0].keys[type]++;
	}
      vector<int> cost(N);
      vector<vector<int> > earn(N);
      for(int j = 0; j < N; ++j)
	{
	  int type, KK;
	  cin >> type >> KK;
	  --type;
	  cost[j] = type;
	  for(int k = 0; k < KK; ++k)
	    {
	      int newKey;
	      cin >> newKey;
	      --newKey;
	      earn[j].push_back(newKey);
	    }
	}    
      for(int j = 1; j < (1<<N); ++j)
	{
	  for(int k = 0; k < MAXKEY; ++k)
	    {
	      chests[j].keys[k] = chests[0].keys[k];
	    }
	  for(int bit = 0; bit < N; ++bit)
	    {
	      if(j&(1<<bit))
		{
		  chests[j].costs[cost[bit]]++;
		  for(int l = 0; l < earn[bit].size(); ++l)
		    {
		      chests[j].keys[earn[bit][l]]++;
		    }
		}
	    }
	}
      vector<int> move(1<<N, 0);
      vector<int> visited(1<<N, 0);
      int okay = dp(chests, move, 0, N, visited);
      cout << "Case #" << i+1 << ": ";
      if(okay)
	{
	  int curr = 0;
	  while(curr != (1<<N)-1)
	    {
	      //cerr << curr << endl;
	      for(int bit=0; bit < N; ++bit)
		{
		  if(!(curr&(1<<bit)) && move[curr|(1<<bit)])
		    {
		      cout << bit+1 << " ";
		      curr |= (1<<bit);
		      break;
		    }
		}
	    }
	  cout << endl;
	}
      else
	{cout << "IMPOSSIBLE" << endl;}
    }
}

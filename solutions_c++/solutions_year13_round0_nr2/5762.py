#include <iostream>
#include <vector>
#include <deque>

#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;


int main()
{
  int T, N, M;
  
  cin>>T;

  for(int i=0; i<T; ++i)
  {
    cin>>N>>M;
    
    vector<vector<int> > lawn(N);
    vector<vector<bool> > possible_lawn(N);
    
    vector<int> row_max(N, 1);
    vector<int> col_max(M, 1);
    
    for(int j=0; j<N; ++j)
    {
      lawn[j].resize(M);
      possible_lawn[j].resize(M, false);
      
      for(int k=0; k<M; ++k)
      {
        cin>>lawn[j][k];
        
        if(lawn[j][k] > row_max[j]) row_max[j] = lawn[j][k];
        if(lawn[j][k] > col_max[k]) col_max[k] = lawn[j][k];
      }
    }
    
    for(int j=0; j<N; ++j)
    {
      int first_height = lawn[j][0];
      bool possible = true;
      
      for(int k=1; k<M; ++k)
        if(lawn[j][k] != first_height)
          possible = false;
      
      if(possible)
      {
        possible_lawn[j].clear();
        possible_lawn[j].resize(M, true);
      }
    }    
    
    for(int k=0; k<M; ++k)
    {
      int first_height = lawn[0][k];
      bool possible = true;
      
      for(int j=1; j<N; ++j)
        if(lawn[j][k] != first_height)
          possible = false;
      
      if(possible)
      {
        for(int j=0; j<N; ++j)
          possible_lawn[j][k] = true;

      }
    }
    
    for(int j=0; j<N; ++j)
    {
      bool possible = true;
      
      for(int k=0; k<M; ++k)
      {
        if(lawn[j][k] != row_max[j] && !possible_lawn[j][k])
          possible = false;
      }
      
      if(possible)
      {
        possible_lawn[j].clear();
        possible_lawn[j].resize(M, true);
      }
    }
    
    for(int k=0; k<M; ++k)
    {
      bool possible = true;
      
      for(int j=0; j<N; ++j)
        if(lawn[j][k] != col_max[k] && !possible_lawn[j][k])
          possible = false;
      
      if(possible)
      {
        for(int j=0; j<N; ++j)
          possible_lawn[j][k] = true;
        
      }
    }
    
    bool possible = true;
    
    for(int j=0; j<N; ++j)
    {
      for(int k=0; k<M; ++k)
      {
        //cout<<possible_lawn[j][k];
        
        if(!possible_lawn[j][k]) possible = false;
      }
      
      //cout<<endl;
    }
    
    cout<<"Case #"<<i+1<<": ";
    
    if(possible)

      cout<<"YES"<<endl;
    
    else
      
      cout<<"NO"<<endl;
      
  }
  
	return 0;
  
}

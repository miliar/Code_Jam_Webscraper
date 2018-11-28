#include <iostream>
#include <vector>
#include <cstdio> 
#include <algorithm>
#include <set>
#include <string>
#include <map>

using namespace std;

#define REP(i, to) for(int i=0; i<to; i++)

typedef long long int LLI; 
typedef pair<LLI, LLI> PII; 

#define MOD 1000002013
#define INF 123456789123456789ll

LLI N;
map<LLI, LLI> C;

LLI solve(map<LLI, LLI>::iterator b, map<LLI, LLI>::iterator e){
  //cout << "solve("<<b->first<<", )" << endl; 

  LLI m=INF; 
  LLI result = 0; 
  
  while(b != e && b->second == 0){
    b++; 
  }
  if(b == e){
    return 0; 
  }
  
  for(map<LLI, LLI>::iterator iter = b ; iter != e ; iter++){
    //cout << iter->first << ", " << iter->second << endl;
    
    if(iter->second == 0){
      //cout << "remove("<<b->first<<", "<<iter->first<<") m=" << m << "" << endl; 
      LLI n = iter->first - b->first; 
      result = (result + m*(N*n - n*(n+1)/2)) % MOD; 
    
      for(map<LLI, LLI>::iterator kter = b ; kter != iter ; kter++){
        C[kter->first] -= m; 
      }
      //cout << "sub1("<<iter->first<<", "<<e->first<<") " << endl; 
      //result = (result + solve(iter, e)) % MOD; 
      break;
    }
    else{
      m = min(m, iter->second); 
    }
    
  }
  
  return result; 
}
    
int main()
{
  int T;
  cin >> T;
  REP(t, T){
    LLI result=0; 
  
    int M;
    cin >> N >> M;
    
    C.clear();
    vector<PII> E; 
    LLI price = 0; 
    
    REP(i, M){
      LLI a,b,p;
      cin >> a >> b >> p; 
      E.push_back(PII(a, p));
      E.push_back(PII(b, -p));
      
      price = (price + p*((b-a)*N - (b-a)*(b-a+1)/2)) % MOD; 
    }
    sort(E.begin(), E.end()); 
    
    int m=0; 
    REP(i, E.size()){
      m += E[i].second; 
      C[E[i].first] = m; 
    }
    
    //cout << "price=" << price << endl; 
    while(true){
      LLI add = solve(C.begin(), C.end()); 
      //cout << "add=" << add << endl;
      result = (result + add) % MOD; 
      if(add == 0){
        break;
      }
    }
    result = (price - result + MOD) % MOD; 
  
    cout << "Case #" << t+1 << ": " << result << endl;
  }
  
	return 0;
}

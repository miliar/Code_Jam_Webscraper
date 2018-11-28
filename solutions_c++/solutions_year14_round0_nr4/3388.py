#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int T,x,y,N,i,j;
vector<double> naomi,ken;
vector<vector<int> > adj;
int score1, score2;

int cheatMode(vector<double> n, vector<double> k)
{
  vector<bool> used1(N,false), used2(N,false);
  double chosen, told, kchosen;
  int score;

  int minK, minN, maxK, maxN;
  int a=0;
  while(a<N){
    chosen = -1;
    kchosen = -1;
    told = -1;
    a++;
    
    for(maxK=0;maxK<k.size();maxK++) if(!used2[maxK]) break;
    for(maxN=0;maxN<n.size();maxN++) if(!used1[maxN]) break;
    for(minK=k.size()-1;minK>=0;minK--) if(!used2[minK]) break;
    for(minN=n.size()-1;minN>=0;minN--) if(!used1[minN]) break;
    
    if(k[maxK]>n[maxN]){	  
      chosen = n[minN];
      told = n[maxN]-0.00001;
      used1[minN] = true;
    } else {
      told= n[maxN];
      for(j=n.size();j>=0;j--){
	if(n[j]>k[minK] && !used1[j]){
	  chosen = n[j];
	  used1[j] = true;
	  break;
	}
      }
    }
    
    for(j=k.size()-1;j>=0;j--){
      if(k[j]>told && !used2[j]){
	kchosen = k[j];
	used2[j] = true;
	break;
      }
    }
    
    if(kchosen==-1){
      kchosen = k[minK];
      used2[minK] = true;
    }

    if(kchosen < chosen) score++;
  }
  return score;
}

int normalMode(vector<double> n, vector<double> k)
{
  double chosen, kchosen;
  int score=0;
  while(!n.empty()){
    chosen = n[0];
    kchosen = -1;
    for(j=k.size()-1;j>=0;j--){
      if(k[j]>chosen){
	kchosen = k[j];
	break;
      }
    }
    
    if(kchosen==-1){
      kchosen = k[k.size()-1];
      score++;
    }
    n.erase(n.begin());
    k.erase(remove(k.begin(),k.end(),kchosen),k.end());
  }
  return score;
  
}

int main()
{
  cin >> T;
  int t=1;
  while(t<=T){
    cin >> N;
    naomi.resize(N);
    ken.resize(N);
    adj.resize(N,vector<int>(N,0));
    for(i=0;i<N;i++) {
      cin >> naomi[i];
    }
    for(i=0;i<N;i++){
      cin >> ken[i];
      for(j=0;j<N;j++){
	if(ken[i] < naomi[j]){
	  adj[i][j] = 1;
	}
      }
    }

    sort(naomi.begin(),naomi.end(),greater<double>());
    sort(ken.begin(),ken.end(),greater<double>());
    score1 = cheatMode(naomi,ken);
    score2 = normalMode(naomi,ken);
    cout << "Case #" << t << ": " << score1 << " " << score2 << endl;
    
    naomi.clear();
    ken.clear();
    adj.clear();
    t++;
  }
  
  return 0;
}

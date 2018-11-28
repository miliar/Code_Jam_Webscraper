#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#define mp(a,b) make_pair((a),(b))
#define ff first
#define ss second

using namespace std;

int main(){
  int i,j,k,l,m,n,o,p,r,s,t;
  int maxi,maxpoc;
  char c;
  vector<vector<char> > slova;
  vector<char> pom;
  map<vector<char>,int> mapa;
  vector<int> used;
  
  scanf("%d",&t);
  
  for(l=1;l<=t;l++){
    scanf("%d",&n);
    scanf("%d",&m);
    slova.clear();
    slova.resize(n);
    used.resize(n);
    
    
    maxi=0;
    maxpoc=0;
    
    for(i=0;i<n;i++){
      c=getchar();
      while(c=='\n'){
	c=getchar();
      }
      while(c!='\n'){
	slova[i].push_back(c);
	c=getchar();
      }
    }
    p=1;
    for(i=0;i<n;i++){
      p*=m;
    }
    
    for(i=0;i<p;i++){
      k=i;
      for(j=0;j<n;j++){
	used[j]=k%m;
	k/=m;
      }
      
      k=0;
      
      //printf("Delenie %d:\n",i);
      
      for(r=0;r<m;r++){
	mapa.clear();
	for(j=0;j<n;j++){
	  if(used[j]==r){
	    /*for(o=0;o<slova[j].size();o++){
	      putchar(slova[j][o]);
	    }
	    printf(" patri do skupiny %d\n",r);*/
	    pom.clear();
	    for(s=0;s<slova[j].size();s++){
	      pom.push_back(slova[j][s]);
	      mapa[pom]=1;
	    }
	  }
	}
	//printf("Velkost skupiny: %d\n",mapa.size());
	k+=mapa.size();
	if(mapa.size()>0){
	  k++;
	}
      }
      
      
      
      if(k==maxi){
	maxpoc++;
      }
      if(k>maxi){
	maxi=k;
	maxpoc=1;
      }
    }
    printf("Case #%d: %d %d\n",l,maxi,maxpoc);
  }
  
  return 0;
}

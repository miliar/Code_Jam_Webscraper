#include<bits/stdc++.h>
#define eps 1e-6
using namespace std;
int main(){
  int t,l=1;
  int i,j,n,kn,dwin=0,win=0;
  double nami[1000],ken[1000];
  cin>>t;
  while(t--){
    cin>>n;
    for(i=0;i<n;i++)
      cin>>nami[i];
    for(i=0;i<n;i++)
      cin>>ken[i];
    
    sort(nami, nami + n);
    sort(ken, ken + n);
    
    
  
    i=0;j=0;
    kn=n-1;
    dwin=0;
    while(i<n){
      if(nami[i]-ken[j]<eps){
	//TOLDnaomi = between k[n] and k[n-1]
	//ken wins
	kn--;	//delete k's block
      }
      else{
	if(nami[i]>ken[kn]){
	  //No need to decieve TOLDnaomi = n[i]
	  dwin=dwin+(n-i);  //naomi wins all
	  break;
	}
	else{
	  //Decive TOLDnaomi > k[kn]
	  j++;
	  dwin++;  //wins
	}
      }
      i++;
    }

    j=0;i=0;win=0;
    while(j<n){
      if(ken[j]-nami[i]>eps){
	j++;
	i++;
      }
      else{
	j++;
      }
    }
    win=n-i;

    cout<<"Case #"<<l++<<": "<<dwin<<" "<<win<<endl;
  }
}

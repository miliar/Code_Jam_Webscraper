#include<bits/stdc++.h>
#define N 2005
using namespace std;
string s,ans;
bool used[N],used2[N];
int n,a[10]={0,6,4,8,2,3,1,7,9,5};
string d[10];

int main(){
  d[0]="ZERO";
  d[1]="SIX";
  d[2]="FOUR";
  d[3]="EIGHT";
  d[4]="TWO";
  d[5]="THREE";
  d[6]="ONE";
  d[7]="SEVEN";
  d[8]="NINE";
  d[9]="FIVE";
  cin>>n;  
  for(int l=1;l<=n;l++){
    cin>>s;
    memset(used,0,sizeof(used));
    for(int i=0;i<10;i++){
      int j;
      memset(used2,0,sizeof(used2));
      for(j=0;j<d[i].size();j++){
	int f=0;
	for(int k=0;k<s.size();k++){
	  if(!used[k]&&!used2[k]&&s[k]==d[i][j]){
	    used2[k]=true;
	    f=1;
	    break;
	  }
	}
	if(!f)break;
      }
      if(j==d[i].size()){
	for(j=0;j<d[i].size();j++){
	  for(int k=0;k<s.size();k++){
	    if(!used[k]&&s[k]==d[i][j]){
	      used[k]=true;
	      break;
	    }
	  }
	}
	ans+=a[i]+'0';
	i--;
      }
    }
    sort(ans.begin(),ans.end());
    for(int w=0;w<s.size();w++)
      assert(used[w]);
    cout<<"Case #"<<l<<": ";
    cout<<ans<<endl;
    ans.clear();
  }
  return 0;
}

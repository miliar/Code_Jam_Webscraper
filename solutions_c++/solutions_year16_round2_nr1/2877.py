#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  string v[10];
  v[0]="ZERO";
  v[1]="TWO";
  v[2]="FOUR";
  v[3]="EIGHT";
  v[4]="THREE";
  v[5]="SIX";
  v[6]="ONE";
  v[7]="SEVEN";
  v[8]="FIVE";
  v[9]="NINE";
  int d[10]={0,2,4,8,3,6,1,7,5,9};
  cin>>n;
  for(int i=1;i<=n;i++){
    int c[300]={};
    vector<int> ans;
    string s;
    cin>>s;
    cout<<"Case #"<<i<<": ";
    for(int k=0;k<s.size();k++)
      c[s[k]]++;
    for(int j=0;j<=9;j++){
      int t=0;
      bool f=1;
      while(f){
	for(int k=0;k<v[j].size();k++){
	  if(!c[v[j][k]])f=0;
	  c[v[j][k]]--;
	}
	if(f)t++;
	else for(int k=0;k<v[j].size();k++)c[v[j][k]]++;
      }
      for(int k=0;k<t;k++)ans.push_back(d[j]);
    }
    sort(ans.begin(),ans.end());
    for(int k=0;k<ans.size();k++)cout<<ans[k];
    cout<<endl;
  }
  return 0;
}

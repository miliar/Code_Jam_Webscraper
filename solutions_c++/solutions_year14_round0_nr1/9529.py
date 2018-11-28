#include<bits/stdc++.h>
#include<iostream>
using namespace std;

void solve(int test) {
  int cnt[16];
  for(int i=0; i<16; i++) cnt[i] = 0;
  for(int z=0; z<2; z++) {
    int a;
    cin>>a;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++) {
	int k;
	cin>>k;
	k--;
	if(i==a-1) {
	  cnt[k]++;
	}
      }
  }
  int counter = 0;
  int ans;
  for(int i=0; i<16; i++) {
    if(cnt[i]==2)
      counter++, ans = i+1;
    
  } 
  cout<<"Case #"<<test<<": ";
  if(counter==0) cout<<"Volunteer cheated!"<<endl;
  if(counter==1) cout<<ans<<endl;
  if(counter>=2) cout<<"Bad magician!"<<endl;
    
}


int main() {
  int T;
  cin>>T;
  for(int i=0; i<T; i++)
    solve(i+1);
  
  
  return 0;
}

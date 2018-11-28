#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>


using namespace std;

typedef long long ll;


string prs;

void f(vector<int> v){  
  if (v[0]+v[1]+v[2]==1){
    for (int i=0; i<3; ++i)
      if (v[i])
	cout<<prs[i];
    return;
  }
  vector<int> v2(3,0);
  for (int i=0; i<3; ++i)
    v2[i]=v[i]/2;
  for (int i=0; i<3; ++i)
    if (v2[i]*2!=v[i]){
      v2[i]+=1;
      f(v2);
      v2[i]-=1;
    }
  return;
}
  

int main(){
  int T; cin>>T;
  prs="PRS";
  for (int tc=1; tc<=T; ++tc){
    cout<<"Case #"<<tc<<": ";
    int n, r, p, s;
    cin>>n>>r>>p>>s;
    vector<int> v(3,0);
    v[0]=p;
    v[1]=r;
    v[2]=s;
    vector<int> v2=v;
    sort(v2.begin(), v2.end());
    //cout<<"hei"<<endl;
    if (v2[2]-v2[0]!=1)
      cout<<"IMPOSSIBLE\n";
    else{
      f(v);
      cout<<endl;
    }
    


  }
  return 0;
}

#include <iostream>
#include <map>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int cs,a[4],r;


int main(){
  cin>>cs;
  rep(ii, cs){
    map<int,int> mp;
    int cnt = 0;
    int res = 0;

    cin>>r;
    rep(i,4){
      rep(j,4){
        cin>>a[j];
        if(i==r-1)mp[a[j]]=1;
      }
    }
    cin>>r;
    rep(i,4){
      rep(j,4){
        cin>>a[j];
        if(i==r-1 && mp[a[j]]==1){cnt++; res=a[j];}
      }
    }
    if(cnt==0){
      cout<<"Case #"<<ii+1<<": Volunteer cheated!"<<endl;
    }
    else if(cnt==1){
      cout<<"Case #"<<ii+1<<": "<<res<<endl;
    }
    else {
      cout<<"Case #"<<ii+1<<": Bad magician!"<<endl;
    }
  }
  
}

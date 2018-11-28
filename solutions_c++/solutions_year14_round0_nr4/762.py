#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
int num;
vector<double> n,nn,k,kk;
int ns,ks,used;
void pv(vector<double> x){
  for(int i=0;i<x.size();i++){
    cout<<x[i]<<" ";
  }
  cout<<endl;
}
int war(){
  double np,kp;
  int nw=0,kw=0;
  //cout<<k[ks-1]<<endl;
  while(used<num){
    np=n[ns-1];
    //cout<<"round "<<used+1<<endl;
    //pv(n);
    //pv(k);
    if(np>k[ks-1]){
      nw++;
      kp=k[0];
      used++;
      //cout<<np<<"  "<<k[ks-1]<<endl;
      n.erase(n.begin()+(ns-1));
      ns--;
      k.erase(k.begin()); //cout<<k[0]<<" "<<k[ks-1]<<endl;
      ks--;
      //cout<<"n won\n";
      //cout<<ns<<"  "<<ks<<endl;
    }else{
      kw++;
      used++;
      //cout<<np<<"  "<<*(upper_bound(k.begin(),k.end(),np))<<endl;
      n.erase(n.begin()+(ns-1));
      k.erase(upper_bound(k.begin(),k.end(),np));
      ns--; ks--;
      //cout<<"k won\n";
      //cout<<ns<<"  "<<ks<<endl;
    }
  }
  //cout<<nw<<" "<<kw<<endl;
  return nw;
}
int dwar(){
  ns=ks=num;
  used=0;
  double np,kp;
  int nw=0,kw=0;
  while(used<num){
    np=nn[ns-1];
    //cout<<"round "<<used+1<<endl;
    //pv(nn);
    //pv(kk);
    if(nn[0]>kk[0]){
      //lie bignum to him so that he'll play kk[0]
      //cout<<"beat his small with my small\n";
      nn.erase(nn.begin());
      kk.erase(kk.begin());
      ns--; ks--;
      used++;
      nw++;
    } else if(nn[0]<kk[0]){
      //lie with his max-1 so that he'll play kk[ks-1]
      //cout<<"exhausted his big\n";
      kw++; used++;
      nn.erase(nn.begin());
      kk.erase(kk.begin()+(ks-1));
      ns--; ks--;
    } else if(np>kk[ks-1]){
      //cout<<"straightfwd\n";
      nw++; used++;
      nn.erase(nn.begin()+(ns-1));
      kk.erase(kk.begin());
      ns--; ks--;
    }
  }
  return nw;
}
int main(){
  int tc;
  double inp;
  scanf("%d",&tc);
  for(int tcc=1;tcc<=tc;tcc++){
    printf("Case #%d: ",tcc);
    scanf("%d",&num);
    for(int i=0;i<num;i++){
      cin>>inp;
      n.push_back(inp);
      nn.push_back(inp);
    }
    sort(n.begin(),n.end());
    sort(nn.begin(),nn.end());
    for(int i=0;i<num;i++){
      cin>>inp;
      k.push_back(inp);
      kk.push_back(inp);
    }
    sort(kk.begin(),kk.end());
    sort(k.begin(),k.end());
    used=0;
    //cout<<n.size()<<"  "<<k.size()<<endl;
    ns=ks=num;
    cout<<dwar()<<" "<<war()<<endl;
  }
  return 0;
}


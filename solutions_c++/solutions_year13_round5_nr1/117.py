#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<cassert>
#include<map>
#define INF (1000000000000000LL)
using namespace std;
typedef long long ll;
int zz;
ll bets[40];
ll olb[40];
ll b;
double profit(double totb, double minc){
  return totb*(36.0/minc);
}
ll totc(ll minc, ll mid){
  ll totcost=mid*minc-olb[minc-1];
  for(int i=minc;i<37;i++){
    if(bets[i]<mid+1)
      totcost+=mid+1-bets[i];
  }
  return totcost;
}
bool canaf(ll minc, ll mid){
  ll totcost=totc(minc,mid);
  if(totcost<=b)
    return true;
  else
    return false;
}
double realpr(ll minc, ll mid){
  if(canaf(minc,mid) && mid>=bets[minc-1])
    return profit(mid*minc-olb[minc-1],minc)-((double)totc(minc,mid));
  return -INF;
}
double trin(ll minc, ll min, ll max){
  if(min>max)
    return -INF;/*
  if(zz==2 && minc==34)
    cout<<min<<" "<<max<<endl;*/
  if(max-min<10LL){
    double bst=-INF;
    for(ll i=min;i<=max;i++){
      if(realpr(minc,i)>bst)
        bst=realpr(minc,i);
    }
    return bst;
  }
  ll left=(max-min)/3LL+min;
  ll right=(2LL*(max-min))/3LL+min;
  double leftpr=realpr(minc,left);
  double rightpr=realpr(minc,right);
  if(leftpr>=rightpr)
    return trin(minc,min,right);
  else
    return trin(minc,left,max);
}
int main(){
  int ntest;
  cin>>ntest;
  ll n;
  bool debug=false;
  bool spam=true;
  double best2;
  for(zz=1;zz<=ntest;zz++){
    if(spam)
      printf("Case #%d: ",zz);
    //cout<<"Case #"<<zz<<": ";
    scanf("%lld%lld",&b,&n);
    double best=0;
    for(int i=0;i<n;i++){
      //cin>>bets[i];
      scanf("%lld",&(bets[i]));
    }
    for(int i=n;i<37;i++){
      bets[i]=0;
    }
    sort(bets,bets+37);
    olb[0]=bets[0];
    for(int i=1;i<37;i++){
      olb[i]=olb[i-1]+bets[i];
    }/*
    if(zz==2)
      cout<<trin(34,0,10)<<endl;*/
    for(ll minc=1;minc<37;minc++){
      ll min=bets[minc-1];
      ll max=b+2+bets[0];
      double prof=trin(minc,min,max);
      if(prof>best)
        best=prof;
    }
    if(debug){
      best2=0;
      for(ll minc=1;minc<37;minc++){
        for(ll mid=0;mid<=b+bets[0]+1;mid++){
          double prof=realpr(minc,mid);
          if(prof>best2)
            best2=prof;
        }
      }
      /*if(!(best-best2<0.000001 && best2-best<0.000001)){
        cout<<best<<" "<<best2<<endl;
        for(int i=0;i<37;i++){
          cout<<bets[i]<<" ";
        }
        cout<<endl;
      }*/
      assert(best-best2<0.00001 && best2-best<0.00001);
    }
    if(spam)
      printf("%.9lf\n",best);
  }
  return 0;
}

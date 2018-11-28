#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>

typedef long long int ll;
typedef long double ld;
#define SLL(x) scanf("%lld",&(x))
#define SI(x) scanf("%d",%(x))
#define REP(i,n) for(i=0;i<(n);i++)
using namespace std;
int FEQ(ld x,ld y){
  ld EPS=0.0000001;
  return (abs(y-x)<EPS)?1:0;
}
int fgreater(ld x, ld y){
  return ((x>y) && !(FEQ(x,y)))?1:0;
}
ll gcd(ll a, ll b){
  while(b!=0){
    //a,b=b,a%b
    ll temp=b;
    b=a%b;
    a=temp;
  }
  return a;
}
// class frac{
// public:
//   ll num, den;
//   int operator<(ll frac2){
//     return (num*frac2.den<den*frac2.num)?1:0;
//   } 
//   frac(ll num, ll den){
//     ll g=gcd(num,den);
//     num/=g;den/=g;
//     this.num=num;this.den=den;
    
//   }
//   int operator==(ll frac2){
//     return (num*frac2.den==frac2.num*den)?1:0;
//   }
//   frac operator+(frac frac2){
//     return frac(num
//   }
// };
// class mytime:frac{
// public:
//   mytime(ll num, ll den){
//     frac(num,den);
//   }
//   ll getCookies(){
//     return this.num;
//   }
//   ll getRate(){
//     return this.den;
//   }
// };
// ll longFracCeil(ll x, ll y){
//   return x/y+((x%y)==0?0:1);
// } 

ld ncookies;
ld time_base_;
ld n_factories;
ld rate;
ld cost, capacity, goal;
// class result{
// public:
//   ll time; //more time needed
//   ll mode;// mode==0 means no buy, mode==1 means buy
//   result(ld time_, ld mode_){
//     time=time_;mode=mode_;
//   }
// };
// result mintime(ld time_){
//   ld time1=ld(goal-ncookies)/ld(rate);
//   if(ncookies<factory_cost)return result(time1,0);
//   //try buying 1 factory
//   ll try_rate=rate+capacity;
//   ll try_ncookies=ncookies-factory_cost;
//   ld time2=ld(goal-ncookies)/ld(rate);
//   if(fgreater(time2,time1)){
//     return result(time2,1);
//   }else return result(time1,0);

// }
ll ldtoll(ld x){
  return ll(x+0.001);
}
int main(){
  ll i,j,k,n,nin,inum;
  SLL(nin);
  REP(inum,nin){
    n_factories=0;
    rate=2;
    //cin>>cost>>capacity>>goal;
    scanf("%Lf%Lf%Lf",&cost,&capacity,&goal);
    time_base_=0;
    ncookies=0;
    //postulate that if buying 1 factory does not benifit at a point of time, then buying multiple factories will not benifit either
    while(true){
      ld time1=(goal-ncookies)/(rate);
      if(ncookies<cost){
	ld time_adv=(cost-ncookies)/(rate);
	if(time1<time_adv){
	  time_base_+=time1;
	  printf("Case #%lld: %.6Lf\n",1+inum,time_base_);
	  break;/*break main while loop*/
	}else{
	  time_base_+=time_adv;
	  ncookies=cost;
	  //rate+=capacity;
	}
      }
      else {
	ld time2=(goal-(ncookies-cost))/(rate+capacity);
	if(time1<time2){
	  time_base_+=time1;
	  printf("Case #%lld: %.6Lf\n",1+inum,time_base_);
	  break;/*break main while loop*/
	}else{
	  //time_base_+=0.l;
	  ncookies-=cost;
	  rate+=capacity;
	}}}
  
  }
  return 0;
}

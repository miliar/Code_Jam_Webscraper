#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>

using namespace std;

const int taille=2000;
const int MAXI=100000000;

struct tribe{
  int d,n,w,e,s,dd,dp,ds;
  tribe(int _d, int _n, int _w, int _e, int _s, int _dd, int _dp, int _ds){
    d=_d;
    n=_n;
    w=_w;
    e=_e;
    s=_s;
    dd=_dd;
    dp=_dp;
    ds=_ds;
  }
};

int next_day(const vector<tribe> & tribues){
  int res=MAXI;
  for(int i=0;i<int(tribues.size());++i)
    res=min(res, tribues[i].d);
  return res;
}

bool attack(const tribe & t, const vector<int> & wall){
  for(int i=2*t.w;i<=2*t.e;++i)
    if(t.s>wall[i+taille/2])
      return true;
  return false;
}

void update(tribe & t, vector<int> & wall){
  for(int i=2*t.w;i<=2*t.e;++i)
    wall[i+taille/2]=max(wall[i+taille/2], t.s);
  t.n--;
  if(t.n==0)
    t.d=MAXI;
  else{
    t.d+=t.dd;
    t.w+=t.dp;
    t.e+=t.dp;
    t.s+=t.ds;
  }
}

int main(){
  int nbcase;
  cin >> nbcase;
  for(int icase=1;icase<=nbcase;++icase){
    cout << "Case #" << icase << ": ";
    int N;
    cin >> N;
   
    vector<tribe> tribues;
    for(int i=0;i<N;++i){
      int d,n,w,e,s,dd,dp,ds;
      cin >> d >> n >> w >> e >> s >> dd >> dp >> ds;
      tribues.push_back(tribe(d,n,w,e,s,dd,dp,ds));
    }
    vector<int> wall(taille,0);

    int res=0;
    int day=-1;
    while(day!=MAXI){
    day=next_day(tribues);
    if(day==MAXI)
      break;
    //cerr << day << endl;
    
    for(int i=0;i<N;++i){
      if(tribues[i].d!=day)
	continue;
      if(attack(tribues[i], wall)){
	//	cerr << "success\n";
	res++;
      }
    }

    for(int i=0;i<N;++i){
      if(tribues[i].d!=day)
	continue;
      update(tribues[i], wall);
    }


    }
    cout << res << '\n';
  }
}

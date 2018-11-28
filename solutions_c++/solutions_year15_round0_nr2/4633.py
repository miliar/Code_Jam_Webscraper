
#include <iostream>
#include <iomanip> //setprecision
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <iterator> //istream_iterator

using namespace std;

#define REP(i,N) for(int i=0;i<(N);i++)
#define FOR(i,A,B) for(int i=(A);i<=(B);i++)
#define ROF(i,A,B) for(int i=(B);i>=(A);i--)
#define ALL(A) (A).begin(),(A).end()

#define ISIi std::istream_iterator<int>
#define ISS std::istringstream
#define cinL2B(L,B) getline(cin,L); B.clear(); B.str(L);

typedef pair<int,int> pi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vector<vi> > vvvi;
typedef vector<pi> vpi;
typedef vector<vpi> vvpi;
typedef queue<pi> qpi;
typedef set<int> si;
typedef set<pi> spi;
typedef set<si> ssi;

vi p;

int optim(int max_p){
  //cout<<" :::"<<" "<<max_p<<" "<<p[max_p];
  if(p[max_p]<0) return 0;
  if(!max_p || !p[max_p]) return 0;
  if(max_p==1) return 1;
  if(max_p==2) return 2;
  if(max_p==3) return 3;

  p[max_p]--;
  int sub_max_p=max_p;
  //int moves=0;
  int tmp;
  int rez=1111;
  //REP(i,max_p+1)cout<<" "<<p[i];
  //cout<<" :"<<max_p<<endl;
  if(max_p==9){
    p[2]+=1;
    p[7]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    rez=optim(sub_max_p)+1;
    p[2]-=1;
    p[7]-=1;

    p[4]+=1;
    p[5]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    tmp=optim(sub_max_p)+1;
    if(rez>tmp) rez=tmp;
    p[4]-=1;
    p[5]-=1;

    p[3]+=1;
    p[6]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    tmp=optim(sub_max_p)+1;
    if(rez>tmp) rez=tmp;
    p[3]-=1;
    p[6]-=1;
  }
  else if(max_p==8){
    p[4]+=2;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    rez=optim(sub_max_p)+1;
    p[4]-=2;

    p[3]+=1;
    p[5]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    tmp=optim(sub_max_p)+1;
    if(rez>tmp) rez=tmp;
    p[3]-=1;
    p[5]-=1;

    p[2]+=1;
    p[6]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    tmp=optim(sub_max_p)+1;
    if(rez>tmp) rez=tmp;
    p[2]-=1;
    p[6]-=1;
  }
  else if(max_p==7){
    p[2]+=1;
    p[5]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    rez=optim(sub_max_p)+1;
    p[2]-=1;
    p[5]-=1;

    p[3]+=1;
    p[4]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    tmp=optim(sub_max_p)+1;
    if(rez>tmp) rez=tmp;
    p[3]-=1;
    p[4]-=1;
  }
  else if(max_p==6){
    p[3]+=2;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    rez=optim(sub_max_p)+1;
    p[3]-=2;

    p[2]+=1;
    p[4]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    tmp=optim(sub_max_p)+1;
    if(rez>tmp) rez=tmp;
    p[2]-=1;
    p[4]-=1;
  }
  else if(max_p==5){
    p[3]+=1;
    p[2]+=1;
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    rez=optim(sub_max_p)+1;
    p[3]-=1;
    p[2]-=1;
  }//*
  else if(max_p==4){
    p[2]+=2;
    //cout<<"----:"<<p[max_p];
    sub_max_p=max_p; while(!p[sub_max_p] && sub_max_p>0) sub_max_p--;
    rez=optim(sub_max_p)+1;
    p[2]-=2;
  }//*/
  p[max_p]++;

  if(max_p>rez) return rez;
  else return max_p;
}


int main(){
  int N,nr;
  string line;
  int d,max_p,sub_max_p,tmp,prev_max_p;
  ISS buffer;
  int moves;
  int rez;
  int old_max;
  
  getline(cin,line); istringstream(line)>>N;
  for(nr=0;nr<N;nr++){
    //getline(cin,line); istringstream(line)>>d;
    cinL2B(line,buffer);
    buffer>>d;

    p=vi(1001,0);
    //REP(i,1001) p[i]=0;

    max_p=0;
    //all=0;
    cinL2B(line,buffer);
    REP(i,d){
      buffer>>tmp;
      p[tmp]++;
      if(tmp>max_p) max_p=tmp;
    }

    //REP(i,max_p+1){
    //cout<<" "<<p[i];
      // }
    cout<<"Case #"<<nr+1<<":";

    cout<<" "<<optim(max_p);

    //   REP(i,max_p+1){
    //  cout<<" "<<p[i];
    //}
    cout<<endl;

    // ------------------------------------------------------
    //cout<<C<<" "<<F<<" "<<X<<endl;

  }
}

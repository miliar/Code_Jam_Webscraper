#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <limits.h>
#include <iterator>

using namespace std;

typedef int ttyp;
#define fors(bg,en) for(int i=bg;i<en;i++)
#define forso(j,bg,en) for(int j=bg;j<en;j++)
#define forz(n) for(int i=0;i<n;i++)
#define forzo(j,n) for(int j=0;j<n;j++)
#define forsz(v) for(int i=0;i<v.size();i++)
#define forszo(j,v) for(int j=0;j<v.size();j++)
#define MP make_pair
#define sz(v) v.size()
#define MODV 1000002013LL

map<long long,pair<long long,long long> > tempmap;
map<long long,pair<long long,long long> >::iterator it;
pair<long long,long long> tpra, tprb, vals[3000];
long long sta[3000];


void doit(){
    long long n, bg, en, np, on=1, ze=0, ret, expval=0, actval=0, nstat;
    int m, valix=0, valn=0;
    tpra=make_pair(on,ze);
    tprb=make_pair(ze,on);
    tempmap.clear();
    cin>>n>>m;
    forz(m){
        cin>>bg>>en>>np;
        nstat = en - bg;
        ret =( (nstat * n ) - ( nstat * (nstat-1) / 2)  ) % MODV;
        ret = (ret * np) % MODV;
        expval = ( expval + ret ) % MODV;
        if(tempmap.count(bg)==0){
            tempmap[bg]=tpra;
            tempmap[bg].first = np;
        }
        else tempmap[bg].first+=np;
        if(tempmap.count(en)==0){
            tempmap[en]=tprb;
            tempmap[en].second = np;
        }
        else tempmap[en].second+=np;
    }
    for(it=tempmap.begin();it!=tempmap.end();it++){
        sta[valn]=(*it).first;
        vals[valn++]=(*it).second;
    }
    forz(valn){
        ret = vals[i].second;
        if(vals[i].first){
            if(vals[i].first >= ret){vals[i].first-=ret;ret=0;}
            else {ret-=vals[i].first;vals[i].first=0;}
        }
        valix=i-1;
        while(ret){
            //cout<<"ret valix sta[valix] "<<ret<<" "<<valix<<" "<<sta[valix]<<endl;
            if(vals[valix].first){
                nstat = sta[i]-sta[valix];
                if(vals[valix].first >= ret){
                    np = ret;
                    vals[valix].first-=ret;
                    ret=0;
                }
                else {
                    np = vals[valix].first;
                    ret-=vals[valix].first;
                    vals[valix].first=0;
                }
                bg =( (nstat * n ) - ( nstat * (nstat-1) / 2)  ) % MODV;
                bg = (bg * np) % MODV;
                actval = ( actval + bg ) % MODV;
            }
            valix--;
        }
    }
    //cout<<"exp act "<<expval<<" "<<actval<<endl;
    ret = expval - actval;
    while(ret<0) ret = ( ret + MODV ) % MODV;
    cout<<ret<<endl;

  return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
      cout<<"Case #"<<i<<": ";
      doit();
    }
    return 0;
}


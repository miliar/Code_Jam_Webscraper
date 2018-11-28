#include <iostream>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <iterator>
#include <string>
#include <fstream>
#include <cstdio>

using namespace std;

typedef long long int64;

#define mp make_pair
#define pb push_back
#define ms0(x) memset(x,0,sizeof(x));
#define ms1(x) memset(x,-1,sizeof(x));

#define mod 1
#define EPS 1e-8

//------------------------------------------------------------------------//

vector<int> str,prm;

int mrk[100000];
int use[100000];
void sieve(){
    ms0(mrk);
    for(int i=2;i<100001;i++){
        if(mrk[i]==0){
            prm.pb(i);
            for(int j=i+i;j<100001;j+=i){
                mrk[j]++;
            }
        }
    }
}

int64 cal_fctrs(){
    int64 lcm=1;
    for(int i=0;i<prm.size();i++){
        int64 mx=0;
        for(int j=0;j<str.size();j++){
            //if((int64)prm[i]*prm[i]>(int64)str[j]) continue;
            int tmp= str[j];
            int cnt=0;
            while(tmp%prm[i]==0){
                cnt++;
                tmp/=prm[i];
            }
            if(mx<cnt) mx= cnt;
        }

        for(int j=0;j<mx;j++){
            lcm= lcm*prm[i];
        }
    }
    return lcm;
}

int main(){
    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    fout.open("out.txt");

    int tst;
    fin >> tst;
    sieve();
    for(int t=1;t<=tst;t++){
        int b,n;
        fin >> b >> n;

        for(int i=0;i<b;i++){
            int x;
            fin >> x;
            str.pb(x);
        }

       int64 lcm= cal_fctrs();
       //fout << lcm << endl;
       int dne=0;
       for(int i=0;i<str.size();i++){
            dne= dne+ (lcm/str[i]);
       }

       int tk= floor((double)n/dne);

       int rm= n- (tk-1)*dne;

       if(rm>dne) rm-=dne;
       //fout << rm << endl;
       fout << "Case #" << t << ": ";
       int fl=0;int ans;
       if(rm<=b) fout << rm << endl;
       else{
          int l= rm-b;
          for(int i=0;i<str.size();i++){
            use[i]=str[i];
          }
          int i;
          for(i=0;;){
            int mn= INT_MAX;
            for(int j=0;j<str.size();j++){
                if(mn>use[j]) mn=use[j];
            }

            for(int j=0;j<str.size();j++){
                if(use[j]==mn){
                   i++;
                   use[j]+=str[j];
                   if(i==l){
                    fl++;
                    ans=j;
                    break;
                   }
                }
            }
                if(fl>0) break;
          }
          fout << ans+1 << endl;
       }

       str.clear();
    }
}

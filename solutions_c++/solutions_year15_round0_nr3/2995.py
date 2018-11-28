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

using namespace std;

typedef long long int64;

#define mp make_pair
#define pb push_back
#define ms0(x) memset(x,0,sizeof(x));
#define ms1(x) memset(x,-1,sizeof(x));

#define mod 1
#define EPS 1e-8

//------------------------------------------------------------------------//

string str;
vector<int> use,cum;

int mult[][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int main(){
    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    fout.open("out.txt");

    int tst;
    fin >> tst;

    for(int t=1;t<=tst;t++){
        int l,x;
        fin >> l >> x;
        fin >> str;
        for(int i=0;i<x;i++){
            for(int j=0;j<l;j++){
                if(str[j]=='i') use.pb(2);
                else if(str[j]=='j') use.pb(3);
                else if(str[j]=='k') use.pb(4);
            }
        }
        for(int i=0;i<use.size();i++){
            if(i==0){
                cum.pb(use[i]);
            }else{
                int tp= cum[i-1];
                int tk= use[i];
                int fl=1;
                if(tp<0){ fl=-1; tp*=-1;}

                int kn= mult[tp][tk];
                cum.pb(kn*fl);
            }
        }
        int fl=0;
        for(int i=0;i<cum.size();i++){
            if(cum[i]==2 && fl==0){
                fl++;
            }
            if(cum[i]==4 && fl==1){
                fl++;
            }
            if(cum[i]==-1 && fl==2 && i==cum.size()-1){
                fl++;
            }
            //fout << cum[i] << " ";
        }
        if(fl==3) fout << "Case #" << t << ": YES" << endl;
        else fout << "Case #" << t << ": NO" << endl;
        cum.clear();
        use.clear();
        str.clear();
    }
    fin.close();
    fout.close();
    return 0;
}

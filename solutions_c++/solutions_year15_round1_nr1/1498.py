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

vector<int> str;

int main(){
    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    fout.open("out.txt");
    int tst;

    fin >> tst;

    for(int t=1;t<=tst;t++){
        int n;
        fin >> n;

        for(int i=0;i<n;i++){
            int x;
            fin >> x;
            str.pb(x);
        }

        int mn1=0;int mx=0;
        for(int i=1;i<n;i++){
            if(str[i]<str[i-1]){
                int x= str[i-1]-str[i];
                mn1+= (x);
                if(mx<x) mx=x;
            }
        }
        //fout << mx << endl;
        int mn2=0;
        for(int i=0;i<n-1;i++){
            if(mx<str[i]){
                mn2+= mx;
            }else mn2+= str[i];
        }

        fout << "Case #" << t << ": " << mn1 << " " << mn2 << endl;
        str.clear();
    }
    return 0;
}

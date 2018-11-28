#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define FOR(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define FORR(i,n) for(int i=(int)(n);i>=0;i--)
#define FORE(i,n) for(int i=0;i<=(int)(n);++i)
#define MP(X,Y) make_pair(X,Y)
typedef pair<int,int> ipair;
typedef long long int64;
#define MAX_N 2001

bool dict[30];

void initDict(){
    FOR(i,30)dict[i]=true;
    dict['a'-'a']=false;
    dict['e'-'a']=false;
    dict['i'-'a']=false;
    dict['o'-'a']=false;
    dict['u'-'a']=false;
}

int main(int argc,char** argv){
    initDict();
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int TC;
    cin>>TC;
    FOR(tc,TC){
        string name;
        int n,length;
        cin>>name>>n;
        int num=0;
        length=name.size();
        vector<int> sums(length+1);
        sums[0]=0;
        FOR(i,length){
            sums[i+1]=sums[i]+(dict[name[i]-'a']?1:0);
        }
        int end=length-n+1;
        int next=n;
        FOR(i,end){
            REP(j,max(i+n,next),length+1)if(sums[j]-sums[j-n]>=n){
                num+=length+1-j;
                next=j;
                break;
            }
        }
        cout<<"Case #"<<tc+1<<": "<<num<<endl;
    }
}
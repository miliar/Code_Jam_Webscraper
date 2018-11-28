#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <cassert>
#include <set>
using namespace std;


const int N=888888;

int n;
string get(char ch,int d) {
    if (d>=n) {
        string ret="";
        ret+=ch;
        return ret;
    }
    if (ch=='R') {
        string a=get('R',d+1);
        string b=get('S',d+1);
        return min(a,b)+max(a,b);
    }
    else if (ch=='S') {
        string a=get('P',d+1);
        string b=get('S',d+1);
        return min(a,b)+max(a,b);
    }
    else {
        string a=get('P',d+1);
        string b=get('R',d+1);
        return min(a,b)+max(a,b);
    }
}
bool valid(string str,int r,int p,int s) {
    int nr=0,np=0,ns=0;
    for (int i=0;i<str.length();i++) {
        if (str[i]=='R')
            nr++;
        else if (str[i]=='P')
            np++;
        else
            ns++;
    }
   // cout<<ns<<" "<<nr<<" "<<np<<endl;
    return s==ns&&r==nr&&p==np;
}
string ret="IMPOSSIBLE";
void update(string s) {
    if (ret=="IMPOSSIBLE")
        ret=s;
    else
        ret=min(ret,s);
}
int main () {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        int r,p,s;
        scanf("%d %d %d %d",&n,&r,&p,&s);
        ret="IMPOSSIBLE";
        //cout<<"cccc"<<endl;
        string a=get('R',0);
        if (valid(a,r,p,s))
            update(a);

        string b=get('P',0);
        if (valid(b,r,p,s))
            update(b);
        string c=get('S',0);
        if (valid(c,r,p,s))
            update(c);
        printf("Case #%d: %s\n",cas,ret.c_str());
    }
    return 0;
}

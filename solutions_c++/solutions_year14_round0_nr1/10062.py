//Coder: saiteja ranuva

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

int grid1[4][4],grid2[4][4],r1,r2;

int magic(int r1,int r2){
    int h[17],n=0,c=0;
    for(int i=0;i<16;i++)
        h[i]=0;
    for(int i=0;i<4;i++)
        h[grid1[r1-1][i]]=1;

    for(int i=0;i<4;i++){
        if(h[grid2[r2-1][i]]==1){
            n=grid2[r2-1][i];
            c++;
        }
    }
    if(c==0)
        return -1;
    if(c==1)
        return n;
    else
        return 0;
}

int main() {
    FILE *f1=fopen("input.txt", "r");
    FILE *f2=fopen("output.txt", "w");
    int T;
    fscanf(f1,"%d", &T);

    for(int t = 0; t < T; ++t) {
        fscanf(f1,"%d", &r1);
        char buffer[10]="";
        fr(i, 4) fr(j, 4)fscanf(f1,"%d", &grid1[i][j]);
        fscanf(f1,"%d", &r2);
        fr(i, 4) fr(j, 4)fscanf(f1,"%d", &grid2[i][j]);
        string ans;
        int k=magic(r1,r2);
        if(k==0)
            ans="Bad magician!";
        if(k==-1)
            ans="Volunteer cheated!";
        if(k!=0 && k!=-1)
            itoa(k,buffer,10);
        if(buffer[0]!='\0')
            ans=buffer;
        fprintf(f2,"Case #%d: %s\n", t+1, ans.c_str());
    }

	return 0;
}

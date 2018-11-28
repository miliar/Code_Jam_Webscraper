#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <set>
#include <sstream>
#include <istream>
#include <fstream>
#include <climits>
#include <string.h>
#include <ctime>

#define infinity        200000000
#define pusb(a)         push_back(a)
#define SZ(val)         ((int)val.size())
#define mp(a,b)         make_pair(a,b)
#define fs              first
#define sc              second
#define sqr(a)          ((a)*(a))
#define pi              (2.0*acos(0.0))
#define ALL(a)          a.begin(),a.end()
#define memos(ARR,VAL)  memset(ARR,VAL,sizeof(ARR))
#define fileinput       freopen("A-small-attempt0.in","r",stdin)
#define fileoutput      freopen("output.txt","w",stdout)
const int SIZE=4;
const int SIZE2=25;

using namespace std;

typedef long long Bint;
typedef vector<int> Vint;
typedef vector<string> Vstring;
typedef pair<int,int> Prr;
typedef vector<Prr> Vprr;
typedef multiset<int> MSet;
typedef map<Prr,int> PM;
typedef map<Prr,int> ::iterator PMit;
typedef multiset<int>::iterator MSetit;
typedef priority_queue< int, Vint, greater<int> > MinPQ;
typedef priority_queue< int, Vint, less<int> > MaxPQ;

///int BigMod(Bint B,Bint P,Bint M){Bint R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;}
///int cx[]= {0, 1, 1, 1, 0, -1, -1, -1};
///int cy[]= {1, 1, 0, -1, -1, -1, 0, 1};
///int cx[]={-1,0,0,1};
///int cy[]={0,-1,1,0};
///int hx[]={-2,-2,-1,-1,1,1,2,2};
///int hy[]={-1,1,-2,2,-2,2,-1,1};

map<int,int> info;
map<int,int>::iterator it;
int mat[SIZE][SIZE],twoCount,ans;

void getAnswer();
int main() {

    fileinput;
    fileoutput;
    int test,row,x;

    scanf("%d",&test);

    for(int kase=1; kase<=test; kase++) {

        scanf("%d",&row);
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                scanf("%d",&mat[i][j]);
            }
        }

        row--;
        for(int i=0; i<4; i++) {
                info[mat[row][i]]++;
        }

        scanf("%d",&row);
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                scanf("%d",&mat[i][j]);
            }
        }

        row--;
        for(int i=0; i<4; i++) {
                info[mat[row][i]]++;
        }

        getAnswer();
        if(twoCount==1){
                printf("Case #%d: %d\n",kase,ans);
        }
        else if(twoCount>=2){
            printf("Case #%d: Bad magician!\n",kase);
        }
        else{
            printf("Case #%d: Volunteer cheated!\n",kase);
        }

        twoCount=0;
        info.clear();
    }
    return 0;
}


void getAnswer(){

    for(it=info.begin();it!=info.end();it++){
        if(it->second==2){
            twoCount++;
            ans=it->first;
        }
    }
    return ;
}

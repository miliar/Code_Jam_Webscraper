#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <climits>

using namespace std;

typedef long long LL;

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );

#define X first
#define Y second

#define MP make_pair

#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)


typedef pair<int,int> pint;
typedef map<int,int> mint;

#define SIZE 2100

double naomi[SIZE];
double ken[SIZE];

vector< pair<double,int> > tmp;

int main(){

    freopen("D-large.in","r",stdin);
    freopen("out.out","w",stdout);

    //FRO

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){
        int n;
        scanf("%d",&n);
        tmp.clear();

        for (int i=0;i<n;++i){
            scanf("%lf",&naomi[i]);
            tmp.PB( MP( naomi[i],0 ) );
        }
        for (int i=0;i<n;++i){
            scanf("%lf",&ken[i]);
            tmp.PB( MP( ken[i],1 ) );
        }

        sort( tmp.begin(),tmp.end() );
        int score=0;
        for (int i=0;i<tmp.size();++i){
            if ( tmp[i].Y == 0 ){
                score++;
            }else{
                score--;
            }
            if ( score<0 ){
                score=0;
            }
        }

        sort( naomi,naomi+n );
        sort( ken,ken+n );

        deque<double> x,y;

        for (int i=0;i<n;++i){
            x.PB( naomi[i] );
        }

        for (int i=0;i<n;++i){
            y.PB( ken[i] );
        }
        /*
        for (int i=0;i<n;++i){
            printf(" %.3lf",x[i]);
        }printf("\n");
        for (int i=0;i<n;++i){
            printf(" %.3lf",y[i]);
        }printf("\n");
        */

        int ans = 0;
        for (int i=0;i<n;++i){

            double xback= x.back();
            double yback= y.back();

            if ( xback<yback ){
                y.pop_back();
                x.pop_front();
            }else{
                double yfront=y.front();
                //bool ok=false;
                for ( deque<double>::iterator it = x.begin() ; it != x.end();++it ){
                    if ( (*it) > yfront ){
                        y.pop_front();
                        x.erase( it );
                        ans++;
                        //ok=true;
                        break;
                    }
                }
                //if ( !ok )exit(5);
            }

        }


        printf("Case #%d: %d %d\n",kk,ans,score);

    }


    return 0;
}

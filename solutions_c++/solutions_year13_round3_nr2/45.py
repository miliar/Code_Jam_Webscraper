#define ll __int64
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

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
#include <cstring>
#include <queue>
#include <cassert>


using namespace std;



#define off 2000


bool vst[ 5007 ][ 5007 ];
int d[ 5007 ][ 5007 ];
int p[ 5007 ][ 5007 ];

int dx[]={+1,-1,0,0};
int dy[]={0,0,+1,-1};




char dir[]={ 'E','W','N','S' };


void go(int x,int y)
{
    if( x==off && y==off )
    {
        return;
    }


    int i=p[x][y];
    int nx=x+d[x][y]*(-dx[i]);
    int ny=y+d[x][y]*(-dy[i]);



    go( nx,ny );

    printf("%c",dir[i]);
    return;

}

int main()
{
    int i,j,k,ks,T,X,Y,x,y;


  //  filer();


    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.txt","w",stdout);


    scanf("%d",&T);


    FOR(ks,1,T)
    {

        scanf("%d%d",&X,&Y);


//        cout<<X<<" "<<Y<<endl;

        X+=off;
        Y+=off;



        SET(vst,0);
        queue<int>qx,qy;



        qx.push( off );
        qy.push( off );




        vst[ off ][ off ]=1;
        d[off][off]=0;


        int x1,y1;

        while(!qx.empty())
        {

            x=qx.front();
            y=qy.front();



         //   cout<<x-off<<" "<<y-off<<endl;



            if( x==X && y==Y )break;


            qx.pop();
            qy.pop();





            REP(i,4)
            {

                x1=x+dx[i]*(d[x][y]+1);
                y1=y+dy[i]*(d[x][y]+1);



                if( vst[ x1 ][ y1 ] )continue;
                vst[x1][y1]=true;


                qx.push( x1 );
                qy.push( y1 );

                p[x1][y1]=i;
                d[x1][y1]=d[x][y]+1;

            }




        }


       // cout<<d[X][Y]<<endl;

		printf("Case #%d: ",ks);
        go( X,Y );
		printf("\n");








    }


    return 0;

}

#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <memory.h>
#include <queue>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits.h>
#include <cstdlib>
#include <stack>
#define sc(x) scanf("%d",&x);
#define pr(x) printf("%d \n",x);
#define scll(x) scanf("%lld",&x);
#define prll(x) printf("%lld \n",x);

using namespace std;

ifstream fin ("input.txt");
ofstream fout ("output.txt");
int main()
{
    int tc,cas=1;
    fin>>tc;
    int x,r,c,R,C;
    string gab="GABRIEL",ric="RICHARD",ans;
    while(tc--)
    {
        fout<<"Case #"<<cas++<<": ";
        fin>>x>>R>>C;
        r=min(R,C);c=max(R,C);
        int tem=(r*c)/x;

        if( tem*x != r*c ){
            ans=ric;
        }
        else{
            if(x==1) ans=gab;
            else if(x==2) ans=gab;
            else if(x==3){
                if(r==1) ans=ric;
                else ans=gab;
            }
            else if(x==4){
                if(r==1) ans=ric;
                else if(r==2) ans=ric;
                else if(r==3) ans=gab;
                else if(r==4) ans=gab;
            }
        }
        fout<< ans<<endl;
    }
}

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
    long long n,chk,x;n=1;
    while(tc--)
    {
        fout<<"Case #"<<cas++<<": ";
        fin>>n;
        if(n==0){
            fout<<"INSOMNIA\n";
            continue;
        }
        int i=0;
        chk = 1023;
        while(chk){
            x=n*(++i);
            while(x){
                chk &= (1023^(1<<(x%10))) ;
                x /= 10;
            }
        }
        //cout<<n*i<<endl;
        fout<<n*i<<endl;
        n++;
    }
}

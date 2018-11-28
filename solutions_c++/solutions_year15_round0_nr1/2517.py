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
    string s;
    int n;
    while(tc--)
    {
        fin>>n>>s;
        n++;
        long long k=s[0]-'0',x=0;
        for(int i=1;i<n;i++){
           int tem = s[i]-'0';
            if( k < i ){
                x += i - k;
                k = i + tem;
            }
            else k += tem;
        }

        fout<<"Case #"<<cas++<<": ";
        fout<<x<<endl;
    }
}

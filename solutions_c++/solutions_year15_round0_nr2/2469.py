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
int A[1010];
int B[1001];
int main()
{
    int tc,cas=1;
    fin>>tc;
    int n;
    while(tc--)
    {
        fin>>n;
        int sum=0;
        for(int i=0;i<n;i++){
            fin>>A[i];
            sum += A[i];
        }
        fout<<"Case #"<<(cas++)<<": ";
        if(sum == 0){
            fout<<0<<endl;
            continue;
        }
        memset(B,0,sizeof B);
        for(int i=1;i<1001;i++){
            for(int j=0;j<n;j++){
                int temp = A[j] / i;
                if( temp*i != A[j] ) temp++;
                temp--;
                B[i] += temp;
            }
            B[i] += i;
        }
        int ans=1000000000;
        for(int i=1;i<1001;i++){
            if(B[i] < ans && B[i] > 0) ans = B[i];
        }
        fout<<ans<<endl;
    }
}

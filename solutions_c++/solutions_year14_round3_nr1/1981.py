#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#define INF 2147483647
#define NINF -2147483647
#define pb push_back
#define mp make_pair
#define LL long long
#define f(i,n) for(int i=0;i<n;i++)
#define fd(i,n) for(int i=n-1;i>=0;i--)
#define cmp(str1,str2) str1.compare(str2)
#define vpair vector < pair <int , int> >
using namespace std;
main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    bool win = false;
    for(int t=1;t<=T;t++){
        int P,Q;
        int counter = 1;
        scanf("%d/%d",&P,&Q);
        double f = P/(double)Q;
        double x;
        while(f<1){
            x = f*2 - 1;
            if(x>=0 && x <= 1){
                win = true;
                break;
            }
            f*=2;
            counter++;
        }
        //cout << counter << endl;
        //cout << log2(Q) << "\t" << (int)(log2(Q)) << endl;
        if(log2((double)Q)!=(int)log2((double(Q))))
            win = false;
        printf("Case #%d: ",t);
        if(win)
            printf("%d\n",counter);
        else
            printf("impossible\n");
    }
}

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
using namespace std;
#define VISITED 2
#define EXPLORED 1
#define UN_VISISTED 0

typedef unsigned long long ull;
typedef unsigned long ul;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main(){
    freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    int T,tcase=1;
    cin>>T;
    while(T--){
        int N;
        cin>>N;
        char c;
        scanf(" ");
        long cnt = 0;
        long result = 0;
        for(int i=0;i<=N;i++){
            scanf(" %c",&c);
            int tmp = c-'0';
            if(tmp!=0){

                if(i>cnt){
                    result += (i-cnt);
                    cnt+=(i-cnt)+tmp;
                }else{
                    cnt+=tmp;
                }
            }

        }
        getchar();
        printf("Case #%d: %ld\n",tcase++,result);
    }
    return 0;
}
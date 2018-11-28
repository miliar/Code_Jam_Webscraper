#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<string.h>
#include<cstring>
#include<iostream>

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pin;
typedef std::pair<int,std::pair<int, int> > ppin;
using namespace std;

int main(){
    freopen("/Users/shitian/Desktop/A-large.in","r",stdin);
    freopen("/Users/shitian/Desktop/out.txt","w",stdout);
    int tcase;
    scanf("%d", &tcase);
    for(int tca = 1; tca <= tcase; tca++){
        printf("Case #%d: ",tca);
        
        int ans=0;
        int Sm;
        scanf("%d ", &Sm);
        int S[2000];
        char n;
        for(int i=0;i<=Sm;i++){
            scanf("%c", &n);
            S[i] = n - '0';
            
        }
        printf("\n");
        int now=0;
        for(int i=0;i<=Sm;i++){
            if(i <= now){
                now += S[i];
            }
            else{
                ans += i - now;
                //cout<<"i: "<<i<<"    now: "<<now<<"  ans: "<<ans<<endl;
                now += i - now + S[i];
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
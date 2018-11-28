#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<cmath>
using namespace std;
#define PB push_back
#define PPB pop_back
#define MP make_pair
#define LL long long
#define ULL unsigned long long
#define fs first
#define sc second
#define pii pair<int,int>
#define pll pair<LL,LL>
#define ppii pair< pii,int >
#define BIG 2000000000

void gabriel() {printf("GABRIEL\n");}
void richard() {printf("RICHARD\n");}

int kasus,x,r,c;

int main()
{
//    freopen("D-small-attempt1.in","r",stdin);
//    freopen("d.out","w",stdout);
    
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++) {
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: ",z);
        if ((r*c) % x != 0) richard();
        else if (x<=2) gabriel();
        else if (x==3) {
            if (r==1 || c==1) richard();
            else gabriel();
        } else {
            if (r==2 && c==2) richard();
            else if (r>=3 && c>=3) gabriel();
            else richard();
        }
    }
    
//    fclose(stdin);
//    fclose(stdout);
    return 0;
}

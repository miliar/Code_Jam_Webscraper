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

using namespace std;

int main(){
    int x,r,c;
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	int cases;
	scanf("%d", &cases);
    for(int i=0;i<cases;i++){
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: ",i+1);
        if((r*c)%x||x==4||(x==3&&(r*c)%2==1)){
            printf("RICHARD\n");
        }else{
            printf("GABRIEL\n");
        }
    }
}

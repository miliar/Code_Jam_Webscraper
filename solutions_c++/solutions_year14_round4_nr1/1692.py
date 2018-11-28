#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string.h>
using namespace std;
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)<(b))?(b):(a))
#define ABS(x) (((x)<0)?(-(x)):(x))

int cnt[701];
int n,c;


int getMinimum(){
    int needed=1;
    int total=0;
    int inthis=0;
    while(n>0){
        int sel=-1;
        for(int i=c;i>=1;--i)if(cnt[i]>0){
            if(sel<0){
                sel = i;
            }
            if(i+total<=c){
                sel = i;
                break;
            }
        }
        cnt[sel]--;

        if((inthis<2) && (total+sel<=c)){
            total+=sel;
            ++inthis;
        }else{
            needed++;
            total=sel;
            inthis = 1;
        }
        --n;
    }
    return needed;
}

int main(int argc, char *argv[]){
    int T;
    cin >> T;
    for(int cc=1;cc<=T;++cc){
        cin>>n>>c;
        memset(cnt,0,sizeof(cnt));
        for(int i=0;i<n;++i){
            int s;
            cin>>s;
            cnt[s]++;
        }
        int sol = getMinimum();
        cout<<"Case #"<<cc<<": "<<sol<<endl;
    }
	return 0;
}

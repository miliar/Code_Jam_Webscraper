#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <iostream>
#include <string>
#include <array>
#include <regex>


using namespace std;

#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rendr()
#define sz(v) ((int)v.size())
#define read(x) scanf("%d",&(x))
#define read2(x, y) scanf("%d %d",&(x),&(y))
#define read3(x, y, z) scanf("%d %d %d",&(x),&(y),&(z))

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;
typedef long double ld;
int arr[10];
int num;

bool valid(int i, bool take){
vector<int> heap(arr,arr+num);
make_heap(all(heap));
while(i>=0 && heap.front() > i){
      pop_heap(all(heap));
        int element = heap.back();
        heap.pop_back();
int left = element/2;
int right = element - left;
if((left%2 == 0 && right%2 == 0) || (left%2 != 0 && right%2 != 0)){
heap.push_back(left); push_heap (all(heap));
heap.push_back(right); push_heap (all(heap));
i-=1;
continue;
}
else{
if(right % 2 == 0 || take ){
heap.push_back(left); push_heap (all(heap));
heap.push_back(right); push_heap (all(heap));
i-=1;
continue;
}
else{
    left +=2 ;
    right-=2;
    heap.push_back(left); push_heap (all(heap));
heap.push_back(right); push_heap (all(heap));
i-=1;
continue;
}
}
}

if(heap.front() == i){
    return true;
}

return false;
}



int main(){
freopen("in.txt", "r",stdin);
freopen ("out.txt","w",stdout);
int i = 1;
int n;
read(n);
while(n--){

read(num);
for(int k=0;k<num;k++){
    read(arr[k]);
}
for(int l=1;l<50;l++){
if(valid(l,true) || valid(l,false)){
    printf("Case #%d: %d\n",i++,l);
    break;
}
}
}
return 0;
}

// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 10000;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

char total_str[M + 5];
struct Quat {
    int w,x,y,z;

    Quat() {}

    Quat(int w, int x, int y, int z) {
        this->w = w;
        this->x = x;
        this->y = y;
        this->z = z;
    }
};

Quat running_product[M];
Quat mul(Quat q1,Quat q2) {

    int w = (q1.w*q2.w - q1.x*q2.x - q1.y*q2.y - q1.z*q2.z);
    int x = (q1.w*q2.x + q1.x*q2.w + q1.y*q2.z - q1.z*q2.y);
    int y = (q1.w*q2.y - q1.x*q2.z + q1.y*q2.w + q1.z*q2.x);
    int z = (q1.w*q2.z + q1.x*q2.y - q1.y*q2.x + q1.z*q2.w);


    return Quat(w,x,y,z);
}

Quat get_quat(char x) {

  if(x == '1') return Quat(1,0,0,0);
  if(x == 'i') return Quat(0,1,0,0);
  if(x == 'j') return Quat(0,0,1,0);
  if(x == 'k') return Quat(0,0,0,1);

  return Quat(0,0,0,0);
}

bool eql(Quat q1, Quat q2) {
    return q1.w == q2.w &&
        q1.x == q2.x &&
        q1.y == q2.y &&
        q1.z == q2.z;
}

void print(Quat q) {
    printf("%d %d %d %d\n",q.w,q.x,q.y,q.z);
}


int main() {

    int tc;
    scanf("%d", &tc);
    for(int t=1;t<=tc;++t) {
        int L,X;
        scanf("%d %d",&L,&X);

        char curr_str[L + 5];
        scanf("%s",curr_str);

        total_str[0] = '\0';

        for(int i = 0;i<X;++i) strcat(total_str, curr_str);

        int total_length = L * X;

        running_product[0] = get_quat(total_str[0]);
        for(int i=1;i<total_length;++i) {
            running_product[i] = mul(running_product[i-1] , get_quat(total_str[i]));
        }

        bool found_i= false;
        bool found_ij = false;

        for(int i = 0; i< total_length; ++i) {
            if(eql(running_product[i], get_quat('i'))) found_i = true;

            if(found_i && eql(running_product[i], get_quat('k'))) found_ij = true;
        }
        bool possible = found_ij && eql(running_product[total_length - 1], Quat(-1,0,0,0));

        printf("Case #%d: %s\n",t, (possible ? "YES" : "NO"));

    }
    return 0;
}


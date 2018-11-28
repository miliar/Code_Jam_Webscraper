#include <algorithm>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

typedef long long i64;
typedef vector<bool> bvec;
typedef vector<string> svec;
typedef vector<int> ivec;

int T, N, tmp, oneCounter, oneIndex;
bool finish, onlyOneLeft;
ivec P;
string result;

int main() {
    
    freopen("A-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    
    scanf("%d",&T);
    F1(t, T) {
        scanf("%d",&N);
        result = "";
        P.clear();
        F0(i,N) {
            scanf("%d",&tmp);
            P.push_back(tmp);
        }
        while(true) {
            finish = true;
            int max = 0;
            int maxIndex = -1;
            int next = 0;
            int nextIndex = -1;
            F0(i,N) {
                if(P[i] > max) {
                    max = P[i];
                    maxIndex = i;
                } else if(P[i] > next) {
                    next = P[i];
                    nextIndex = i;
                }
            }
            onlyOneLeft = true;
            oneCounter = 0;
            F0(i,N) {
                if(P[i] > 1) {
                    onlyOneLeft = false;
                }
                if(i != maxIndex && i != nextIndex && P[i] == 1) {
                    oneCounter++;
                    oneIndex = i;
                }
            }
            if(onlyOneLeft && oneCounter == 1) {
                result+=65+oneIndex;
                P[oneIndex]--;
                result+=" ";
            }
            if(max >= 0) {
                result+=65+maxIndex;
                P[maxIndex]--;
            }
            if(nextIndex >= 0) {
                result+=65+nextIndex;
                P[nextIndex]--;
            }
            result+=" ";
            F0(i,N) {
                if(P[i] != 0) {
                    finish = false;
                    break;
                }
            }
            if(finish) break;
        }
        printf("Case #%d: %s\n", t, result.c_str());
    }
    return 0;
}
#include <cstdio>
#include <set>
using namespace std;

const int L = 1e7;

int main(){
    freopen("A-large.in","r",stdin); freopen("A-large.txt","w",stdout);

    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i){
        int n;
        scanf("%d", &n);
        if(n == 0)
            printf("case #%d: INSOMNIA\n", i);
        else {
            set<int> digits;
            int j;
            for(j = n; j <= L; j += n){
                int a = j;
                while(a){
                    digits.insert(a % 10);
                    a /= 10;
                }
                if(digits.size() == 10){
                    printf("case #%d: %d\n", i, j);
                    break;
                }
            }
        }
    }

    return 0;
}

#include <cstdio>
#include <set>

using namespace std;
int main(){
    int n, in;
    set<int> digit;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &in);
        if(in == 0) printf("Case #%d: INSOMNIA\n", i + 1);
        else {
            int t;
            for(int j = 1; digit.size() < 10; j++) {
                int tmp = j * in;
                t = tmp;
                do {
                    int temp = tmp % 10;
                    digit.insert(temp);
                    tmp /= 10;
                } while(tmp);
            }
            printf("Case #%d: %d\n", i + 1, t);
            digit.clear();
        }
    }
}

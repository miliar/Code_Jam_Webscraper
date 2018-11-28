#include <stdio.h>
#include <set>

int main(void){

    std::set<int> myset;

    int N = 0;
    int count = 0;
    scanf("%d", &count);

    for (int c = 0; c < count; c++){
        scanf("%d", &N);
        myset.clear();
        
        if (N == 0){
            printf("Case #%d: INSOMNIA\n", (c+1));
        }
        else {
            int k = 1;
            int last;

            while (myset.size() != 10){

                int n = N * k;
                last = n;

                while (n != 0) {
                    int reminder = n % 10;
                    myset.insert(reminder);
                    n = n / 10;
                }

                k++;
            }
            printf("Case #%d: %d\n", (c+1), last);
        }
    }

    return 0;
}

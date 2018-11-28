#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
    int TC, N, m;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        scanf("%d", &N);
        int have1 = 0, eaten1 = 0;
        int step2 = 0, eaten2 = 0;
        int arr[N];
        int maxim = 0;
        for(int n = 0; n < N; n++){
            scanf("%d", &m);
            arr[n] = m;
            maxim = max(maxim, m);
            if(m < have1) eaten1 += have1 - m;
            have1 = m;
        }

        for(int i = 0; i <= maxim; i++){
            bool valid = true;
            for(int n = 0; n < N - 1; n++){
                if(arr[n + 1] < arr[n] - i){
                    valid = false;
                    break;
                }

            }
            if(valid){
                step2 = i;
                break;
            }
        }

        for(int n = 0; n < N - 1; n++){
            int eat = min(step2, arr[n]);
            eaten2 += eat;
        }


        printf("Case #%d: %d %d\n", c, eaten1, eaten2);
    }
}


/*
#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
    int TC, N, m;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        scanf("%d", &N);
        int have1 = 0, eaten1 = 0;
        int step2 = 0, eaten2 = 0;
        int arr[N];
        for(int n = 0; n < N; n++){
            scanf("%d", &m);
            arr[n] = m;
            if(m < have1) eaten1 += have1 - m;
            have1 = m;
        }

        for(int n = 0; n < N; n++){
            if(n < N - 2) step2 = max(step2, arr[n]);
            else step2 = max(step2, arr[n] - arr[N - 1]);
        }

        for(int n = 0; n < N - 1; n++){
            int eat = min(step2, arr[n]);
            eaten2 += eat;
        }

        printf("Case #%d: %d %d\n", c, eaten1, eaten2);
    }
}
*/

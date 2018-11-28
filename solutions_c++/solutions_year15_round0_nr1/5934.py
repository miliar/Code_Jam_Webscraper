#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("lou.txt", "w", stdout);

    int t, s=0;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        char str[n+1];
        scanf("%s", str);

        int count = 0, fr = 0, ad, num;
        for(int i=0; str[i]; i++){
            num = str[i] - '0';
            if(i <= count) count+=num;
            else{
                ad = i - count;
                fr += ad;
                count += ad + num;
            }
        }

        printf("Case #%d: %d\n", ++s, fr);

    }

    return 0;
}

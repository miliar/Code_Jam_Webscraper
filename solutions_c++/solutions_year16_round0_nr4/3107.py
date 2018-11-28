#include <iostream>

using namespace std;

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int times;
    cin >> times;
    for (int time = 1; time <= times; time ++)
    {
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        long long gap = 1;
        for (int i = 0; i < c-1; i++)
        {
            gap = gap * k + 1;
        }

        printf("Case #%d:",time);
        if (k == s){
            long long currpos = 1;
            for (int i = 0; i < s; i++)
            {
                cout << ' ' <<  currpos ;
                currpos += gap;
            }
            printf("\n");
        }
        else{
            printf(" Impossible\n");

        }
    }
}
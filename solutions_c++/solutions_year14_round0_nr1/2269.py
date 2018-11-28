
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>

using namespace std;

int b1[4][4];
int b2[4][4];
int a1,a2;

int hasWon() {
    int ans,count=0;
    int a[8];
        int arr[8];
        for(int j=0;j<4;j++)
                {
                    a[j]=b1[a1-1][j];
                    a[j+4]=b2[a2-1][j];
                }
        for(int i=0;i<8;i++)
        {
            for(int j=i+1;j<8;j++)
                {
                    if(a[i]==a[j])
                        {   count++;
                            ans=a[i];
                        }
                }
        }
    if(count==0)
        return 0;
    else if(count>1)
        return -1;
    else
        return ans;


}

int main() {
    freopen("A-small.in", "r", stdin);
    freopen("small.txt", "w", stdout);
    int T;
    char ans[30];

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {

        scanf("%d", &a1);

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d", &b1[i][j]);

        scanf("%d", &a2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d", &b2[i][j]);

        int x=hasWon();
        if(x==-1)
                strcpy(ans,"Bad magician!");
        else if(x==0)
                strcpy(ans,"Volunteer cheated!");
        else
                itoa(x,ans,10);

        printf("Case #%d: %s\n", t, ans);
    }

	return 0;
}

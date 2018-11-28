#include <stdio.h>

int main()
{
    int t,n,m;
    int a[4][4], b[4][4];

    scanf("%d", &t);
    for(int i=0; i<t; i++){
        printf("Case #%d: ", i+1);
        scanf("%d", &n);
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                scanf("%d", &a[j][k]);
            }
        }
        scanf("%d", &m);
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                scanf("%d", &b[j][k]);
            }
        }

        int q=0;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                if(b[m-1][k]==a[n-1][j])
                    q++;
            }
        }

        if(q>1)
            printf("Bad magician!\n");
        else if(q==0)
            printf("Volunteer cheated!\n");
        else
        {
            for(int j=0; j<4; j++){
                for(int k=0; k<4; k++){
                    if(b[m-1][k]==a[n-1][j])
                        printf("%d\n", a[n-1][j]);
                }
            }
        }

    }

}

#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    int t;

    int R1,R2,arr[4][4],array[4][4],j,k,ar[4],arra[4],sol,number;

    cin>>t;

    for(int i=1; i<=t;i++) {
        sol=0;
        cin>>R1;
        for(j=0;j<4;j++) for(k=0;k<4;k++) cin>>arr[j][k];
        for(j=0;j<4;j++) ar[j]=arr[R1-1][j];
        cin>>R2;
        for(j=0;j<4;j++) for(k=0;k<4;k++) cin>>array[j][k];
        for(j=0;j<4;j++) arra[j]=array[R2-1][j];
        for(j=0;j<4;j++) {
            for(k=0;k<4;k++){
                if(ar[j] == arra[k]) {
                    sol++;
                    number=ar[j];
                }
            }
		}
        if(sol == 1) {
            printf("Case #%d: %d\n",i,number);
        } else if(sol ==0) {
            printf("Case #%d: Volunteer cheated!\n",i);
        } else {
            printf("Case #%d: Bad magician!\n",i);
        }
    }
    return 0;
}






#include<bits/stdc++.h>
using namespace std;

main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,c=1;
    scanf("%d",&t);
    while(t--){
        int r,cnt=0,n1,n2,arr1[5][6],arr2[5][6];
        scanf("%d",&n1);
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                scanf("%d",&arr1[i][j]);
            }
        }
        scanf("%d",&n2);
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                scanf("%d",&arr2[i][j]);
            }
        }
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                    if(arr1[n1][i]==arr2[n2][j]){
                        cnt++;
                        r=arr1[n1][i];
                        arr1[n1][i]=-1;
                    }
            }
        }
        if(cnt==1)printf("Case #%d: %d\n",c++,r);
        else if(cnt>1)printf("Case #%d: Bad magician!\n",c++);
        else printf("Case #%d: Volunteer cheated!\n",c++);
    }
}

#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
    freopen("m1.in","r",stdin);
    freopen("k.out","w",stdout);

int t,a1,a2,i,j,z=0;
int mat1[5][5],mat2[5][5];
cin>>t;
while(t--)
{   z++;
    int cnt=0,temp;
    cin>>a1;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin>>mat1[i][j];
        cin>>a2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>mat2[i][j];
    for(i=0;i<4;i++)
        {  for(j=0;j<4;j++){
            if(mat1[a1-1][i]==mat2[a2-1][j])
            {  temp=mat1[a1-1][i];
                cnt++;
            }

         }
         }
      if(cnt==0)
                printf("Case #%d: Volunteer cheated!\n",z);
      else if(cnt==1)
                printf("Case #%d: %d\n",z,temp);
      else
                printf("Case #%d: Bad magician!\n",z);


}
return 0;
}

#include <iostream>
#include<stdio.h>

using namespace std;

void magiccard(int t);
int main()
{
    int t,i;
    scanf("%d",&t);
    for(i=0;i<t;i++)
        magiccard(i);
    return 0;
}
void magiccard(int t)
{
    int a[4][4];
    int b[4][4];
    int n1,n2;
    int i,j,p;
    int c[4]={1,1,1,1};
    cin>>n1;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        scanf("%d",&a[i][j]);
    cin>>n2;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            scanf("%d",&b[i][j]);

    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[n1-1][i]==b[n2-1][j])
            {
                c[i]++;
//               cout<<"Element found at"<<j<<" element is :"<<a[n1-1][i]<<endl;
            }
        }
    }
/*
    for(i=0;i<4;i++)
        cout<<"c["<<i<<"]="<<c[i]<<endl;


    cout<<"p="<<p<<endl;
*/
p=c[0]*c[1]*c[2]*c[3];
    switch(p)
    {
    case 1:
        printf("Case #%d: Volunteer cheated!\n",++t);
        break;
    case 2:
        {
            for(i=0;i<4;i++)
                if(c[i]!=1)
                {
                    printf("Case #%d: %d\n",++t,a[n1-1][i]);
                }
                break;
        }
    default:
        printf("Case #%d: Bad magician!\n",++t);
    }
}

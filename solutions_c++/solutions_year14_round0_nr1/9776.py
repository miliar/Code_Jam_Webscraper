#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<stack>
#include<queue>
#include<vector>
using namespace std;
int a[4][4];
int b[4][4];
int a1[4];
int b1[4];

int main()
{
//    freopen("A-small-attempt1.in","r",stdin);
//    freopen("A-small-attempt0 - .out","w",stdout);
    int i,j,k,l;
    int kase=1;
    int T;
    cin>>T;
    while(T--)
    {
        int n1,n2;
        cin>>n1;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>n2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }
//        cout<<"<======================>"<<endl;
//        cout<<n1<<endl;;
//        for(i=0;i<4;i++)
//        {
//            for(j=0;j<4;j++)
//            {
//                cout<<a[i][j];
//            }
//            cout<<endl;
//        }
//        cout<<n2<<endl;;
//        for(i=0;i<4;i++)
//        {
//            for(j=0;j<4;j++)
//            {
//                cout<<b[i][j];
//            }
//            cout<<endl;
//        }
        memset(a1,0,sizeof(a1));
        memset(b1,0,sizeof(b1));
        printf("Case #%d: ",kase++);
//        cout<<n1<<"          "<<n2<<endl;
        for(i=0;i<4;i++)
        {
            a1[i]=a[n1-1][i];
            b1[i]=b[n2-1][i];
        }
//        for(i=0;i<4;i++)
//        {
//            cout<<a1[i];
//
//        }
//        cout<<endl;
//        for(i=0;i<4;i++)
//        {
//            cout<<b1[i];
//        }
        int count1=0;
        int num;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a1[i]==b1[j])
                    {
                        count1++;
                        num=a1[i];
                    }
            }
        }
        if(count1>1)
            printf("Bad magician!\n");
        else if(count1==0)
            printf("Volunteer cheated!\n");
        else if(count1==1)
            printf("%d\n",num);
    }
    return 0;
}

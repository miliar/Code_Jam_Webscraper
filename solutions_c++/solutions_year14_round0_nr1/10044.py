#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[10][10];
int b[10][10];
int row1,row2;
int main()
{
#ifdef LOCAL
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
#endif // LOCAL
    int ncase;
    scanf("%d",&ncase);
    int k = 1;
    while(ncase -- )
    {
        int flag = 0;
        cin>>row1;
        int cnt;
        for(int i = 1 ; i <= 4 ; i++)
        {
            for(int j = 1 ; j <= 4; j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>row2;
        for(int i = 1 ; i <= 4; i++)
        {
            for(int j = 1 ; j <= 4 ; j++)
            {
                cin>>b[i][j];
            }
        }
        for(int i = 1 ; i <= 4 ; i++)
        {
            for(int j = 1 ; j <= 4 ; j++)
            {
                if(a[row1][i] == b[row2][j])
                {
                    flag++;
                    cnt = i;
                }
            }
        }
        printf("Case #%d: ",k++);
        if(!flag)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else if(flag == 1)
        {
            cout<<a[row1][cnt]<<endl;
        }
        else
        {
            cout<<"Bad magician!"<<endl;
        }
    }
    return 0;
}

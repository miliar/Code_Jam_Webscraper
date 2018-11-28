#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int te;
    cin>>te;
    int contain[10][10];

    for(int t =1 ; t<=te  ; t++ )
    {
        int a;
        cin>>a;
        for(int i = 0 ; i<4 ; i++ )
            for(int j= 0 ; j< 4 ; j++ )
                cin>>contain[i][j];
        for(int i = 0 ; i< 4 ; i++ )
            contain[7][i] = contain[a-1][i];

        cin>>a;
        for(int i = 0 ; i<4 ; i++ )
            for(int j= 0 ; j< 4 ; j++ )
                cin>>contain[i][j];
        for(int i = 0 ; i< 4 ; i++ )
            contain[8][i] = contain[a-1][i];

        int cnt = 0 ;
        int number ;
        for(int i = 0 ; i< 4; i++ )
        {
            for(int j = 0 ; j< 4 ; j++ )
                if(contain[7][i] == contain[8][j])
                {
                    number = contain[8][j];
                    cnt++ ;
                }
        }
        printf("Case #%d: ",t);
        if(cnt==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(cnt >1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<number<<endl;


    }
    return 0;
}

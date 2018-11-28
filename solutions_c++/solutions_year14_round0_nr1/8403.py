#include<iostream>
using namespace std;


struct node{
    int f;
    int s;
}s[20];

int main(){

    int t,a[4][4],b[4][4],a1,a2,i,j;
    int tc;
    tc = 0;
    cin>>t;
    while(t--){

    cin>>a1;

    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin>>a[i][j] , s[ a[i][j] ].f = i;

    cin>>a2;

    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin>>a[i][j], s[ a[i][j] ].s = i;


    int count;
    count = 0;

    for(i=1;i<=16;i++)
        if( s[i].f == a1 - 1 && s[i].s == a2 - 1)
            count++;

            cout<<"Case #"<<++tc<<": ";

    if(count == 0 )
        cout<<"Volunteer cheated!"<<endl;
    else if (count == 1)
        {
            for(i=1;i<=16;i++)
                if( s[i].f == a1 - 1 && s[i].s == a2 - 1)
                    break;
            cout<<i<<endl;
        }
    else
        cout<<"Bad magician!"<<endl;



    }//t



}

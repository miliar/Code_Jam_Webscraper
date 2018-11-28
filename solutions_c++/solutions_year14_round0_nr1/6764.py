#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int a,b,c=0,d;
        cin>>a;
        int m[4][4];
        for(int x=0;x<4;x++)
            for(int y=0;y<4;y++)
            cin>>m[x][y];
        cin>>b;
        int n[4][4];
        for(int x=0;x<4;x++)
            for(int y=0;y<4;y++)
            cin>>n[x][y];
        for(int p=0;p<4;p++)
            for(int q=0;q<4;q++)
        {
            if(m[a-1][p]==n[b-1][q]){
                c++;
                d=m[a-1][p];
            }
        }
        if(c==0)
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        if(c==1)
            cout<<"Case #"<<i+1<<": "<<d<<endl;
        else if(c>1)
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    }
}

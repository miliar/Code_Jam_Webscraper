#include<stdio.h>
#include<iostream>
#include<queue>
using namespace std;
int card[17];
int maps[4][4];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.codeout","w",stdout);
    int t;
    cin>>t;
    for(int cnt=1;cnt<=t;cnt++)
    {
        int x;
        cin>>x;x--;
        for(int i=0;i<17;i++)card[i]=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>maps[i][j];
        for(int i=0;i<4;i++)card[maps[x][i]]++;

        cin>>x;x--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>maps[i][j];
        for(int i=0;i<4;i++)card[maps[x][i]]++;
        queue<int> q;
        for(int i=1;i<17;i++)if(card[i]==2)q.push(i);
        cout<<"Case #"<<cnt<<": ";
        if(q.size()==1)cout<<q.front()<<endl;
        else if(q.empty())cout<<"Volunteer cheated!"<<endl;
        else cout<<"Bad magician!"<<endl;
    }
}

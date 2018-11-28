#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream oyf("yes.txt");
    ifstream myf("sam.txt");
    if(myf.is_open()){
    int t,x=1;
    myf>>t;
    while(t--)
    {
        int flag[17]={0};
        int a[4][4];
        int p,y,i,j,k,c=0,ans;
        myf>>p;
        p--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                myf>>k;
                if(i==p)
                    flag[k]++;
            }
        myf>>y;
        y--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                myf>>a[i][j];
                if(i==y)
                    flag[a[i][j]]++;
            }
        for(i=0;i<4;i++)
            if(flag[a[y][i]]>=2)
            {
                c++;
                ans=a[y][i];
            }
        if(c==1)
            oyf<<"Case #"<<x++<<": "<<ans<<endl;
        else if(c<1)
            oyf<<"Case #"<<x++<<": "<<"Volunteer cheated!"<<endl;
        else
            oyf<<"Case #"<<x++<<": "<<"Bad magician!"<<endl;
    }}
    return 0;
}

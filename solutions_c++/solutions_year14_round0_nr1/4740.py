#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    int test,t,ans1,ans2,a1[5][5],a2[5][5],i,j,count,res;
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    cin >> test;
    t=1;
    while(t<=test)
    {
        cin >> ans1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin >> a1[i][j];
            }
        }
        cin >> ans2;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin >> a2[i][j];
            }
        }
        count=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a1[ans1][i]==a2[ans2][j])
                {
                    count++;
                    res=a1[ans1][i];
                    break;
                }
            }
        }
        cout << "Case #" << t << ": ";
        if(count==0)
            cout << "Volunteer cheated!" << endl;
        else if(count>1)
            cout << "Bad magician!" << endl;
        else
            cout << res << endl;
        t++;
    }
    return 0;
}

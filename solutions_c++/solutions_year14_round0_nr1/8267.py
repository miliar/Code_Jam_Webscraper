#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<stack>
using namespace std;
int main()
{
    freopen("input1.in", "r",stdin);
    freopen("o1.txt","w",stdout);
    int t,a1[4][4],a2[4][4],b[4],c[4],i,j,k=1,ans1,ans2,temp=0,sol;
    cin >> t;
    while(t--)
    {
        temp=0;
        cin >> ans1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin >> a1[i][j];
        for(j=0;j<4;j++)
            b[j]=a1[ans1-1][j];
        cin >> ans2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin >> a2[i][j];
        for(j=0;j<4;j++)
            c[j]=a2[ans2-1][j];
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(b[i]==c[j])
            {temp++;sol=b[i];}
        if(temp==1)cout << "Case #"  << k << ": " << sol;
        else if (temp>1) cout << "Case #" << k << ": Bad magician!";
        else if(temp==0) cout << "Case #" << k << ": Volunteer cheated!";
        else;
        k++;
        cout << "\n";
    }

    return 0;
}

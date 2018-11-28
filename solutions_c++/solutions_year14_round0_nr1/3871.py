#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>

using namespace std;
int a[5],b[5];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
    int t;
    cin>>t;
    int x;
    int r1,r2;
    for (int k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
        cin>>r1;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        {

        cin>>x;
        if (r1==i) a[j]=x;
        }
        cin>>r2;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        {
            cin>>x;
            if (r2==i) b[j]=x;
        }
        int count=0;
        for (int i=1; i<=4;i++)
        for (int j=1;j<=4;j++)
        {
            if (a[i]==b[j])
            {
                x=a[i];
                count++;
            }
        }
        if (count==1) cout<<x<<endl;
        else if (count>1) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}

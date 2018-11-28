////////////////////////////////////////////////////////////
// authour: amr eldfrawy
//////////////////////////////////////////////////////////////

#include <stdio.h>
#include <cstring>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<cstring>
#include<math.h>
using namespace std;

int main()
{
     freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout);



    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        int x1=0,y1=0;
        int x,y;
        cin>>x>>y;
        printf("Case #%d: ",i);

        while(x1!=x)
        {
            if(x>x1)
            {
                cout<<"WE";
                x1++;
            }

            if(x1>x)
            {
                cout<<"EW";
                x1--;
            }
        }
        while(y1!=y)
        {
            if(y>y1)
            {
                cout<<"SN";
                y1++;
            }

            if(y1>y)
            {
                cout<<"NS";
                y1--;
            }
        }
        cout<<endl;
    }

    return 0;
}

#include <iostream>
#include<cmath>
#include<cstdio>
#include<cstring>

using namespace std;
int arr[15];
int main()
{
     freopen("in.txt", "r", stdin);
     freopen("out.txt", "w", stdout);
     int tt,n,x,y,k,c;
     scanf("%d",&tt);
     for (int qq=1;qq<=tt;qq++)
     {
        printf("Case #%d: ",qq);
        scanf("%d %d %d",&x,&y,&k);
        int c=0;
        for (int i=0;i<x;i++)
        {
            for(int j=0;j<y;j++)
            {
                int t=i&j;
                //cerr<<t<<"  "<<k<<endl;
                if(t<k)
                    c++;
            }
        }
            printf("%d\n",c);
    }

        return 0;
}

#include <iostream>
#include<cmath>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
     freopen("in.txt", "r", stdin);
     freopen("out.txt", "w", stdout);

     int tt,qq;
     scanf("%d",&tt);
     for (int qq=1;qq<=tt;qq++)
     {
        int r=0,n,c=0,fr=0;
        char arr[1004];
        printf("Case #%d: ",qq);
        scanf("%d",&n);
        scanf("%s",arr);
        for(int i=0;arr[i];i++)
        {
            int x=arr[i]-48;
            //cout<<x<<"\n";
            if(c>=i)
                c+=x;
            else if(x>0)
            {
                r=(i-c);
                fr+=r;
                c+=(x+r);
            }
        }
            //cerr<<fr;
            printf("%d\n",fr);
    }

        return 0;
}

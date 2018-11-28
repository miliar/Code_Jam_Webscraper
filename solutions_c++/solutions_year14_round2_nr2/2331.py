#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int q=1;q<=t;q++)
    {
        int a,b,k;
        int res=0;
        cin >> a >> b >> k;
        for(int i=0;i<a;i++)
        for(int j=0;j<b;j++)
            if((i&j)<k)
            {
                res++;
            }
        cout << "Case #"<<q<<": "<<res<<endl;
    }
    return 0;
}

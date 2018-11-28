#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        char a[1055];
        scanf("%s",a);
        int l=strlen(a);
        deque<char>d;
        d.push_back(a[0]);
        for(int i=1;i<l;i++)
        {
            if(d.front()>a[i])d.push_back(a[i]);
            else d.push_front(a[i]);
        }
        printf("Case #%d: ",ca);
         while (!d.empty())
        {
            //std::cout << ' ' << d.front();
            printf("%c",d.front());
            d.pop_front();
        }
        printf("\n");
    }

    return 0;

}

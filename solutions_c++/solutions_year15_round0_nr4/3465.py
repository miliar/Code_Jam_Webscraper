#include<bits/stdc++.h>
#define D 1000000007
#define gcd __gcd
#define getcx getchar
#define pc putchar
#define get(x) scanf("%d",&x)
#define getl(x) scanf("%lld",&x)
#define print(x) printf("%d\n",x)
#define printl(x) printf("%lld\n",x)
#define bitcount __builtin_popcount
using namespace std;
typedef long long ll;
int main()
{
    int t,i,j; get(t);
    for(j=1;j<=t;j++)
    {
        int x,r,c; get(x);get(r);get(c);
        cout << "Case #" << j << ": ";
        if(x==1)
            cout << "GABRIEL";
        else if(x==2)
        {
            if((r*c)%2)
                cout << "RICHARD";
            else
                cout << "GABRIEL";
        }
        else if(x==3)
        {
            if(r==1)
                cout << "RICHARD";
            else if(r==2)
            {
                if(c==3)
                    cout << "GABRIEL";
                else
                    cout << "RICHARD";
            }
            else if(r==3)
            {
                if(c!=1)
                    cout << "GABRIEL";
                else
                    cout << "RICHARD";
            }
            else
            {
                if(c!=3)
                    cout << "RICHARD";
                else
                    cout << "GABRIEL";
            }
        }
        else
        {
            if((r==3 && c==4)||(r==4 && c==3)||(r==4 && c==4))
                cout << "GABRIEL";
            else
                cout << "RICHARD";
        }
        cout << endl;
    }
    return 0;
}



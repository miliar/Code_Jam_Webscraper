#include<iostream>
#include<cstdio>
using namespace std;
int main ()
{
    freopen("C-small-attempt0.in", "r",stdin);
    freopen("out.txt", "w", stdout);
    int T,caseno = 1;
    cin >> T;
    while(T--)
    {
        int l, h, a[] = {1, 4, 9, 121, 484}, c = 0 ;
        cin >> l >> h;
        for(int i =0; i<5; i++)
        {
            if(a[i]>=l && a[i]<=h)
            {
                c++;
            }
        }
        cout<<"Case #"<<caseno<<": "<<c<<endl;
        caseno++;
    }
    return 0;
}

#include<bits/stdc++.h>
#include<deque>
#include<iterator>


using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ggA.out","w",stdout);
    int i,j,k,l,m,T,t=1;
    char a[1010],b;
    deque <char >d;

    cin >> T;

    while(T--)
    {
        cin >> a;
        d.push_back(a[0]);
        b =a[0];
        for(i=1;i<strlen(a);i++)
        {

            if(a[i]>=b)
            {
                d.push_front(a[i]);
                b=d[0];
            }
            else {
                d.push_back(a[i]);
            }

        }
        //Case #1: CAB
        cout <<"Case #" <<t << ": ";
        for(deque <char> ::iterator it= d.begin();it<d.end();it++)
        {
            cout <<*it;
        }
        cout <<endl;

       d.clear();
       t++;

    }

    return 0;
}

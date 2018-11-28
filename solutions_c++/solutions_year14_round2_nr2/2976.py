#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small.out","w",stdout);
    int test, a, b, c, k, count, CASE=0;
    cin >> test;
    while(test--)
    {

        cin >> a >> b >> k;

        count=0;

        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                c = i&j;

                if(c<k)
                {
                    count++;
                }
            }
        }

        cout << "Case #" << ++CASE << ": " << count << endl;

    }

    return 0;

}
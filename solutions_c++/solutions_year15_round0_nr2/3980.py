#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<limits>

using namespace std;

#define gi(n) scanf("%d",&n)

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("asdf_large.txt", "w", stdout);
    int cases;
    cin>>cases;
    int t = 1;
    while(cases--)
    {
        int d;
        gi(d);
        int p[d+5];
        for(int i=0; i<d; i++) gi(p[i]);
        sort(p, p+d, greater<int>());
        int max = p[0];
        int time = INFINITY;
        int m = 0;
        for(int i=1; i<=max; i++)
        {
            m = 0;
            for(int j=0; j<d; j++)
            {
                if(p[j]<=i)
                    break;
                //cout<<ceil(float(p[j])/float(i))<<"  ";
                m += (ceil(float(p[j])/float(i)) - 1);
                //cout<<m<<"  ";
            }
            if((m + i) < time)
                time = m + i;

        }
        cout<<"Case #"<<t++<<": "<<time<<endl;


    }
}


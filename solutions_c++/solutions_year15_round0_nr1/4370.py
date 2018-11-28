#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

#define gi(n) scanf("%d",&n)


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int cases;
    gi(cases);
    int x=1;
    while(cases--)
    {
        int smax;
        gi(smax);
        if(smax == 0)
        {
            cout<<"Case #"<<x<<": "<<"0"<<endl;
            x++;
            continue;
        }

        string s;
        cin>>s;

        int need = 0, prevSum = 0;

        for(int i=0; i<smax+1; ++i)
        {
            int num = s[i];
            num = num - 48;
            //cout<<num<<"    ";
            if(s[i] == 0) continue;

            if(prevSum <= i)
            {
                need += (i-prevSum);
                prevSum = prevSum + need;
            }
            prevSum += num;
        }

        cout<<"Case #"<<x<<": "<<need<<endl;
        x++;
    }
    return 0;
}


#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;

int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        OF << "Case #" << tt << ": ";
        int sum=0,n,x; IF >> n;
        pair <int,char> pp[n+3];
        for(int i=0;i<n;i++)
        {
            IF >> x; sum += x;
            pp[i] = make_pair(x,'A'+i);
        }

        while(sum>0)
        {
            sort(pp,pp+n);
            if(sum==3)
            {
                OF << "C AB"; break;
            }
            if(pp[n-2].first>0)
            {
                pp[n-1].first -= 1; pp[n-2].first -= 1;
                OF << pp[n-1].second << pp[n-2].second << " ";
            }
            else
            {
                pp[n-1].first -= 1; OF << pp[n-1].second;
            }
            sum=0;
            for(int i=0;i<n;i++)
                sum += pp[i].first;
        }
        OF << endl;
    }
    OF.close(); IF.close();
}



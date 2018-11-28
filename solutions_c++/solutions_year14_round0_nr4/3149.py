#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{
    ifstream in;
    in.open("D-large.in");
    ofstream out;
    out.open("D-small-attempt.out");
    int n;
    in>>n;
    double a[1008],b[1008];
    for (int cur=1;cur<=n;cur++){
        int N;
        in>>N;
        for (int i=0;i<N;i++)
            in>>a[i];
        for (int i=0;i<N;i++)
            in>>b[i];
        sort(a,a+N);
        sort(b,b+N);
        int y=0,z=0;
        int j=0,i=0;
        for (i=0;i<N;i++)
            for (;j<N;j++)
                if (a[i]<b[j])
                    {z++;j++;break;}
        z=N-z;
        int li=0;
        j=N-1;i=N-1;
        for (;j>=li;)
               if (a[j]>b[i])
                    {y++;j--;i--;}
                else {li++;i--;}
        out<<"Case #"<<cur<<": "<<y<<" "<<z;
        if (cur<n) out<<"\n";
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,l,i,p;
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");
    IF>>t;
    for(p=1;p<=t;p++)
    {
        long long int n,i,j=-1,c1=0,c2=0;
        IF>>n;
        long long int a[n];
        for(i=0;i<n;i++)
        {
            IF>>a[i];
        }
        for(i=0;i<n-1;i++)
        {
            j=max(j,a[i]-a[i+1]);
        }
        c2=(a[0]>=j)?j:a[0];
        for(i=1;i<n-1;i++)
        {
            c2+=(a[i]>=j)?j:a[i];
            if(a[i-1]-a[i]>=j)
                c1+=j;
            else if(a[i]<a[i-1])
                c1+=a[i-1]-a[i];
        }
        if(a[i-1]-a[i]>=j)
            c1+=j;
        else if(a[i]<a[i-1])
            c1+=a[i-1]-a[i];
        OF<<"Case #"<<p<<": "<<c1<<" "<<c2<<endl;
    }
    IF.close();
    OF.close();
    return 0;
}

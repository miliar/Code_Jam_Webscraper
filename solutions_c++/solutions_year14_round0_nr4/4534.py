#include <bits/stdc++.h>

using namespace std;

int main()
{
     freopen("A.in","r",stdin);
freopen("output.in","w", stdout);
    int t,C=1;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<C<<": ";

        int n,i,j,pnt=0;
        cin>>n;
        double a[1004],b[1004];
        for(i=0;i<n;i++) cin>>a[i];
        for(i=0;i<n;i++) cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        for(i=n-1,j=n-1;j>=0;j--)
        {
            if(a[i]>b[j])  i--;
            else
            {
                pnt++;
            }
        }
        pnt=n-pnt;
        cout<<pnt<<' ';
        pnt=0;
        for(i=n-1,j=n-1;i>=0;i--)
        {
            if(a[i]>b[j]) {pnt++;}
            else j--;
        }
        cout<<pnt<<endl;
        C++;
    }
    return 0;
}

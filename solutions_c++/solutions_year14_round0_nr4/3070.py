#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

#define DEBUG

int main()
{
    #ifdef DEBUG
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    #endif

    long long int tc,i,n,j,cnt1,cnt2,p,temp;
    double a[1000],b[1000],c[1000],d[1000];
    cin>>tc;
    for(p=1;p<=tc;p++) {
        cin>>n;
        cnt1=0;
        cnt2=0;
        for(i=0;i<n;i++) {
            cin>>a[i];
            c[i]=a[i];
        }
        for(i=0;i<n;i++) {
            cin>>b[i];
            d[i]=b[i];
        }
        sort(a,a+n);
        sort(b,b+n);
        sort(c,c+n);
        sort(d,d+n);
        for(i=0;i<n;i++) {
            for(j=0;j<n;j++) {
                if(b[j]<a[i]&&b[j]!=-1) {
                    cnt1++;
                    b[j]=-1;
                    a[i]=-1;
                    break;
                }
            }
        }
        j=n-1;
        temp=0;
        for(i=n-1;i>=0;i--) {
            if(c[i]>d[j]) {
                temp++;
                cnt2++;
            } else if(c[i]<d[j]) {
                j--;
            } if(temp>j) {
                break;
            }
        }
        cout<<"Case #"<<p<<": "<<cnt1<<" "<<cnt2<<endl;
    }
    return 0;
}

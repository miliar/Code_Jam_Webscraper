#include<iostream>
using namespace std;
int w,dw;
double a[1005],b[1005];
int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
            int n; cin>>n;
            w=dw=0;
            for(int j=0;j<n;j++) cin>>a[j];
            for(int j=0;j<n;j++) cin>>b[j];
            sort(a,a+n);
            sort(b,b+n);
            for(int j=n-1,k=n-1;j>=0&&k>=0;)
            {
                    if(a[j]>b[k]) {dw++;j--;k--;}
                    if(a[j]<b[k]) {k--;}
            }
            for(int j=0,k=0;j<n&&k<n;)
            {
                    if(a[j]>b[k]) {k++;}
                    if(a[j]<b[k]) {w++;k++;j++;}
            }
            w=n-w;
            cout<<"Case #"<<i+1<<": "<<dw<<" "<<w<<endl; 
    }
    return 0;
}

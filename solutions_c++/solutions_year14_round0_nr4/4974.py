#include<iostream>
#include<algorithm>

using namespace std;

int n;

int war (double A[10], double B[10]){
    int ret=0;
    int y=0;
    for(int i=0;i<n;i++){
        for(int j=y;j<n;j++){
            if(A[i]<B[j]){
                y=j+1;
                ret++;
                break;
            }
        }
        if(ret==0) break;
    }
    return n-ret;
}

int dwar(double A[10],double B[10]){
    int ret=0;
    for(int i=0;i<n;i++)
        if(A[i]<B[0]) ret++;
        else break;
    for(int j=n-(ret+1);j>=0;j--)
        if(B[j]>A[n-1]) ret++;
        else break;
    for(int k=ret;k<n;k++)
        if(A[k]<B[k-ret]) ret++;
    return n-ret;
}

int main(){
    int t, T=1,w,dw;
    double a[10],b[10];
    cin>>t;
    while(t!=0){
        cin>>n;
        for(int i=0;i<n;i++)    cin>>a[i];
        for(int i=0;i<n;i++)    cin>>b[i];
        sort(a,a+n);sort(b,b+n);
        w=war(a,b);
        dw=dwar(a,b);
        cout<<"Case #"<<T++<<": "<<dw<<" "<<w<<endl;
        t--;
    }
    return 0;
}

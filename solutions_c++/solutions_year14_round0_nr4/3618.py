#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;
int main(){
    int t,x,i,j,k,n,count;
    double a[1001],b[1001];
    cin>>t;
    for(x=1;x<=t;x++){
        count=0;
        int count2 =0;
        cin>>n;
        for(i=0;i<n;i++)
        cin>>a[i];
        for(i=0;i<n;i++)
        cin>>b[i];
        k=0;
        sort(a,a+n);
        sort(b,b+n);
        for(i=0;i<n;i++)
        for(j=k;j<n;j++){
            if(a[i]>b[j]){
                count++;
                k=j+1;
                break;
            }
         //   i++;
        }
        int n2=n;
        for(i=0;i<n2;i++)
        for(j=0;j<n;j++){
            if(a[i]<b[j]){
                for(k=j;k<n-1;k++){
                    b[k]=b[k+1];
                }
                n--;
                break;
            }
            else count2++;
        }
        cout<<"Case #"<<x<<": "<<count<<" "<<n<<endl;
    }
    return 0;
}

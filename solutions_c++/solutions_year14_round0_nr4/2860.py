#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
    int t,mm,n,i,j;
    cin>>t;
    double pp;
    for(mm=1;mm<=t;mm++){
        cin>>n;
        vector<double> kk(n),nn(n);
        for(i=0;i<n;i++){
            cin>>pp;
            nn[i]=pp;
        }
        for(i=0;i<n;i++){
            cin>>pp;
            kk[i]=pp;
        }
        sort(nn.begin(),nn.end());
        sort(kk.begin(),kk.end());
        i=0;j=0;
        int c1=0;
        while(i<n && j<n){
            if(nn[i]>kk[j]){
                c1++;i++;j++;
                //printf("%llf %llf",nn[i],kk[i]);
                //cout<<nn[i]<<"  "<<kk[j]<<endl;
            }
            else if(nn[i]<kk[j]){
                i++;
            }
        }
        int c2=0;
        i=0;j=0;
        while(i<n && j<n){
            if(nn[i]<kk[j]){
                c2++;i++;j++;
                //cout<<nn[i]<<"  "<<kk[j]<<endl;
               // printf("%llf %llf",nn[i],kk[i]);
            }
            else if(nn[i]>kk[j]){
                j++;
            }
        }
        printf("Case #%d: %d %d\n",mm,c1,n-c2);
    }
    return 0;
}

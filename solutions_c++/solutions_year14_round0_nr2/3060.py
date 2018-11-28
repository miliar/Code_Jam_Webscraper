#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int t,mm,j,i;
    cin>>t;
    double sum,ti,c,f,x,r,tp;
    for(mm=1;mm<=t;mm++){
        cin>>c>>f>>x;
        tp=999999999.0;
        for(j=0;;j++){
            sum=0;
            for(i=1;i<=j;i++){
                r=2+(i-1)*f;
                sum+=(c/r);
            }
            r=2+j*f;
            sum+=(x/r);
            //cout<<sum<<" ";
            if(sum<=tp)
                tp=sum;
            else
                break;
           // cout<<r<<" "<<sum<<endl;
        }
        printf("Case #%d: %.7llf\n",mm,tp);
        //cout<<endl;
    }
    return 0;
}

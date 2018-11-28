#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int oneCount(int num){
    int k=0;
    while(num){
        k=k+num%2;
        num/=2;
    }
    return k;
}
int main()
{
    int t,n,k,i,j,num,iter,l;
    double arr[20];
    double ans,tempans,temp1;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d%d",&n,&k);
        ans=0.0;
        for(j=0;j<n;j++){
            cin>>arr[j];
        }
        for(j=0;j<(1<<n);j++){
            num=j;
            if(oneCount(num)!=k)
                continue;
            iter=0;
            vector<int> item;
            while(num){
                if(num%2==1){
                    item.push_back(iter);
                }
                num=num/2;
                iter=iter+1;
            }
            tempans=0.0;
            for(l=0;l<(1<<k);l++){
                num=l;
                if(oneCount(num)!=k/2)
                    continue;
                temp1=1.0;
                for(iter=0;iter<k;iter++){
                    if(num%2==0){
                        temp1=temp1*(1-arr[item[iter]]);
                    }
                    else{
                        temp1=temp1*arr[item[iter]];
                    }
                    num=num/2;
                }
                tempans=tempans+temp1;
            }
            ans=max(ans,tempans);
        }
        printf("Case #%d: %0.6f\n",i,ans);
    }
    return 0;
}

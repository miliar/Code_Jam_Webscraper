#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

bool fun(float a,float b){
    if(a>b){
        return 1;
    }else return 0;
}

int main()
{
    int t;
    int n;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int z=0;z<t;z++){
        scanf("%d",&n);
        float arr[n];
        float brr[n];
        for(int i=0;i<n;i++){
            scanf("%f",&arr[i]);
        }
        for(int i=0;i<n;i++){
            scanf("%f",&brr[i]);
        }
        sort(arr,arr+n,fun);
        sort(brr,brr+n,fun);
        int count1,count2;
        count1=0;
        count2=0;
        int p,q,r,s;
        p=r=0;
        q=s=n-1;
        while(p<=q  && r<=s){
            if(arr[q]>brr[s]){
                count1++;
                q--;
                s--;
            }
            else{
                q--;
                r++;
            }
        }
        p=r=0;
        q=s=n-1;
        while(p<=q  && r<=s){
            if(arr[p]>brr[r]){
                count2++;
                p++;
                s--;
            }
            else{
                p++;
                r++;
            }
        }
      printf("Case #%d: %d %d\n",z+1,count1,count2);
    }
    return 0;
}

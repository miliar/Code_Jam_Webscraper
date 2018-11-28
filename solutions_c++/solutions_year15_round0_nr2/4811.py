#include <bits/stdc++.h>
using namespace std;
int arr[1001];
int min(int a,int b){
    if(a>b)return b;
    else return a;
}
void sort(int n){
    int a,i,j;
    for (i = 0; i < n; ++i)
    {
        for (j = i + 1; j < n; ++j)
        {
            if (arr[i] < arr[j])
            {
                a =  arr[i];
                arr[i] = arr[j];
                arr[j] = a;
            }
        }
    }
}

int main()
{
    int t,ans[9],len;
    cin>>t;
    for (int i = 0; i < t; i++) {
        cin>>len;
        for (int l = 0; l < len; l++) {
            cin>>arr[l];
        }
        int flag=1;
        sort(len);
        int max=arr[0];
        int ans=max,n=len;
        if(max>2)
        for(int k = 1 ; k <= max;++k){
            int tm = 0;
            for(int j=0;j<n;++j){
        		tm += (arr[j]-1)/k;
        	}
        	tm+=k;
        	ans=min(ans,tm);
        } 
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}
    
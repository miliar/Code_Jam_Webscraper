#include<iostream>
using namespace std;
#include<cstdio>
#include<cstdlib>
#include<algorithm>


int main(){
    int t,index=1;
    cin>>t;
    while(t--){
        int N,ans1=0,ans2=0,i=0,j=0;
        cin>>N;
        float arr[N];
        float brr[N];
        for(int i=0;i<N;i++)
            cin>>arr[i];
        for(int i=0;i<N;i++)
            cin>>brr[i];
        //qsort (arr, N, sizeof(float), compare);
        //qsort (brr, N, sizeof(float), compare);
        sort(arr,arr+N);
        sort(brr,brr+N);
        // for(int i=0;i<N;i++)
        //     cout<<brr[i];
        //   cout<<endl;
        // for(int i=0;i<N;i++)
        //     cout<<arr[i];
        while(i<N&&j<N){
            if(arr[i]<brr[j]){
                i++;
                j++;
                ans2++;
            }
            else{
                j++;
            }
        }
        i=0,j=0;
        while(i<N&&j<N){
            if(brr[i]<arr[j]){
                i++;
                j++;
                ans1++;
            }
            else{
                j++;
            }
        }
        printf("Case #%d: %d %d\n",index,ans1,N-ans2);
        index++;
    }

    return 0;

}

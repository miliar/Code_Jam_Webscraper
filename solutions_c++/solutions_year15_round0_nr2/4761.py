#include<iostream>
#include<algorithm>
#include<cstdio>

#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    CASET{
        int arr[1002];
        int n, max1, min1, time;
        cin>>n;
        for(int i=0;i<n; i++){
            cin>>arr[i];
            max1 = max(max1,arr[i]);
        }
        min1 = max1;
        for(int i=1;i<=max1;i++){
            time=i;
            for(int j=0;j<n;j++){
                if(arr[j]>i){
                    if( arr[j]%i == 0 ){
                        time+=(arr[j]/i-1);
                    }
                    else{
                        time+=(arr[j]/i);
                    }
                }
            }
            min1 =min(min1,time);
        }
        cout<<"Case #"<<case_n<<": "<< min1<<endl;
        case_n++;
    }
}

#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=0;p<t;p++){
        long long int n;
        cin >> n;
        int arr[10]={0};
        if(n==0){
            cout << "Case #" << p+1 << ": INSOMNIA"  << endl;
        }
        else{
            long long ans,temp;
            int count=0;
            long long int i=1;
            while(count!=10){
                ans=n*i;
                temp=ans;
                while(temp!=0){
                    if(arr[temp%10]==0){
                        arr[temp%10]=1;
                        count++;
                    }
                    temp=temp/10;
                }
                i++;
            }
            cout << "Case #" << p+1 << ": " << ans << endl;
        }
    }
	// your code goes here
	return 0;
}

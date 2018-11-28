#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <stack>
#define test int t; cin >> t;while(t--)
typedef unsigned long long ll;

using namespace std;

int MOD=1e9+7;

bool compare(int arr[]){
    for(int i=0;i<10;i++){
        if(arr[i]==0)return false;
    }
    return true;
}

void print(int arr[]){
    for(int i=0;i<10;i++)cout << arr[i] << " ";
    cout << endl;
}

void procedure(int n,int arr[]){
     while(n!=0){
            arr[n%10]=1;
            n=n/10;
        }
}
int main(){
	freopen("codejamrevengein.txt","r",stdin);
	freopen("codejamrevengeout.txt","w",stdout);
    int tt=1;
    test{

        int n;cin >> n;
        int temp=n;
        int arr[10]={0};
        cout << "Case #" << tt << ": ";
        int aa[n],cnt=0;
        tt++;
        if(n==0)printf("INSOMNIA\n");
        else{
        while(n!=0){
            aa[cnt]=n%10;
            arr[n%10]=1;
            n=n/10;
         //   cout << aa[cnt] << " ";
            cnt++;

        }

        int in=2;
        while(true){
          //  cout << "in" << in << "\n";
            int flag=1;
            for(int i=0;i<10;i++){
                if(arr[i]==0)flag=0;
            }
            if(flag)break;

            int carry=0;

            for(int i=0;i<cnt;i++){
                int k=aa[i]*in+carry;
                arr[k%10]=1;
                if(i==cnt-1){
                    procedure(k,arr);
                }

            //    cout << k%10 << "\n";
             //   print(arr);
                carry=k/10;
            }
            in++;
        }
        cout << (in-1)*temp << endl;
        }
    }
}

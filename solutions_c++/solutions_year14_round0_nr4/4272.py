#include<iostream>
#include <cstdio>
#include<algorithm>
using namespace std;
double a[1005];
double b[1005];
int main(){
    if (fopen("input.txt", "r")) freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int N;
    cin>>N;
    for (int i =1; i<=N; i++){
        int num;
        cin>>num;
        for (int j = 0; j<num; j++) cin>>a[j];
        for (int j = 0; j<num; j++) cin>>b[j];
        sort (a,a+num);
        sort (b,b+num);
        int ans1=0;
        int p2 = 0;
        for (int p1 =0; p1 < num; p1++){
            while (a[p1]>b[p2] && p2 < num) p2++;
            if (p2==num) break;
            if (p2<num){ ans1++; p2++;}
        }
        int ans2 = 0;
        int pi = 0;
        for (int p1 = 0; p1 < num; p1++){
            if (a[p1]>b[pi]){
                pi++;
                ans2++;
            }
        }
        cout<<"Case #"<<i<<": ";
        cout<<ans2<<" ";
        cout<<num-ans1<<endl;
    }
    return 0;
}

#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const int P = 1000000007;
int main(){
    int T,TT;
    cin>> T;
    TT=T;
    while (T--){
    	int row=0,x;
    	cin>>row;
    	int a[10];
    	for (int i=1;i<row;i++) for (int j=1;j<=4;j++)cin>>x;
    	for (int i=1;i<=4;i++) cin>>a[i];
    	for (int i=row+1;i<=4;i++) for (int j=1;j<=4;j++) cin>>x;
    	cin >>row;
    	int cnt=0,tx=0;
    	for (int i=1;i<row;i++) for (int j=1;j<=4;j++)cin>>x;
    	for (int i=1;i<=4;i++) {
    		cin>>x;
    		for (int j=1;j<=4;j++) if (x==a[j]) {a[j]=-a[j];
    			cnt++;tx=x;
    		}
    	}
    	for (int i=row+1;i<=4;i++) for (int j=1;j<=4;j++) cin>>x;
    	printf("Case #%d: ",TT-T);
        if (cnt==0) puts("Volunteer cheated!");
        if (cnt==1)  printf("%d\n",tx);
        if (cnt>1) puts("Bad magician!");
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	int t;
	//scanf("%d",&t);
	//int X=0;
	ifstream f1;
    ofstream f2;
    f1.open("B-large.in");
    f2.open("output.out");
	f1>>t;
	//ll n,j
	int X=1;
	while(t--)
    {
        int n,x;
        f1>>n;
        //int a[n][n];
        int b[2500+2]={0};
        int a[n];
        for(int i=0;i<n*(2*n-1);i++) {f1>>x;b[x]+=1;}
        int j=0,i=1;
        //for(int j=0;j<10;j++) cout<<b[j]<<" ";cout<<endl;
        while(j<n) {
        	if(b[i]%2  == 1) {a[j]=i;j++;}
        	i++;

        }
        sort(b,b+n);
        f2<<"Case #"<<X<<": ";
        for(int i=0;i<n;i++) f2<<a[i]<<" ";f2<<endl;
    X++;
    }
    //X++;
	f1.close();
    f2.close();
	return 0;
}

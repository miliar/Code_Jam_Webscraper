#include<iostream>
#include<algorithm>
#include<cstdio>

//#define CASET

using namespace std;
int main(){
    long long int t,x,i,n,j,a;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long int ___T,case_n;
    case_n = 1;
    scanf("%lld ", &___T);
    while (___T-- > 0){

        cout<<"Case #"<<case_n++<<": ";
        int ar[3001];
		for(i=0;i<=3000;i++)
		{
			ar[i]=0;
		}
		cin>>n;
		for(i=0;i<(2*n-1);i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>a;
				ar[a]++;
			}
		}
		//cout<<"Case #"<<x<<": ";
		for(i=0;i<=3000;i++)
		{
			if(ar[i]%2==1)
			{
				cout<<i<<" ";
			}
		}
		cout<<endl;
    }
}

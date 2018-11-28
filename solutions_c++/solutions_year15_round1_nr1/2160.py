#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#define ll long long int
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\Admin\\Downloads\\4.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
	int t,x=1;
	cin>>t;
	while(t--){
		int n,i,val1=0,ans1=0,ans2=0;
		cin>>n;
		int a[n];
		for(i=0;i<n;i++){
			cin>>a[i];
		}
		for(i=1;i<n;i++){
			if(a[i]-a[i-1]<0)
				ans1+=(a[i-1]-a[i]);
			val1=max(val1,a[i-1]-a[i]);
		}
		for(i=0;i<n-1;i++){
			if(a[i]>=val1)
			ans2+=val1;
			else
			ans2+=a[i];
		}
		cout<<"Case #"<<x++<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
} 
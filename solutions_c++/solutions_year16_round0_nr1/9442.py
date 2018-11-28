#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	long long N , ans;
	for(int i = 1 ; i <= t ; i ++){
		int freq[10]={0};
		cin>>N;
		long long n=N;
		int x=1;
		cout<<"Case #"<<i<<": ";
		if(N==0)
			cout<<"INSOMNIA\n";
	
		else{
			
			while(freq[0]==0||freq[1]==0||freq[2]==0||freq[3]==0||freq[4]==0||freq[5]==0||freq[6]==0||freq[7]==0||freq[8]==0||freq[9]==0){
			N=n*x;
			ans=N;
			int re;
			while(N>0){
				re=N%10;
				N/=10;
				++freq[re];
			}
			x++;
		
			}
		cout<<ans<<"\n";
		}
	}
}
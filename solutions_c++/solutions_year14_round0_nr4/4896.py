#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
double Naomi[1005];
double Ken[1005];

int main(){
	int T,n;
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	cin>>T;
	for(int t = 1; t <= T; t++){
		cin>>n;
		
		for(int i = 0; i < n;i ++)
			cin>>Naomi[i];
		for(int i = 0; i < n;i ++)
			cin>>Ken[i];
			
		sort(Naomi,Naomi + n);
		sort(Ken,Ken + n);
		
		int j = 0,count = 0,count1 = 0;
		for(int i = 0; i < n&& j < n; i ++){
		    while(j < n && Naomi[j] < Ken[i])
				j ++;
			if(j < n){ j ++; count++;}
		}
		j = 0;
		for(int i = 0; i < n && j < n; i ++){
			while(j < n && Ken[j] < Naomi[i])
				j ++;
			if(j < n){ j ++; count1++;}
		}
		cout<<"Case #"<<t<<": "<<count<<" "<<n - count1<<endl;
	}
}

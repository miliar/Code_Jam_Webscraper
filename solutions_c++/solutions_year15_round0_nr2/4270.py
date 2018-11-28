#include <bits/stdc++.h>
 
using namespace std;
 
int main(){
	int t,t_max;
	scanf("%d",&t);
	t_max = t;
	while(t--){	
		int d;
		scanf("%d",&d);
		int* a=new int[1001];
		for(int i=0;i<1001;i++){
			a[i]=0;
		}
		for(int i=0;i<d;i++){
			int p;
			scanf("%d",&p);
			a[p]++;
		}
		int opt=1000;
		for(int i=1;i<=1000;i++)
		{	int count=0;
			for(int j=i+1;j<=1000;j++)
			{	if(j%i==0)count+=a[j]*((j/i)-1);
				else count+=a[j]*(j/i);
			}
			opt=min(opt,count+i);
		}
		cout<<"Case #"<<t_max - t<<": "<<opt<<endl;
	}
}
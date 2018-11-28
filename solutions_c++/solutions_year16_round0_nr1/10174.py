#include<bits/stdc++.h>

using namespace std;

#define PI 3.14159265
 int a[10]={0,0,0,0,0,0,0,0,0,0};
	long long int t,k,l,m,n,flag=0;
	int j;
int search(int n){
	long long int k,j,l;
	k=n;
	while(k>0){
		l=k%10;
		for(j=0;j<10;j++){
			if(l==j)
				a[j]=1;
		}
		k=k/10;
	}
	
	
}

int check(){
	int i,j=1;
	for(i=0;i<10;i++){
	if(a[i]==0)
		{
		j=0;
		return 0;
		}
	}
	return 1;
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("ou.txt","w",stdout);
   
    cin>>t;

	for(j=0;j<t;j++)
	{		
		cin>>n;
		flag=0;
		for(m=0;m<10;m++){
			a[m]=0;
		}
		if(n==0)		
		cout<<"Case #"<<j+1<<": INSOMNIA"<<endl;
		else
		{
			m=1;
			while(flag!=1)
			{
				k=m*n;
				search(k);
				flag=check();
				m++;
			}	
		cout<<"Case #"<<j+1<<": "<<k<<endl;
			
		}
	}

return 0;
}

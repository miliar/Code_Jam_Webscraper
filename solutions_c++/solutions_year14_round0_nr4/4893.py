#include <iostream>
#include <algorithm>
using namespace std;

bool sort_des(const double &l, const double &r){
	return l>r;
}

int war(double na[],double ke[],int n){

	int i,k=0,flag=0,f[n],j,count=0;
	for(i=0;i<n;i++)
		f[i]=1;
	sort(na,na+n,sort_des);
	sort(ke,ke+n);
	for(i=0;i<n;i++){
		flag=0;
		for(j=0;j<n;j++){
			if(ke[j]>na[i]&&f[j]==1){
				f[j]=0;
				flag=1;
				count++;
				break;
			}
			
		}
		if(flag==0){
				f[k]=0;
				k++;
			}

			
	}
	
return (n-count);
}

int d_war(double na[],double ke[],int n){
	int i=0,j=0,count=0;
	sort(na,na+n);
	sort(ke,ke+n);
	while(i<n){
		if(na[i]>ke[j])
		{
			count++;
			i++;j++;
		}
		else
			i++;
		}
	return count;
}

int main()
{
	int t,n,i,nt=0;
	cin>>t;
	while(t--){
		nt++;
		cin>>n;
		double na[n],ke[n];
		for(i=0;i<n;i++)
			cin>>na[i];
		for(i=0;i<n;i++)
			cin>>ke[i];
		cout<<"Case #"<<nt<<": "<<d_war(na,ke,n)<<" "<<war(na,ke,n)<<endl;
	}
	return 0;
}

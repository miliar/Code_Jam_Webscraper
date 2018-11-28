//#define LOCAL
#include<iostream>
using namespace std; 
void bubblesort(int n,float a[]){
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
			if(a[i]>a[j])swap(a[i],a[j]);
}
int main()
{
	#ifdef LOCAL
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,j,k,l,win1,win2;
		cin>>n;
		float nao[n],ken[n];
		for(j=0;j<n;j++)cin>>nao[j];
		for(j=0;j<n;j++)cin>>ken[j];
		bubblesort(n,nao);
		bubblesort(n,ken);
		j=k=l=0;//k is the abandoned nao woods for ken's biggest woods.
		while(nao[j]<ken[n-1-k]&&j<n)
		{
			if(nao[j]>ken[l])l++;
			else k++;
			j++;
		}
		win1=n-k;
		j=k=l=0;
		while(l<n)
		{
			if(nao[j]<ken[l])j++;
			else k++;
			l++;
		}
		win2=k;
		cout<<"Case #"<<i+1<<": "<<win1<<" "<<win2<<endl;
	}
	return 0;
}

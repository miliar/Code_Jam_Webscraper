#include<iostream>
#include<algorithm>
#define MAXN 1000001
using namespace std;
int t,a,n,x,ile,res;
int iletrzeba[MAXN];
int tab[MAXN];
int main(){
	ios_base::sync_with_stdio(0);
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>a>>n;
		for(int j=0;j<n;j++){
			cin>>tab[j];
			}
		if(a==1){
			cout<<"Case #"<<(i+1)<<": "<<n<<"\n";
			continue;	
		}
		sort(tab,tab+n);
		for(int j=0;j<n;j++){
			ile=0;
			while(a<=tab[j]){
				a+=(a-1);
				ile++;
			}
			a+=tab[j];
			if(j==0)iletrzeba[j]=ile;
			else iletrzeba[j]=iletrzeba[j-1]+ile;	
		}
		res=n;  //res to usuniecie reszty
		for(int j=0;j<n;j++){
			x=(iletrzeba[j]+(n-j-1));
			if(x<res)res=x;
		}
		cout<<"Case #"<<(i+1)<<": "<<res<<"\n";
	}
cout<<endl;
return 0;
}

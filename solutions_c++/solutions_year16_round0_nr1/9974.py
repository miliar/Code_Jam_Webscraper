#include<iostream>
#include<set>
using namespace std;
int main(){
	
	freopen("A-large.in","r",stdin);
	
	freopen("output.txt","w", stdout);
	
	long int n;
	
	cin>>n;
	
	long int ress=1;
	
	while(n--){
		
		set<int>v;
		
		long int k;
		
		cin>>k;
		
		if(k==0){
			
			cout<<"Case #"<<ress<<": "<<"INSOMNIA"<<endl;
			++ress;
			continue;
		}
		
		
		long int i=1;
		
		long int kk=0;
		
		while(true){
			
			if(v.size()==10)
			{
				cout<<"Case #"<<ress<<": "<<kk<<endl;
				++ress;
				break;
			}
		
			
			kk=k*i;
			
			long no=kk;
			
			
			long res=0;
	
			while(no!=0){
		
				res=no%10;
		
				v.insert(res);
		
				no=no/10; 
			}
			
			++i;	
		}
	}
	return 0;
}

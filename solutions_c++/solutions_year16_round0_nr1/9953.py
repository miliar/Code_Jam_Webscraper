#include <iostream>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int br[10];
	int t;
	cin>>t;
	int a[t];
	int p,d,f;
	for(int i=0;i<t;i++)
	{
		cin>>a[i];
	}	
	for(int i=0;i<t;i++){
		if(a[i]==0)
		cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		else{
			f=1;
			for(int k=0;k<10;k++)
			br[k]=0;
			for(int j=1;f==1;j++){
				p=j*a[i];
				while(p!=0){
					d=p%10;
					br[d]+=1;
					p=p/10;
				}
				d=0;
				for(int t=0;t<10;t++){
					if(br[t]<1)
					{
						d=1;
						t=10;
					}
				}
				if(d==0)
				{
					f=0;
					cout<<"Case #"<<i+1<<": "<<j*a[i]<<endl;
				}
			}	
		}
	}	
}

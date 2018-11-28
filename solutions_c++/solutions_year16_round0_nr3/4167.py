#include<fstream>
using namespace std;
ifstream cin("c.in");
ofstream cout("c.out");
long long n,t,j,a[50],y,num[20],divi[20];
void tran(long long x){
	for(int i=0;i<=32;i++){
		a[i]=0;
	}
	y=1;
	while(x){
		if(x%2)a[y]=1;
		else a[y]=0;
		x=x/2;
		y++;
	}
}
long long prim(long long x){
		//int k=0;
	////	bool u=false;
		for(int i=2;i<=x/2&&i<=1000000;i++){if(x%i==0)return i;}
	//	k=0;
	//	if(u)for(int i=1;i<=x;i++){if(x%i==0)k++;if(k==2){return i;i=x+2;}}
	 return 0;
}
int main(){
	cin>>t;
	for(long long r=1;r<=t;r++){
		cin>>n>>j;
		long long p=1;
		for(long long i=1;i<n;i++)p=p*2;
		cout<<"Case #"<<r<<":\n";
		while(j>0){
				
		for(long long i=p;i<p*2;i++){
			   if(j>0){ if(i%2==1){
			    		int l=1;
			    		for(int o=1;o<=9;o++)num[o]=0;
			    		tran(i);
			    		num[l]=i;l++;
			    		long long m=0;
			    		for(int q=3;q<=10;q++){
			    			m=0;
			    			y=1;
			    			for(int o=1;o<=n;o++){
			    						m=a[o]*y+m;
			    						y=y*q;
									}
							num[l]=m;
							l++;
						}	
							for(int o=1;o<=9;o++)divi[o]=prim(num[o]);	  
							bool e=true;
							for(int o=1;o<=9;o++)if(!divi[o])e=false;
							if(e){
								cout<<num[9]<<" ";
								for(int o=1;o<=9;o++)cout<<divi[o]<<" ";j--;
								cout<<'\n';
							
							} 		
			   		}
			   	
				}
			}
		}
			
	}
}

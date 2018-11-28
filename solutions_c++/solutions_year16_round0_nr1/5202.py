
#include<bits/stdc++.h>
using namespace std;
int prime[1000000]={0};

void makedivisor(){
	prime[2]=0;
	prime[3]=0;
	for(int i=2;i<=1000000;i++){
		if(prime[i]==0)
		for(int j=i*2;j<=1000000;j+=i){
			prime[j]=i;

		}

	}


}
void cal(int n){
}


int main()
{
	int t;
	//makedivisor();
	/**for(int i=0;i<100;i++)
		cout<<i<<" "<<prime[i]<<" \n";
	*/
	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout)  ;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		long long int n,k;
		cin>>n;
		cout<<"Case #"<<tt<<": ";
		long long int temp;
		int arr[10]={0};
		int count=1;
		bool flag=false;
		clock_t c0, c1;
		time_t t0, t1;
		t0 = time(NULL);
		c0 = clock();
		t1 = time(NULL);
		int no=0;
		long long int ans;

		if(n==0){
			cout<<"INSOMNIA"<<endl;;

		}
		else {
			while(flag==false){
				temp=n*count;
				while(temp!=0){
					arr[temp%10]=1;
					temp=temp/10;
					// cout<<temp;
				}
				for(int i=0;i<10;i++)
				{  if(arr[i]==1)
					no++;
				}
				if(no==10)
				{flag=true;
					ans=n*count;
				}
				else
				{
					count++;
					no=0;
				}
				c1 = clock();
				if((float) (c1 - c0) / CLOCKS_PER_SEC >5)  {
					cout<<"INSOMNIA\n";
					goto here;
				}
			}
			cout<<ans<<endl;
here: ;

		}



	}
}





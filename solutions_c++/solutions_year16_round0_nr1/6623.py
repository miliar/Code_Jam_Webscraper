#define LOCAL
#include<iostream>
using namespace std; 
int main()
{
	#ifdef LOCAL
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		else{
			bool flag[10];
			for(int i=0;i<10;i++){
				flag[i]=false;
			}
			int counter=1;
			int num;
			while(true){
				//extract digits
				num=n*counter;
				int digit;
				int tmp=num;
				while(tmp!=0){
					digit=tmp%10;
					flag[digit]=true;
					tmp=tmp/10;
				}
				bool judge=true;
				for(int i=0;i<10;i++){
					if(flag[i]==false){
						judge=false;
					}
				}
				if(judge){
					cout<<"Case #"<<i+1<<": "<<num<<endl;	
					break;
				}
				counter++;
			}
		}
	}
	return 0;
}

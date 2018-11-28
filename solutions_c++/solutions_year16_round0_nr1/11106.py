#include<iostream>
using namespace std;
int main(){
	long long int T;
	cin>>T;
	long long int j=T;
	for(int T=1;T<j+1;T++){
		long long int N,Copy,Save,i,flag=0;               
		int arr[10]={10,10,10,10,10,10,10,10,10,10};
		cin>>N;
		Copy=N;
		if(N!=0)
		{
			long long int i=1,j=-1;
 loop:	    while(N!=0)
			{
				int i=N%10;
				N=N/10;
				j=-1;
				while(i!=arr[j+1]){
					j++;                      
					if(arr[j]==10)
					{
						arr[j]=i;
						break;
					}
				}
				if(j==9){
					cout<<"Case #"<<T<<": "<<Save<<endl;
					flag=1;
					break;
		        }
			}
			if(flag==1)
			{   
			    flag=0;
			 //   T++;
				continue;
		        
			}
			N=(i++)*Copy;
			Save=N;
			goto loop;
		}
		else
			cout<<"Case #"<<T<<": INSOMNIA"<<endl;
	}
	return 0;
}

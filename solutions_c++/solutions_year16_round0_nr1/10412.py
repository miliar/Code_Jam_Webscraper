#include <iostream>
using namespace std;
int main()

{
	int T; long long  N;
	cin >>T;
	int flag;
	int t; long long num;
	int n=1;
	int count=0;
	while(T--)
	{
	int number[10]={0};
		cin>>N;
		
		for(int j=1;j<100;j++)
		{	if (N==0) {cout<<"Case #"<<n<<":"<<" "<<"INSOMNIA"<<endl; break;} 
			int flag=1;count=0;
			num=j*N;
			while(num)
			{	
				t=num%10;
				//cout<<"Number"<<t<<endl;
				number[t]=1;
				num=num/10;
			}
				for(int y=0;y<10;y++)
				{ if (number[y]==0) {count++;}}//  cout<<"Count"<<count<<endl;}}
		if(count==0){ cout<<"Case #"<<n<<":"<<" "<<j*N<<endl; break;}
		}
	n++;
	}

}

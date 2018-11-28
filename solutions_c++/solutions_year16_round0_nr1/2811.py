#include <iostream>

using namespace std;

int main()
{
	int T, result[100];
	cin>>T;
	for(int i=0;i<T;i++) {
		int N, num[10]={}, check=0, j;
		cin>>N;
		for(j=1;j<=100 && check!=55;j++) {
			int temp=N*j;
			for(;temp;temp/=10) {
				if(num[temp%10]++==0)
					check+=temp%10+1;
			}
		}
		if(check==55)
			result[i]=N*(j-1);
		else
			result[i]=0;
	}
	for(int i=0;i<T;i++) {
		cout<<"Case #"<<i+1<<": ";
		if(result[i])
			cout<<result[i]<<endl;
		else
			cout<<"INSOMNIA"<<endl;
	}
    return 0;
}
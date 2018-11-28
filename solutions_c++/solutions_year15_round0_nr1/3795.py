#include <iostream>
#include<string>
using namespace std;
int main(){	
	int TT;
	cin>>TT;
	int Smax;
	int c=1;
	while(TT--){
		cin>>Smax;
		int guests=0;
		int counts[Smax+1];
	        string s;	
		for(int i=0;i<=Smax;i++)
			counts[i]=0;
		cin>>s;
		for(int i=0;i<=Smax;i++){
			counts[i]=s[i]-'0';
		
		}
		for(int i=0;i<Smax;i++)
		{
			int sum=0;
			for(int j=0;j<i+1;j++){
				sum+=counts[j];	
			}
			if(sum < i+1 && counts[i+1]!=0)
			{
				guests+=(i+1)-sum;
				counts[0]+=(i+1)-sum;
			}
		}
		cout<<"Case #"<<c++<<": "<<guests<<endl;
	}
}

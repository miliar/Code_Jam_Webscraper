#include <iostream>
using namespace std;

int main() {
	int test,q=1;
	cin>>test;
	while(test--)
		{	
			int max_shy,count[7]={0},sum=0,people=0,x=0;
			char shy_count[8]; 
			cin>>max_shy;
			cin>>shy_count;
			for(int i=0;i<=max_shy;i++)
				{
				count[i]=shy_count[i]-48;	
				//cout<<count[i]<<endl;
				}
			sum=count[0];
			for(int i=1;i<=max_shy;i++)
			 {
			 	if(sum<i)
			 	 people=i-sum;
			 	
			 	sum=sum+count[i]+people;
			 	//cout<<sum;
			 	
			 	x=x+people;
			 	//cout<<x<<endl;
			 	people=0;
			 }
		cout<<"Case #"<<q<<": "<<x<<endl;	 
		q++;
		}
	return 0;
}
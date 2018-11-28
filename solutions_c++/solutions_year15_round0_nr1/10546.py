#include<iostream>
#include<fstream>
using namespace std;

class opera
{
	private:
		int test;
		int max;
		int val;
		int arr[7];
		int mod;
		int ans;
		int count;

    public:
	void input()
	{
	 test=0;
	 max=0;
	 val=0;
	 mod=0;
	 ans=0;
	 count=0;
	 
	 ifstream myfile1;
	 ofstream myfile2("output.txt");
	 myfile1.open("input.txt");
	 myfile1>>test;	
	 
	 for(int i=0;i<test;i++)
	 {
	 myfile1>>max;	
	 if((test>100)||(test<1)||(max>6)||(max<0))
	 {
	 	cout<<"limits not satisfied:"<<endl;
	 	break;
	 }
	// cout<<max;
	 myfile1>>val;
	 count=max;
	 
	 for(int j=0;j<=max;j++)
	 {
		 mod=val%10;
		 val=val/10;
		 arr[count]=mod;
		 count--;	
	 }
	 int sum;
	 ans=0;
	 for(int k=1;k<=max;k++)
	 {
	 	sum=0;
	 	for(int l=0;l<k;l++ )
	 	{
	 	sum=sum+arr[l];	
		}
		sum=sum+ans;
		if(sum<k)
		{
			ans=ans+(k-sum);
		}
	 }
	 myfile2<<"case #"<<i+1<<": "<<ans<<endl;
	 }
	}
		
};


int main()
{
 opera obj;
 obj.input();
	
	
	return 0;
}

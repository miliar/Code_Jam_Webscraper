#include<iostream>




using namespace std;



int main()
{
	int n;
	cin>>n;
	int a,b;
	int r=0;
	int fns[]={1,4,9,121,484};
	for(int i=0;i<n;i++)
	{
		cin>>a;
		cin>>b;
		int p=0;
		int q=4;
		while(fns[p]<a && p<5)
			p++;
		while(fns[q]>b && q>=0)
			q--;
		cout<<"Case #"<<i+1<<": "<<q-p+1<<endl;








	}







}

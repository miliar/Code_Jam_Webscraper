#include <iostream>
using namespace std;



int cal(int in1,int a[4][4],int in2,int b[4][4])
{
	int c[4];
	int count=0;
	int k=0;
	int d[4];
	//store all the values of the row in1 in c[]
	for(int i=0;i<4;i++)
	{
		c[i] = a[in1-1][i];
	}
	//store all the values of row in2 in d[]
	for(int i=0;i<4;i++)
	{
		d[i] = b[in2-1][i];
	}
	//now compare the number of elements equal in c and d
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(c[i] == d[j])
				{count++; k = i;}
		}
	}
    
	if(count == 1) return c[k];
	else if(count > 1 ) return 17;
	else if(count == 0)	 return 18;

}

int main()
{
	int n;
	int a[4][4];
	int b[4][4];
	int in1,in2;
	int r[100];
	cin>>n;//number of test cases

	for(int i=0;i<n;i++)
	{
		cin>>in1;// row of the 1st question

		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		cin>>a[j][k];//to input the 1st arragment

		cin>>in2;// row of the 2nd question

		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		cin>>b[j][k];//to input the 2nd arragment

		r[i]= cal(in1,a,in2,b);// calculate the answer.

	}

	for(int i=0;i<n;i++)
	{
		if(r[i]>=0&&r[i]<=16)
			cout<<"Case #"<<i+1<<": "<<r[i];
		else if(r[i] == 17)
			cout<<"Case #"<<i+1<<": "<<"Bad magician!";
		else if(r[i] == 18)
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!";
		cout<<"\n";
	}
    return 0;
}

#include<iostream>
using namespace std;


int main()
{
	int t,testcases,A[5][5],B[5][5],ans1,ans2;
	int buff[20];

	cin>>testcases;
	for(t=1;t<=testcases;t++)
	{
		for(int i=0;i<20;i++)
		{
			buff[i]=0;
		}
		cin>>ans1;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				cin>>A[i][j];
			}
		}
		cin>>ans2;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				cin>>B[i][j];
			}
		}
		for(int j=1;j<5;j++)
		{
			buff[A[ans1][j]]++;
			buff[B[ans2][j]]++;
		}/*
		for(int i=1;i<20;i++)
		{
			cout<<buff[i]<<" ";
		}*/
		int count=0;
		int current=0;
		for(int i=1;i<=16;i++)
		{
            if(buff[i]==2)
            {
                current=i;
                count++;
            }
		}
		cout<<"Case #"<<t<<": ";
		if(count==1)
		{
            cout<<current<<endl;
		}
		else if(count==0)
		{
		    cout<<"Volunteer cheated!"<<endl;
		}
		else
		{
            cout<<"Bad magician!"<<endl;
		}
	}

	return 0;
}

#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{//cout<<i<<endl;
		int n;
		cin>>n;
		cout<<"Case #"<<(i+1)<<": ";
		int a[30];
		int b[30];
		int count=0;
		for(int j=0;j<n;j++)
		{
			cin>>a[j];
			b[j]=j;
			count+=a[j];
		}
		int size=n;
		for(int j=0;j<size;j++)
		{
			for(int k=j+1;k<size;k++)
			{
				if(a[j]>a[k])
				{
					int temp=a[j];
					a[j]=a[k];
					a[k]=temp;
					temp=b[j];
					b[j]=b[k];
					b[k]=temp;
				}
			}
		}//cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
		while(count>0)
		{				//cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
			if(size==3 && a[size-1]==1)
			{//cout<<"a";
				cout<<char(b[size-1]+65)<<" "<<char(b[size-2]+65)<<char(b[size-3]+65)<<endl;
				count = 0;
				size = 0;
				break;
			}
			else if(size==2 && a[size-1]==1)
			{//cout<<"b";
				cout<<char(b[size-1]+65)<<char(b[size-2]+65)<<endl;
				count=0;
				size=0;
				break;
			}
			if (a[size-1]>a[size-2])
			{//cout<<"c";
				cout<<char(b[size-1]+65)<<char(b[size-1]+65)<<" ";
				a[size-1]-=2;
				count-=2;//cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
				if(a[size-1]==0)
				{
					size--;
				}
				else
				{//cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
					int l=a[size-1];int k=b[size-1];//cout<<l;
					int index=size-2;
					while(l<a[index] && index>=0)
					{
						a[index+1]=a[index];
						b[index+1]=b[index];
						index--;//cout<<endl<<a[0]<<a[1]<<a[2]<<"fe"<<endl;
					}//cout<<index;
					a[index+1]=l;
					b[index+1]=k;//cout<<endl<<a[0]<<a[1]<<a[2]<<"fd"<<endl;
				}//cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
			}
			else
			{
				cout<<char(b[size-1]+65)<<char(b[size-2]+65)<<" ";
				a[size-1]-=1;
				a[size-2]-=1;
				count-=2;
				//cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
				if(a[size-1]==0)
				{
					size-=2;
				}
				else if(size>2)
				{
					int gh=size-1;
					int l=a[gh-1];int k=b[gh-1];
					int index=gh-2;
					while(l<a[index] && index>=0)
					{
						a[index+1]=a[index];
						b[index+1]=b[index];
						index--;
					}
					b[index+1]=k;
					a[index+1]=l;
								//	cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
					l=a[size-1];
					index=size-2;
					k=b[size-1];
					while(l<a[index] && index>=0)
					{
						a[index+1]=a[index];
						b[index+1]=b[index];
						index--;
					}
					b[index+1]=k;
					a[index+1]=l;
							//		cout<<endl<<a[0]<<a[1]<<a[2]<<endl;
				}
			}
		}
	}
	return 0;
}
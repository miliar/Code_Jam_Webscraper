#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

void insertion_sort (int arr[],char P[], int length){
	 	int j, temp;
	 	char ctemp;
		
	for (int i = 0; i < length; i++){
		j = i;
		
		while (j > 0 && arr[j] < arr[j-1]){
			  temp = arr[j];
			  arr[j] = arr[j-1];
			  arr[j-1] = temp;
			  ctemp=P[j];
			  P[j]=P[j-1];
			  P[j-1]=ctemp;
			  j--;
			  
			  }
		}
}

int main()
{
	fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\JAMAout.txt");
	int T, s=1;
	cin>>T;
	while(T)
	{
		int N;
		cin>>N;
		int P[N];
		char arr[N+1];
		long int sum=0;
		for(int i=0;i<N;i++)
		{
			cin>>P[i];
			arr[i]=char((int)'A'+i);
			sum+=P[i];
		}
		insertion_sort(P,arr,N);
			cout<<"Case #"<<s<<": ";
			fil<<"Case #"<<s<<": ";	
		while(P[N-1]!=1)
		{
			int tsum;
			if(P[N-2]< (sum-2)/2 )
			{
				sum=sum-2;
				P[N-1]=P[N-1]-2;
				//cout arr[N-1] stmt
				cout<<arr[N-1]<<arr[N-1]<<" ";
				fil<<arr[N-1]<<arr[N-1]<<" ";
				insertion_sort(P,arr,N);
			}
			else if (P[N-2]>= (sum-2)/2)
			{
				P[N-2]--;
				P[N-1]--;
				cout<<arr[N-1]<<arr[N-2]<<" ";
				fil<<arr[N-1]<<arr[N-2]<<" ";
				//cout stmt
				sum-=2;
				insertion_sort(P,arr,N);
			}
		}
		int count=0;
		for(int i=0;i<N;i++)
		{
			if(P[i]==1)
			count++;
		}
		int i=N-1;
		if(count%2==0)
		{
			while(i>=1)
			{
				cout<<arr[i]<<arr[i-1]<<" ";
				fil<<arr[i]<<arr[i-1]<<" ";
				i-=2;
			}
		}
		else
		{
			cout<<arr[i]<<" ";
			fil<<arr[i]<<" ";
			i--;
			while(i>=1)
			{
				cout<<arr[i]<<arr[i-1]<<" ";
				fil<<arr[i]<<arr[i-1]<<" ";
				i-=2;
			}
		}
	fil<<"\n";
	cout<<endl;
		s++;
		T--;
	}
	fil.close();
}
	

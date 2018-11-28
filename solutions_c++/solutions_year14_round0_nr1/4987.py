#include<iostream>
#include<string>
#include<cstring>
#include<vector>
using namespace std;

void print(int A[], int size)
{
	for(int i=0 ; i<size ; ++i)
		cout<<A[i]<<" ";
	cout<<endl;	
}

int magician(int A[], int B[], int size);
void sort(int A[], int size);

int main()
{
	int cases,t,row,ans,rem;
	int A[5],B[5];
	int dump,i,j;
	vector<int> answer;
		
	cin>>cases;
	cin.ignore(10,'\n');
	t=1;
	while(t<=cases)
	{
		cin>>row;
		rem = 4-row;
		while(row>1)
		{
			for(i=0 ; i<4 ; ++i)
				cin>>dump;
			row--;
		}
		for(i=0 ; i<4 ; ++i)
			cin>>A[i];
		while(rem>0)
		{
			for(i=0 ; i<4 ; ++i)
			cin>>dump;
			rem--;
		}
		//----------------
		cin>>row;
		rem = 4-row;
		while(row>1)
		{
			for(i=0 ; i<4 ; ++i)
				cin>>dump;
			row--;
		}
		for(i=0 ; i<4 ; ++i)
			cin>>B[i];
		while(rem>0)
		{
			for(i=0 ; i<4 ; ++i)
			cin>>dump;
			rem--;
		}
		//---------------
		//print(A,4);
		//print(B,4);
		t++;
		
		ans = magician(A,B,4);
		answer.push_back(ans);
	}		//end of while loop
	
	for(i=0 ; i<answer.size() ; ++i)
	{
		ans = answer[i];
		if(ans<=16)
		{
			cout<<"Case #"<<i+1<<": "<<ans<<"\n"; 
		}
		else if(ans==17)
		{
			cout<<"Case #"<<i+1<<": Bad magician!"<<"\n";
		}
		else
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
	}
	return 0;
}

void sort(int A[], int size)
{
	int temp;
	for(int i=0 ; i<size-1 ; ++i)
		for(int j=0 ; j<size-1-i ; ++j)
		{
			if(A[j]>A[j+1])
			{
				int temp = A[j];
				A[j] = A[j+1];
				A[j+1] = temp;
			}
		}	
}

/*int main()
{
	int A[4] = {9,8,4,0};
	int B[4] = {1,5,7,13};
	sort(A,4);
	sort(B,4);
	cout<<magician(A,B,4)<<"\n";
	return 0;
}*/

int magician(int A[], int B[], int size)
{
	sort(A,size);
	sort(B,size);
	//print(A,4);
	//print(B,4);
	int ans=18,i=0,j=0,count=0;
	while(i<size && j<size)
	{
		if(A[i]==B[j])
		{
			if(count<1)
			{
				count++;
				ans = A[i];
				i++;
				j++;
			}
			else
			{
				ans = 17;
				break;
			}
		}
		else if(A[i]<B[j])
			i++;
		else j++;
	}
	return ans;	
}
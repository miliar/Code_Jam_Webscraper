#include<iostream>
using namespace std;

int main()
{
  
  int testcases;
  cin>>testcases;
  for(int t = 0; t<testcases;t++)
  {
    string output="YES";
    int n,m;
    cin>>n>>m;
    int arr[n+1][m+1];
    arr[n][m] = -1;
    int rowMax = -1;
    int colMax = -1;
    for(int i =0;i<n;i++)
    {
	 rowMax = -1;
	 for(int j=0;j<m;j++)
	 {
	   cin>>arr[i][j];
	   if(arr[i][j]>rowMax)
		rowMax = arr[i][j];
	 }
	 arr[i][m] = rowMax;
    }
    
    for(int i =0;i<m;i++)
    {
	 colMax = -1;
	 for(int j=0;j<n;j++)
	 {
	   if(arr[j][i]>colMax)
		colMax = arr[j][i];
	 }
	 arr[n][i] = colMax;
    }
    
    /*cout<<"Printing the Final Array \n";
    
    for(int i =0;i<n+1;i++)
    {
	 for(int j=0;j<m+1;j++)
	 {
	   cout<<arr[i][j];
	 }
	 cout<<"\n";
    }
    cout<<"\n";*/
    
    
    for(int i =0;i<n;i++)
    {
	 for(int j=0;j<m;j++)
	 {
	   if(arr[i][j]!=arr[n][j]&&arr[i][j]!=arr[i][m])
	   {
		output = "NO";
		//cout<<"Index"<<i<<"->"<<j<<"\n";
		break;
	   }
	 }
    }
    
    cout<<"Case #"<<t+1<<": "<<output<<"\n";
  }
}
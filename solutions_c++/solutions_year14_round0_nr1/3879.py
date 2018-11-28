#include<iostream>
using namespace std;
#include<vector>
#include<algorithm>

int main()
{
  int t;
  cin>>t;
  int mat[4][4];
  for(int i=0;i<t;i++)
  {
    int arr1[4],arr2[4];
    for(int trials=0;trials<2;trials++)
    {
	 int row;
	 cin>>row;
	 for(int j=0;j<4;j++)
	 {
	   for(int k=0;k<4;k++)
	   {
		cin>>mat[j][k];
	   }
	 }
	 for(int p=0;p<4;p++)
	 {
	   if(trials==0)
	   arr1[p] = mat[row-1][p];
	   else
		arr2[p] = mat[row-1][p];
	 }
    }
    	     	 /*for(int test=0;test<4;test++)
	   cout<<arr1[test]<<" "<<arr2[test]<<"\n";*/
	 sort(arr1,arr1+3);
	 sort(arr2,arr2+3);
	 
	 int number = -1;	 
	 int intcounter = 0;
	 for(int p=0;p<4;p++)
	 {
	   for(int q=0;q<4;q++)
	   {
		if(arr1[p] == arr2[q])
		{
		    intcounter++;
		    number = arr1[p];
		}
	   }
	 }
	 
	 if(intcounter ==0)
	 cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<"\n";
	 else if(intcounter ==1)
	       cout<<"Case #"<<i+1<<": "<<number<<"\n";
	 else if(intcounter>1)
	 {
	   cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<"\n";
	 }
  }
}
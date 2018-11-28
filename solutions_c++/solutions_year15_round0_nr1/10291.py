#include<iostream>
using namespace std;
int main()
{
    int i,no=0,a=0,j;
	int t;
	cin>>t;
	int *max = new int[t];
	char **num = new char*[t];
	int **num1 = new int*[t];
	for(i=0;i<t;i++)
	{
	cin>>max[i];
	num[i] = new char[(max[i]+1)];
	num1[i] = new int[(max[i]+1)];
	cin>>num[i];
	}
	for(i=0;i<t;i++)
	{
		for(j=0;j<=max[i];j++)
		{
		num1[i][j] = num[i][j]-'0';	
		}
        for(j=0;j<max[i];j++)
   		{
		 no= no + num1[i][j];
		 if(no<(j+1))
		 {
 			a = a + ((j+1)-no);
 			no = no + ((j+1)-no);
 		}
		}
		cout<<"Case #"<<i+1<<": "<<a<<"\n";
		a=0;
		no=0;
	}
	return 0;
}
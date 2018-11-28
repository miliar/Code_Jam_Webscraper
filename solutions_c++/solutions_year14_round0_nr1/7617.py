/*Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).

If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here. 

*/
#include<iostream>
#include<cstdlib> 
using namespace std;
#define lli long long int
	
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int bsearch(int a[],int num)
{
	int n=4;
    int upper=n-1,lower=0,i=-1,j=0,flag=0;
    lower=0;
    int mid=0,c=0,temp=0;
    
    while(lower<=upper)
    {
        mid=(lower+upper)/2;
        if(a[mid]==num)
        {
            return 1;
        }
        else if(a[mid]>num)
            upper=mid-1;
        else lower=mid+1;
    }
    return 0;
}     
int main()
{
	int arr1[4],arr2[4];
	int r1,r2,dummy;
	lli T,casen=0;
	
	cin >> T;
	while(T--)
	{
		cin >> r1;
		for(int i=0;i<4;i++)
		{
			if(i==r1-1)
			{	
				for(int j=0;j<4;j++)
					cin >> arr1[j];
			}
			else
			{	
				for(int j=0;j<4;j++)
					cin >> dummy;	
			}		
		}	
		cin >> r2;
		for(int i=0;i<4;i++)
		{
			if(i==r2-1)
			{	
				for(int j=0;j<4;j++)
					cin >> arr2[j];
			}
			else
			{	
				for(int j=0;j<4;j++)
					cin >> dummy;	
			}
		}

		qsort(arr1, 4, sizeof(int), compare);
		qsort(arr2, 4, sizeof(int), compare);
		//for(int j=1;j<=4;j++)
		//	cout << "\n" << arr1[j] ;		
		int found=0,c=0,num=0;
		for(int i=0;i<4;i++)
		{
			found=bsearch(arr2,arr1[i]);
			if(found)
			{
				c++;
				num=arr1[i];
			}
			found=0;
		}
		casen=casen+1;
		cout << "Case #" << casen << ": ";
		if(c==1)
			cout << num;
		else if(c>1)
			cout << "Bad magician!";
		else if(c==0)
			cout << "Volunteer cheated!";
		cout << "\n";
		
		
	}
	return 0;
}


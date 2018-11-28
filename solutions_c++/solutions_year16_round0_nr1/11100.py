#include<iostream>
using namespace std;

void main() 
{
  int t;
  unsigned int number, origNum, num, orig_latestNum,latestNum,finalNumber;
  
  cin >> t;
  for (int k = 1; k <= t; ++k) 
  {
    cin >> num ; 
	int myArr[10]={1,0,0,0,0,0,0,0,0,0};
	if(num==0) 
	{ 
		cout << "Case #" << k << ": " << "INSOMNIA" << endl;
	}
	else
	{
		number = num;
		origNum = num;
		//myArr[num]=num;
		while(num>0)
		{
			num=num%10;
			myArr[num]=num;
			num=number/10;
			number=num;
		}
		int i =1;
		number = origNum;
		while(true)
		{
			 i++;
			 latestNum = i*number;
			 orig_latestNum = latestNum;
			 finalNumber = latestNum;
			 //myArr[latestNum] = latestNum;
			 while(latestNum>0)
			{
				latestNum=latestNum%10;
				myArr[latestNum]=latestNum;
				latestNum=orig_latestNum/10;
				orig_latestNum=latestNum;
			}
			if(myArr[0]==0 && myArr[1]==1 && myArr[2]==2 && myArr[3]==3 && myArr[4]==4 && myArr[5]==5 && myArr[6]==6 && myArr[7]==7 && myArr[8]==8 && myArr[9]==9)
			{
				cout << "Case #" << k << ": " << finalNumber << endl;
				break;
			}
		 }
	}
    
  }
}
#include <iostream>
#include <math.h>
using namespace std;

bool palind(int x){

	int y = x;
	int temp = 0;
	while(x>0)
	{
		temp = temp*10 + x%10;
		x /= 10;
	}

	if(temp==y)
		return true;
	return false;
}

bool square(int x){
	int z;
	double y = x;
	y = sqrt(y);
	z = int(y);
	if(y-z>0)
		return false;
	return (palind(z));
}

int main(){

	int x;
	int test, count=0;
	int beg, end;

	cin>>test;
	
	int *ptr;
	ptr = new int[test];

	for(int i=0;i<test;i++)
	{
		cin>>beg>>end;
		for(int j=beg;j<=end;j++)
		{
			if(palind(j))
			{
				if(square(j))
					count++;
			}
		}
		ptr[i] = count;
		count = 0;
	}

	for(int i=0;i<test;i++)
	{
		cout<<"Case #"<<i+1<<": "<<ptr[i]<<endl;
	}

	system("pause");
	return 0;
}
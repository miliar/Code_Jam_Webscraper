#include<iostream>
using namespace std;

static int arr[10] = {0};
static int count = 10;

int findDigits(int num)
{
	int rem = 0;
	int div = num;
	while(div != 0)
	{
		rem = div%10;
		div = div/10;
		
		if(arr[rem] == 0)
		{
			arr[rem] = 1;
			count--;
		}
	}
	
	if(num == 0)
		return 1;
		
	if(count == 0)
		return 2;
	else	
		return 3;
}

void reinitializeArray()
{
	for(int i = 0;i<10;i++)
		arr[i] = 0;
}

int main()
{
int T,N;
cin>>T;
int  i = 1;
int ret = 0;
for(int i1 = 0;i1<T;i1++)
{
cin>>N;
i = 1;
reinitializeArray();
count = 10;
while(1)
{
ret = findDigits(N*i);
if(ret == 1)
{
	cout<<"Case #"<<i1<<": ISOMANIA";
	cout<<endl;
	break;
}
else if(ret == 2)
{
	cout<<"Case #"<<i1<<": "<<N*i;
	cout<<endl;
	break;
}
i++;
}
}
return 0;
}


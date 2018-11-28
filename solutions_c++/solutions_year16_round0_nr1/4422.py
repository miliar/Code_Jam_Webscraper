#include<iostream>
using namespace std;
int main()
{
	int t,chk,n,itr,temp;
	cin>>t;
	for(int T=1;T<=t;T++)
	{	itr=1;
	chk=0;
		cin>>n;
		if(n==0)
		{cout<<"Case #"<<T<<": INSOMNIA"<<endl;
		}
		else
		{while(1)
		{temp =itr*n;
			while(temp)
			{
				switch(temp%10)
				{
					case 0:
						chk=chk|1;
						break;
					case 1:
						chk=chk|2;
						break;
					case 2:
						chk=chk|4;
						break;
					case 3:
						chk=chk|8;
						break;
					case 4:
						chk=chk|16;
						break;
					case 5:
						chk=chk|32;
						break;
					case 6:
						chk=chk|64;
						break;
					case 7:
						chk=chk|128;
						break;
					case 8:
						chk=chk|256;
						break;
					case 9:
						chk=chk|512;
						break;
				}
				temp=temp/10;
			}
			if(chk==1023)
				{
				cout<<"Case #"<<T<<": "<<itr*n<<endl;
				break;}
			itr++;}			
		}
		
		
	}
}

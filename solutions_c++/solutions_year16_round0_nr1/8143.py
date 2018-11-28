#include<iostream>
#include<map>
using namespace std;

int main()
{
	int T, temp, num, naming,i;
	cin >> T;
	for(i=1;i<=T;i++)
	{
		cin >> num;
		map<int,int> digitP;
		digitP.clear();
		int iter = 2;
		naming = num;
		while(1)
		{
			if(naming == 0)	
				break;
			temp = naming;				
			while(temp)
			{
				digitP[temp%10] = 1;
				temp = temp/10;			
			}
			int j;
			for(j=0;j<10;j++)
				if(digitP[j]!=1)
					break;
			if(j==10)
				break;
			naming = iter++ * num;
		}
		
		if(naming == 0)
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << i << ": " << naming << endl;
	}
}
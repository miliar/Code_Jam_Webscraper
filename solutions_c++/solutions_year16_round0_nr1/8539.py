#include<iostream>
#include<fstream>

using namespace std;
int main(){
	
	int test;
	cin>>test;
	
	for(int i = 0; i < test; i++)
	{
		int canSleep = 10;	
		int N;
		cin>>N;
		int inSomnia = 0;
		int digits[10] = {0,0,0,0,0,0,0,0,0,0};
		if(N == 0)
			inSomnia = 1;
		int finalNum = 0;
		int j = 1;
		while(canSleep != 0 && !inSomnia)
		{
			int x = j * N;
			finalNum = x;
			while(x > 0 && canSleep != 0)
			{
				int r = x % 10;
				if(digits[r] == 0)
				{
					canSleep--;
					digits[r]++;
				}
				x = x / 10;
			}
			j++;
		}
		
		if(canSleep == 0)
			cout<<"Case #"<<(i+1)<<": "<<finalNum<<endl;
		else
			cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
	}
	
}

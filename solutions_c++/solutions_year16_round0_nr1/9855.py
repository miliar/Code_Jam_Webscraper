#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

bool marked[10];
vector<int> number;
vector<int>::iterator beg = number.begin();
vector<int>::iterator it;

void reset()
{
	for(int i=0; i< 10 ; i++)
	{
		marked[i] = false;
	}
}
bool allMarked()
{
	for(int i=0; i< 10 ; i++)
	{
		if(marked[i] == false)
			return false;
	}
	return true;
}

/*void storetonum(int n)
{
	while(n!=0)
	{
		int c = n % 10;
		number.insert(beg,1,n);
		marked[c] = true;
		n = n /10;
	}
	for (it=number.begin(); it<number.end(); it++)
    	cout << ' ' << *it;
}*/

void markfor(int n)
{
	while(n!=0)
	{
		int c = n % 10;
		marked[c] = true;
		n = n /10;
	}
}

int main(void)
{
	int i,t,c;
	long long int n,pres;
	cin >> t;
	for(c=1; c<=t; c++)
	{
		i = 1;
		reset();

		cin >> n;
		//storetonum(n); // marked done here for i = 1
		
		if( n == 0)
		{
			cout << "Case #" << c <<": INSOMNIA" << endl; 
		}
		else{
			while(!allMarked())
			{
				pres = i * n;
				//cout << pres << endl;
				markfor(pres);
				i++;
			}
			cout << "Case #" << c <<": " << pres << endl; 
		}
	}

	return 0;
}
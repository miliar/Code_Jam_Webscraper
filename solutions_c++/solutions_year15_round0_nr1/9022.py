#include <iostream>
#include <math.h>
using namespace std;

int main()
{	long long int t;
	long long int Pneed,Pleft,money,n;
	long long int price,pages;
	int flag;
	string str;
	cin >> t;
    long long int extra=0;
    long long int cnt =0;
	for(int i=0;i<t;i++)
	{
		cin >> n;
		cin >> str;
		for(int i=0;i<str.size();i++)
		{
            if(str[i] != '0')
            {
                extra += str[i]-'1';
            }
            if(str[i]=='0')
            {
                if (extra>0)
                {
                extra--;
                }
                else
                {
                cnt++;
                }
            }
		}
		cout << "Case #" << (i+1) << ": " << cnt  << endl;
		cnt=0;
		extra=0;

    }
}

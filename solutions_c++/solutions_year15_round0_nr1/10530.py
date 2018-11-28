#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int ch;
	cin >> ch;
	int t=ch;
	
	while(ch--)
	{
		string s;
		int smax=0;
		int canstood=0;// 초대하면 일어날
		int already=0;//이미 일어남
		int invented=0;//초대할
		cin >> smax >> s;
		
		for (int i=0;i<=smax;i++)
		{
			
			int cur=s[i]-'0';
			if (i-already - invented - canstood<=0)
			{
				already+=cur;
			}
			else
			{
				invented += (i-already-invented-canstood);
				canstood += cur;
			}
		}
		
		cout <<"Case #" << t-ch <<": "<< invented << endl;
	}
	return 0;
}
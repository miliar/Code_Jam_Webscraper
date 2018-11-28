#include <iostream>
#include <stdio.h>
using namespace std;
string tmp ;

int main() {
	int t; 
	cin >> t ; 
	int cont =1;
	while (t--)
	{
		printf("Case #%d: ",cont++);
		int s ;
		cin >> s ;
		cin >> tmp;
		
		int acum, res=0;
		
		acum=tmp[0]-'0';

		for (int i = 1 ; i < tmp.size(); i++ )
		{
			int num = tmp[i]-'0';
			if (i>acum && num>0)
			{ 
				res+=(i-acum); 
				acum+=(i-acum);
			//	cout << "entra i= " << i << endl;  
			}
			acum+=num;	
		}
		cout << res << endl;
	}
	return 0;
}
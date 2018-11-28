#include <iostream>
#include <string>
#include <set>
using namespace std;

int main(){
	int t,n;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n;
		int s[10] ={0} ;
		int count = 0;
		for (int j = 1;j<=100000000; ++j)
		{
			string number = to_string(j*n);
			for (int k = 0; k < number.size(); ++k)
			{
				if(s[number[k]-'0']==0){
					s[number[k]-'0']=1;
					count++;
					
				}
			}
			if(count==10){
				cout << "Case #" << i << ": " <<number<<endl;
				break; 
			}
		}
		if(count<10)
			cout <<"Case #" << i << ": INSOMNIA"<< endl;
	}
}
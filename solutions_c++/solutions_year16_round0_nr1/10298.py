#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int ck[10];

int digits(int num){
	int dig;
	//cout << num<< endl;
	int flag=0;
	while (num != 0){
		dig = num%10;
		//cout << dig << endl;
		ck[dig]=1;
		num = num/10;
		//cout << "num="<<num<<endl;
		
	}
	//cout << "asda";
	for (int j=0;j<10;j++)
	{
		if (ck[j] == 0)
		{
			flag=1;
			break ;
		}
	}
	if (flag == 1)
		return 0;
	else 
		return 1;	
}




int main()
{
	int n,t;
	cin >> t;
	for(int i=0;i<t;i++){
		cin >> n;
		int flag=0;
		memset(ck, 0, sizeof(ck));
		if (n == 0)
			cout <<"CASE #"<<i+1<<": "<<"INSOMNIA"<<endl;
		else{
			
			for(int j =1;j<=100;j++){
			
				
				flag = digits(j*n);
				if (flag == 1){
				
					cout <<"CASE #"<<i+1<<": "<< j*n<< endl;
					break;
				}
			}
			
		}
		
		
		
	}
	
	  

}

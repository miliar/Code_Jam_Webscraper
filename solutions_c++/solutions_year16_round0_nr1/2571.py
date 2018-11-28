#include <iostream>


using namespace std;


int main(){

	int T;
	cin>> T;
	
	
	for( int t=1; t <= T; t++){

		
		int n;
		cin >> n;
		
		
		int digitsSeen[10];	
		memset( digitsSeen, 0, sizeof(int)*10);
		int digitsSeenCount = 0;
		
		if( n == 0)
		{	
			cout << "Case #" << t <<": " <<"INSOMNIA\n";
			continue;
		}

		int lastSeenNum;
		
		int i = 1;
		while(1){
			
			
			int num = n*(i++) ;
			lastSeenNum = num;
			
			
			//cout << " num " << num << " : ";
			while( num > 0 )
			{
				int digit = num %10;
				num = num/10;	
				if(!digitsSeen[digit] ){
					digitsSeenCount++;
					digitsSeen[digit] = 1;
					//cout << "(new)";
				}
				//cout << digit << " ";
			}
			
			if(digitsSeenCount == 10){
				break;
			}
			//cout <<"\n";
		}
		
		cout << "Case #" << t <<": " << lastSeenNum<<"\n";
		
	}
	
	
	
	
	
}
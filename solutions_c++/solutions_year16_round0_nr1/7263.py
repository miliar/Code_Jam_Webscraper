#include <iostream>
#include <string>
#define print(n,data) cout << "Case #" << n << ": " << data<<endl;
using namespace std;



int main()
{
	int c;
	cin >> c;
	int N;
	for(int i=1;i<=c;i++)
	{
		int checker=0;
		cin>>N;
		if(N == 0)
		{
			print(i,"INSOMNIA");
			continue;
		}

		int Nm=N;
		for(int j=1;;j++){
			Nm=N*j;
			while(Nm){
				checker |= (1<<Nm%10);
				Nm/=10;
			}
			if((checker ^ 0x3FF) == 0){
				print(i,N*j);
				break;
			}
		}


	}
}

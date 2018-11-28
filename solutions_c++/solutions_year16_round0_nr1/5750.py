#include "iostream"
#include <stack>
using namespace std;
bool check_digits(bool num[]){
	for (int i = 0; i < 10; ++i)
	{
		if(num[i]==false)
			return false;
	}
return true;
}

int main(){
unsigned long int t;
cin >>t;
unsigned long int tempt=1;
while(t--){
	bool num[10]={false};
	unsigned long int N;
	unsigned long int ans=0;
	cin >> N;

	if(N==0){
		cout << "Case #"<<tempt++<<":"<<" INSOMNIA"<<endl;
		continue;
	}
	else{unsigned long int k=1;
		while(true){
		//cal digits
		unsigned long	int NN=N*k++;
			
			ans=NN;
		while(NN){
			int b=NN%10;
			num[b]=true;
			NN/=10;


		}
		
		
		//check if all digits true;
		if(check_digits(num)!=false)
		{
			cout << "Case #"<<tempt++<<": "<<ans<<endl;
			break;
		}
	}



	
	}


}
return 0;
}
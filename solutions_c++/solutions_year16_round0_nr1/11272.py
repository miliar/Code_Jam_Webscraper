#include <iostream>
#include <set>
using namespace std;

int main(){
	int t;
	cin >> t;
	int cont=0;
	while(t--){
		int a;
		cin >> a;
		set <int> num;
		bool insonia=false;
		int b=a;
		int i;
		for(i=2;num.size()!=10;i++){
			if(a==0){
				insonia=true;
				break;
			}
			while(a!=0){
				num.insert(a%10);
				a /= 10;	
			}
			a = b*i;		
		}
		cont++;
		cout << "Case #" << cont << ": ";
		if(insonia){
			cout << "INSOMNIA" << endl;
		}
		else
			cout << b*(i-2) << endl;
		
	}
}

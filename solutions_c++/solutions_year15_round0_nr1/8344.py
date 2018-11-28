#include "iostream"
using namespace std;

int main(){
	int t,smax,var,count,need;
	cin >> t;
	for(int j=1; j<=t; j++){
		cin >> smax;
		string str;
		count = 0;
		need = 0;
		cin >> str;
		for(int i=0; i<=smax; i++){
			if(i > count && (int)((int)str[i]-48) != 0){			
				need += i - count;
				count = i;
			}
			count = count + (int)((int)str[i]-48);
		}
		cout << "case #" <<j<< ": " << need << endl;	
	}
}

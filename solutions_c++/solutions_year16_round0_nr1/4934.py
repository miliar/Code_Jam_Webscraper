#include<iostream>
#include<algorithm>

using namespace std;
int n, t, a;
bool isResult,tab[10];
int main(){
	cin>>t;
	for(int i = 0;i < t;i ++){
		isResult = false;
		cin>>n;
		cout<<"CASE #"<<i+1<<": ";
		if(n == 0) cout<<"INSOMNIA\n";
		else{
		for(int j = 0;j < 10;j++)tab[j] = false;
		int j = 1;
		while(!isResult){
			int tmp = j * n;
			while(tmp != 0){
				tab[tmp%10]++;
				tmp/=10;
			}
			isResult = true;
			for(int k = 0; k < 10; k++){
				if(tab[k]==0) isResult = false;
			}
			j++;
		}
		cout<<(j-1)*n<<endl;
		}
	}
	return 0;
}
		
		

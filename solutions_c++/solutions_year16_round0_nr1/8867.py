#include <iostream>
#define ll long long
using namespace std;

int t;
ll int num,bck,multiplier,res;
int arr[10];
bool flg;

int main(){
	
	cin>>t;
	for(int i=1 ; i <= t ; i++){
		multiplier = 1;
		flg = true;
		for(int i=0;i<10;i++) arr[i]=0;
		cin>>num;

		if(num == 0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		while(flg == true){
			bck = num;
			bck = bck * multiplier;
			res = bck;
			flg = false;
			while(bck){
				int tm = bck % 10;
				arr[tm] = 1;
				bck /= 10;
			}
			for(int i=0;i<10;i++)	if(arr[i]==0){	flg = true;break;}
			if(flg)	multiplier++;
		}

		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}
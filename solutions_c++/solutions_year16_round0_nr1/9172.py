#include <iostream>
#include <map>
using namespace std;

int main() {
	int t, t1=1, digit;
	bool flag;
	long long unsigned int n, n1, ans;
	cin>> t;
	while(t--){
		cin>>n;
		if(n == 0){
			cout<<"Case #"<<t1<<": INSOMNIA\n";
			t1++;
		}
		else{
			n1=n;
			map<int,bool> num;
			num[0]=false;
			num[1]=false;
			num[2]=false;
			num[3]=false;
			num[4]=false;
			num[5]=false;
			num[6]=false;
			num[7]=false;
			num[8]=false;
			num[9]=false;
			map<int, bool>::iterator it;
			for(int i=2;;i++){
				flag=true;
				while(n1>0){
					digit=n1%10;
					n1=n1/10;
					num.find(digit)->second=true;
				}
				for(it=num.begin(); it!=num.end(); it++){
					if(it->second==false){
						n1=n*i;
						flag=false;
						break;
					}
				}
				if(it==num.end()&&flag==true){
					ans=n*(i-1);
					cout<<"Case #"<<t1<<": "<<ans<<"\n";
					t1++;
					break;
				}
			}
		}
	}
	return 0;
}

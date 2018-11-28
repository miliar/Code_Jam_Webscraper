#include<iostream>
using namespace std;

string people;
int T,smax,num;

int main(){
	cin>>T;
	for(int test=1;test<=T;test++){
		int stand=0,ans = 0;
		cin>>smax>>people;
		stand += people[0] - '0';
		for(int i=1;i<=smax;i++){
			num = people[i] - '0';
			if(num>0){
				if(i>stand){
					ans += (i - stand);
					stand += ((i - stand) + num);
				}
					
				else if(i<=stand)
					stand+=num;
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<"\n";
	}

	return 0;
}

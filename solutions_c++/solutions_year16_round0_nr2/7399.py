#include <iostream>
#include <string>
using namespace std;
int main(){
	int n,ll=1;
	cin>>n;
	string c;
while(n--){
	cin>>c;
	int t=0;
	//cout<< c.size();
		while(1){
			int count=0;
			for(int i=0;i<c.size();i++){
				if(c[i]=='+'){
					count++;
				}
			}
			if(count==c.size()){
				break;
			}
			int s=0,mm=0;
			for(int i=c.size();i>=0;i--){
				if(c[i]=='-'){
					mm=i;
					s=1;
					break;
				}
			}
			//cout<<"mm"<<mm <<"s"<<s;
			if(s==1){
				for(int j=0;j<=mm;j++){
					if(c[j]=='-'){
						c[j]='+';
					}
					else if(c[j]=='+'){
						c[j]='-';
					}
				}
				t++;
			}
		}
		cout<<"Case #"<<ll<<": "<<t<<endl;	
    ll++;
  }
}


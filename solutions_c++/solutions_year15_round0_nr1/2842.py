#include <fstream>
#include <string>
using namespace std;

int t;
int n;
string inp;

ifstream cin("1.in");
ofstream cout("1.out");

int main(){
	cin>>t;
	for(int g=1;g<=t;g++){
		cin>>n;
		cin>>inp;
		int num=0;
		int sol=0;
		for(int i=0;i<=n;i++){
			if(num<i){
				sol+=i-num;
				num=i;
			}
			num+=inp[i]-'0';
		}
		cout<<"Case #"<<g<<": "<<sol<<endl;
	}
}
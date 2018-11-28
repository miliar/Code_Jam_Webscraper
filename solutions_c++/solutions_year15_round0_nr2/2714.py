#include <fstream>
#include <string>
using namespace std;

int t;
int n;
int arr[1111];
int tmp;
int sol;
int num;
string inp;

ifstream cin("1.in");
ofstream cout("1.out");

int main(){
	cin>>t;
	for(int g=1;g<=t;g++){
		cin>>n;
		num=0;
		sol=100000;
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		for(int i=1;i<=1000;i++){
			num=0;
			for(int j=0;j<n;j++){
				num+=(arr[j]-1)/i;
			}
			sol=min(sol,num+i);
		}
		cout<<"Case #"<<g<<": "<<sol<<endl;
	}
}
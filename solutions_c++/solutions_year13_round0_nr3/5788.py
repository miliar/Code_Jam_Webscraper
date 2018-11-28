#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int t;
	cin>>t;
	int x=1;
	ofstream myfile;
	myfile.open ("output.txt");
	if(t>=1 && t<=101){
		while(t>0){
			int count=0;
			int a,b;
			cin>>a>>b;
			int i=1;
			while(i*i<=b){
				if(i*i<a){
					i++;
					continue;
				}
				else
				{
					int num=i*i;
					int n = num;
					int rev = 0;
					int dig;
					while (num > 0){
						dig = num % 10;
						rev = rev * 10 + dig;
						num = num / 10;
					}
					if(n==rev){
						int num1=i;
						int n1 = num1;
						int rev1 = 0;
						int dig1;
						while (num1 > 0){
							dig1 = num1 % 10;
							rev1 = rev1 * 10 + dig1;
							num1 = num1 / 10;
						}
						if(n1==rev1){
							count++;
						}
					}
				}
				i++;
			}
			myfile<<"Case #"<<x<<": "<<count<<"\n";
			x++;
			t--;
		}
	}	
	myfile.close();
	return 0;
}
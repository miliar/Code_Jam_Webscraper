#include<iostream>
#include<string.h>
using namespace std;
int main(int argc, char *argv[])
{
    int i;
	cin>>i;
	string a = "";
	string b = "";
	char max = '\0';
	char min = '\0';
	for (int j = 1; j <= i; j++) {
		a = "";
		b = "";
		cin>>a;
		b = b + a[0];
		max = a[0];
		min = a[0];
		for (int p = 1; p < a.length(); p++) {
			if(a[p] >= max){
				b = a[p] + b;
				max = a[p];
			}
			else {
				b = b + a[p];
				min = a[p];
			}
		}
		cout<<"Case #"<<j<<": "<<b<<endl;

	}

}

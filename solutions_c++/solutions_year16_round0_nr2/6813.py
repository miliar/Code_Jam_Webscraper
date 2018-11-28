#include<iostream>
using namespace std;
int main (){
	int cases ;
	cin >> cases;
	for(int cse= 1 ; cse<=cases; cse ++){
		cout<<"Case #"<<cse<<": ";
		string b,a ; 
		cin >>b;
		for(int i =0 ; i <b.size(); i ++)
			if( a.size() ==0 || a[a.size()-1] !=b[i]) a += b[i];
		
		while(a[a.size()-1]=='+') a = a.substr(0,a.size()-1);
		cout<<a.size()<<endl;
	}
}

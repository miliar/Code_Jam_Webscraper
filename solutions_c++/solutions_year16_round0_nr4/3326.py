#include<iostream>
using namespace std;

int main() {
	int test,tt,tiles,complexity ,students;
	cin>>test;


	for(int i=1; i<=test;i++)
   {
    cin>> tiles>> complexity >> students;
       cout<<"Case #"<<i<<":";
       for (int j=1; j<=students ; j++)
       cout<<" "<<j;
       cout<<endl;
   }
       return 0;


   }
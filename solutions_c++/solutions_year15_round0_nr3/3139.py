#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
int main(){
	long long int i1,l,x,i,t,mi,ct,ev;
	cin>>t;
	int ar[4][4]={{1,2,3,4},
		      {2,-1,4,-3},
		      {3,-4,-1,2},
		      {4,3,-2,-1}};
	char arr[10000];
	for(int i1=0;i1<t;i1++){
		ct=0;
		mi =2;
		ev = 1;
		cin>>l;
		cin>>x;
		cin>>arr;
		i=0;
		while(ct<x){
			int sign = ev/abs(ev);
			ev = sign*ar[abs(ev)-1][int(arr[i]-'h')];
			i++;
			if(i>=l){
			i=0;
			ct++;
			}
			if(ev==mi && mi!=4){
			mi++;
			ev = 1;
			}
		
		}
		if(mi==4 && ev==4)
			cout<<"Case #"<<i1+1<<": "<<"YES"<<endl;
		else
			cout<<"Case #"<<i1+1<<": "<<"NO"<<endl;

	}
}	

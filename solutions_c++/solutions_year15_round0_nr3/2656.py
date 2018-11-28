#include<bits/stdc++.h>

using namespace std;

int table[8][8]={ 
{ 0 ,1 ,2 ,3 ,4 ,5 ,6 ,7},
{ 1 ,4 ,3 ,6 ,5 ,0 ,7 ,2},
{ 2 ,7 ,4 ,1 ,6 ,3 ,0 ,5},
{ 3 ,2 ,5 ,4 ,7 ,6 ,1 ,0},
{ 4 ,5 ,6 ,7 ,0 ,1 ,2 ,3},
{ 5 ,0 ,7 ,2 ,1 ,4 ,3 ,6},
{ 6 ,3 ,0 ,5 ,2 ,7 ,4 ,1},
{ 7 ,6 ,1 ,0 ,3 ,2 ,5 ,4}
};

int main(){
	
	int t,l,x;
	
	cin>>t;
	
	for(int j=1;j<=t;j++){
		
		int left[10100],right[10100];
		set<int> lefts,rights;
		
		string str,temp;
		
		cin>>l>>x;
		cin>>temp;
		
		for(int i=0;i<x;i++)
			str=str+temp;
			
		left[0]=str[0]-'i'+1;
		right[l*x-1]=str[l*x-1]-'i'+1;
			
		if(left[0]==1)
			lefts.insert(0);
			
		if(right[l*x-1]==3)
			rights.insert(l*x-1);
		
		for(int i=1;i<l*x;i++){
			left[i]=table[left[i-1]][str[i]-'i'+1];
			
			if(left[i]==1)
				lefts.insert(i);
				
		}
		
		for(int i=l*x-2;i>=0;i--){
			right[i]=table[str[i]-'i'+1][right[i+1]];
			
			if(right[i]==3)
				rights.insert(i);
		}
		
		if(left[l*x-1]!=4)
			cout<<"Case #"<<j<<": "<<"NO"<<endl;
			
		else{
			set<int>::iterator it;
			for(it=lefts.begin();it!=lefts.end();it++){
				if(rights.lower_bound(*it+1)!=rights.end()){
					cout<<"Case #"<<j<<": "<<"YES"<<endl;
					break;
				}
			}
			
			if(it==lefts.end())
				cout<<"Case #"<<j<<": "<<"NO"<<endl;	
		}
	}
	
	return 0;
}
		
		
	
	

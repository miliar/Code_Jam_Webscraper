#include<bits/stdc++.h>
#include<iostream>
#include<string.h>
using namespace std;
bool visited[10];

bool all_visited(){
	for(int i=0;i<10;i++){
		if(!visited[i])
			return false;
	}
	return true;
}
int find_last_number(int n){
	int rem,last_number=0,i=1,m=n;
	while(!all_visited()){
		last_number = n;
		while(n > 0){
			rem = n%10;
			visited[rem] = true;
			n /= 10;
		}
		n = m*(i+1);
		i++;
		//cout<<m<<" is multiplied with "<<i<<" ="<<n<<endl; 
	}
	return last_number;
}
int main(){


	int t, n, m,i;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	i = 1;
	while(t--){
		cin>>n;
		memset(visited,false,sizeof(visited));
		if(n == 0){
			//cout<<"INSOMIA"<<endl;
			cout << "Case #" << i << ": " <<"INSOMNIA"<< endl;
		}else{
			cout << "Case #" << i << ": " <<find_last_number(n)<< endl;
		}
		i++;
	}
	return 0;
}
#include <iostream>
using namespace std;

int res(string a, string b){
	int sum = 0;
	int i=0, j=0;
	while( i<a.length() or j<b.length() ){
		if( a[i] == b[j] ){ i++; j++; continue;}
		else if(i>0 and a[i] != b[j] and a[i] == a[i-1] ){
			i++;
			sum++;
		}
		else if(j>0 and a[i] != b[j] and b[j] == b[j-1] ){
			j++;
			sum++;
		}
		else
			return -1;
		
	}
	return sum;
}

int main(int argc, char *argv[]) {
	string a,b;
	int n,t;
	cin>>n;
	
	for(int i = 1 ; i <= n ; i++ ){
		cin>>t;
		
		cin>>a;
		cin>>b;
		
		int r = res(a,b);
		if(r==-1)
			cout<<"Case #"<<i<<": "<<"Fegla Won"<<endl;
		else
			cout<<"Case #"<<i<<": "<<r<<endl;
	}
	return 0;
}



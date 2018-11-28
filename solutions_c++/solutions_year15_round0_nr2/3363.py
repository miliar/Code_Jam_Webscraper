#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

long long spDiv(long long a,long long b){
	long long c = a/b;
	
	if(a%b == 0){
		c--;
	}
	
	return c;
}

int main(){
	
	freopen ("B-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
	
	long long t;
	cin>>t;
	
	long long cases = 1;
	
	while(t--){
		long long max;
		cin>>max;
		
		long long maxEl = 0;
		
		long long arr[max];
		
		for(long long i=0;i<max;i++){
			cin>>arr[i];
			if(arr[i] > maxEl){
				maxEl = arr[i];
			}
		}
		
		
		long long minT = maxEl;
		
		for(long long m = maxEl; m>0; m--){
			long long sm = 0;
			for(long long i=0;i<max;i++){
				sm += spDiv(arr[i],m);
			}
			
			if(m+sm < minT){
				minT = m+sm;
			}
		}
		
		cout<<"Case #"<<cases<<": "<<minT<<endl;
		cases++;
	}
	
	fclose(stdin);
	fclose(stdout);
}

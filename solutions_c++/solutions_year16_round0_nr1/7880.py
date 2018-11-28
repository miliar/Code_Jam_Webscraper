#include <iostream>
using namespace std;

int fun1(int arr[]){
    for(int i=0; i<10; i++)
        if(arr[i]==0)
            return 1;
    return 0;
}

int main() {
	long long t, i, j, n, temp, temp1;
	int arr[10], tt;
	cin>>t;
	for(i=1; i<=t; i++){
	    temp=0;
	    for(j=0;j<10;j++)
	        arr[j]=0;
	    cin>>n;
	    if(n==0){
	        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	        continue;
	    }
	    while(fun1(arr)){
	        temp += n;
	        temp1=temp;
	        while(temp1){
	            tt=temp1%10;
	            if(arr[tt]==0)
	                arr[tt]=1;
	            temp1 /=10;
	        }
	    }
	    
	    cout<<"Case #"<<i<<": "<<temp<<endl;
	    
	}
	return 0;
}


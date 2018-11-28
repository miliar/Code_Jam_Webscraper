#include<iostream>
using namespace std;
long arr[100][10];
bool flag;

void compute(long p,int i){
	for(;p>0;p/=10){
		int j = p%10;
		arr[i][j] = 1;
	}
	int c=0;
	for(int k=0;k<10;k+=1){
		if(arr[i][k]==1){
			c++;
		}
	}
	if(c==10){
		flag=true;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=0;i<t;i+=1){
		for(int j=0;j<10;j+=1){
			arr[i][j]=0;
		}
	}
	for(int i=0;i<t;i+=1){
		int n=1;
        long p;
        flag = false;
		cin >> p;
        if(p!=0){
		  while(!flag){
			 compute(n*p,i);
			 n++;
		  }
		  cout << "Case #" << i+1 << ": " << (n-1)*p << endl;
        }
        else{
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
	}
	return 0;
}


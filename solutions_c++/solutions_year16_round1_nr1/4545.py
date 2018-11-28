#include <iostream>
#include <cstring>
using namespace std;

int main() {
	// your code goes here
	int n,t,i,j,k;
	char temp[1000];
	char a[1000],b[1000];
	cin>>n;
	for(t=1;t<=n;t++){
		cin>>a;
		for(i=0;i<1000;i++) b[i]=0;
		
		b[0]=a[0];
		j=0;
		for(i=1;a[i];i++){
			if(a[i]>=b[0]){
				temp[0]=a[i];
				strcpy(temp+1,b);
				strcpy(b,temp);
			}
			else{
				b[i]=a[i];
			}
		}
		b[i]=0;
		cout<<b<<endl;
	}
	return 0;
}
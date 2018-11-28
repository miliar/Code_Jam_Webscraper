#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,x,n;
	int remainder;
	cin>>x;
	for(int j=1;j<=x;j++){
		cin>>n;
		cout<<"Case #"<<j<<": ";
		t=n;
		int temp=0,c = 1000,a[10]={0};
		while(c>0){
			//if(n==0){c=0;break;}
			temp = temp + n;
			t = temp;
			while (t != 0)
			 {
		      remainder = t % 10;
		      a[remainder]=1;
		      t = t / 10;
		   }
		   int i=0;
		   while(i<10){
		   	if(a[i]!=1)
		   	break;
		   	i++;
		   }
		   if(i==10)
		   	break;
		   	c--;
	   }
	   if(c==0)
	    cout<<"INSOMNIA";
	   else
	    cout<<temp;
	    //c=10;while(c--){cout<<a[c];}
	   cout<<endl;
	}
	return 0;
}
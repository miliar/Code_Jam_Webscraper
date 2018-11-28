#include <iostream>
using namespace std;

int main() {
	
	int t,j,flag,n,temp,sum,nu;
	bool a[10];
	cin>>t;
    for(int i=1;i<t+1;i++){
        for(int y=0;y<10;y++)
            a[y]=false;
	    cin>>n;
	    flag=0;
	    if(n==0){
	        cout<<"Case #"<<i<<": INSOMNIA\n";
	        continue; }
	    temp=n;
	    for(j=2;flag!=1;j++){
	           sum=0;
	           while(temp>0){
	               nu=temp%10;
	               a[nu]=true;
	               temp=temp/10;
	           }
	           for(int k=0;k<10;k++){
	                if(a[k]==false)
	                    break;
	                else
	                    sum++; }
	           if(sum==10)
	                flag=1;
	           temp=j*n;
	    }
	    cout<<"Case #"<<i<<": "<<(j-2)*n<<"\n";
	}
	return 0;
}


#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,j,flag,n,temp,count,num;
	bool a[10];
	cin>>t;
    for(int i=1;i<t+1;i++){
        for(int i=0;i<10;i++)
            a[i]=false;
	    cin>>n;
	    flag=0;
	    if(n==0){
	        cout<<"Case #"<<i<<": INSOMNIA\n";
	        continue; }
	    temp=n;
	    for(j=2;flag!=1;j++){
	           count=0;
	           while(temp>0){
	               num=temp%10;
	               a[num]=true;
	               temp=temp/10;
	           }
	           for(int k=0;k<10;k++){
	                if(a[k]==false)
	                    break;
	                else
	                    count++; }
	           if(count==10)
	                flag=1;
	           temp=j*n;
	    }
	    cout<<"Case #"<<i<<": "<<(j-2)*n<<"\n";
	}
	return 0;
}


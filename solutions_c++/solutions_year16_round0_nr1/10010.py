#include <iostream>
#include<set>
using namespace std;
int count(int number);
int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int f=1;f<=t;f++){
	    set<int> myset;
	    set<int> meraset;
	    set<int>::iterator it;
	    int n,flag=0,a,p;
	    for(int k=0;k<10;k++){
	            myset.insert(k);
	         }
	    cin>>n;
	    if(n==0){
	        std::cout << "Case #"<<f<<": INSOMNIA" << std::endl;
	    }
	    else{
	        for(int i=1;i<=100;i++){
	            a=i*n;
	            p=a;
	            int r=count(a);
	            for(int j=0;j<r;j++){
	                int s= a%10;
	                meraset.insert(s);
	                a/=10;
	            }
	           
	            if(myset==meraset){
	                flag=1;
	                break;
	            }
	        }
	        if(flag){
	            cout<<"Case #"<<f<<": "<<p<<endl;
	        }
	    }
	    
	}
	return 0;
}
int count(int number)
{
    int digits = 0;
    if (number < 0) digits = 1; 
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}
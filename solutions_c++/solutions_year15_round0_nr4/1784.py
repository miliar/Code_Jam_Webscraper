#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<stack>
using namespace std;

main(){
	ifstream in("D-small-attempt0.in");
	ofstream out("output.txt");
    int t;
    in>>t;
    int c,x,area,n,max,min;
    for(int i=1;i<=t;i++){
    	in>>n>>c>>x;
    	area=c*x;
    	int f=0;
    	if(x>c){max=x;
    	        min=c;
		}
    	 
    	else{max=c;
    	     min=x;
		}
    	 for(int kk=0;kk<4;kk++)
    	          if(kk==2)
    	          break;
    	if(area%n!=0)
    	 f=1;
    	if(n>max)
    	 f=1;
    	int half;
    	if(n%2==1)
    	 half=(n/2)+1;
    	else
    	 half=n/2;
    	if(n==4)
    	 half=3;
    	if(half>min)
    	 f=1;
    	if(n>=7)
    	 f=1;
    	out<<"Case #"<<i<<": ";
    	if(f==0)
    	 out<<"GABRIEL"<<endl;
    	else
    	 out<<"RICHARD"<<endl;
	}
}

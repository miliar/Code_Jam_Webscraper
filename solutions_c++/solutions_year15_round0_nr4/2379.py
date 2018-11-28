#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<stack>
using namespace std;

main(){
	ifstream in("D-small-attempt1.in");
	ofstream out("out.txt");
    int test;
    in>>test;
    int x,n,area,c,max1,min1;
    for(int i=1;i<=test;i++){
    	in>>n>>c>>x;

    	area=c*x;
    	int flag=0;
    	if(x>c){
            max1=x;
            min1=c;
		}
    	else{
            max1=c;
            min1=x;
		}

    	if(area%n!=0)
    	 flag=1;
    	if(n>max1)
    	 flag=1;
    	int half;
    	if(n%2==1)
    	 half=(n/2)+1;
    	else
    	 half=n/2 ;
    	if(n==4)
    	 half=3;
    	if(half>min1)
    	 flag=1;
    	if(n>=7)
    	 flag=1;
    	out<<"Case #"<<i<<": ";
    	if(flag==0)
    	 out<<"GABRIEL"<<endl;
    	else
    	 out<<"RICHARD"<<endl;
	}
}

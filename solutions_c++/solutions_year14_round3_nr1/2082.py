//Copyright (C) 2014 Akshay Ratan

#include <iostream>

using namespace std;

int main() {
    int t,c,p,q,xn=0;
    std::cin>>t;char ch;
	while(t--)
    {	c=0;
        xn++;
        std::cin>>p>>ch>>q;
	
		
		if(q%2==1){
            std::cout<<"Case #"<<xn<<": impossible"<<"\n";
		}
		else{
		while(q>p){
			q=q/2;
            c++;  //Simply incrementing
		}
        std::cout<<"Case #"<<xn<<": "<<c<<"\n";
	}
    }

    return 0;
}

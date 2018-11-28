#include<iostream>
#include<fstream>
#include<vector>
#include<algorithem>

using namespace std;
main(){
    ifstream in("D-small-attempt5.in");
    ofstream out("output.txt");

    int a;
    in>>a;
    
    for(int l=1;l<=a;l++){
    	int x,w,b;
        in>>x>>w>>b;
        int z=w*b, f=0;
		int ma=max(w,b); 
		int min1=min(w,b);
		int hal;
		if(x%2==0)
		hal=x/2;
		else
		hal=x/2+1;
		if(z%x!=0||x>ma||hal>min1||(x==4 && 3>min1))
		f=1;
			
		if(f==1)
			out<<"Case #"<<l<<": RICHARD"<<endl;
		else
			out<<"Case #"<<l<<": GABRIEL"<<endl;
    }



}

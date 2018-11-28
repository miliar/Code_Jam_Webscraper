#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
#include<functional>
#include<map>
#include<math.h>
#include<cmath>
#include<fstream>
using namespace std;
int main (){
	int n,m,count,p,j=1,output;
	ifstream infile("codejam.txt");
	ofstream offile("output.txt");
    infile>>n;
    while(infile>>m){
    	map<int,int> mm;
    	count = 0 ;
    	int a[10] = {0};
    	int i = 2;
    	p = m;
    	while(mm[p]==0){
    		mm[p] = 1;
    		output = p;
    		while(p>0){
    			//cout<<(abs)(a[p%10]-1)<<"\n";
    			count += (abs)(a[p%10]-1);
    			a[p%10] = 1;
    			p=p/10;
			}
		//	cout<<mm[m]<<" "<<count<<" ";
			if(count >= 10)
			   break;
			p = (i++)*m;
		
		}
		offile<<"Case #"<<j++<<": ";
		if(count >= 10){
			offile<<output<<"\n";
		}else{
		    offile<<"INSOMNIA\n";
		}
	}

}


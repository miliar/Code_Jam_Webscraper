#include<iostream>
#include<fstream>

using namespace std;

int main(){	
	long long i,j,r,t,count=0,paintreq=0;
	int notc,caseno=1;
	ifstream pin("in.txt");
	ofstream pout("out.txt");
	pin>>notc;
	while(caseno<=notc){
		count=0;
		paintreq=0;
		i=0;
		j=1;
		pin>>r>>t;
		while(paintreq<=t){
			paintreq=((r+j)*(r+j))-((r+i)*(r+i));
			if(paintreq<=t){
				count++;
				t=t-paintreq;
			}
			i+=2;
			j+=2;		
		}
		pout<<"Case #"<<caseno<<": "<<count<<endl;
		cout<<"Case #"<<caseno<<": "<<count<<endl;
		caseno++;
	}
	pin.close();
	pout.close();
	//cout<<count;
	return 0;
}

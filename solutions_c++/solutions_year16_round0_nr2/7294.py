#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{	
	ifstream File;
    File.open("ip.txt");
  while(!File.eof())
  {
  	int t=0;
	File >>t;
	for(int x=1;x<=t;x++) {
		string c;
		int flag =0;
		File>>c;
		for(int i=0;i<=c.size();i++) {
    		if(c[i]=='-') {c[i]='0';}
    		else {c[i]='1';}
		}
		for(int i =0;i<=c.size();i++) {
    		if(c[i]!=c[i+1]){ 
    			int k=i+1;
    			flag++;
    			while(k){
        			c[k-1]=c[i+1];
        			k--;
        		}
        	}
		}
	if(c[0]=='0'){ flag++;}
	ofstream File1;
    File1.open("Op.txt", ios::app);
	File1<<"Case #"<<x<<": "<<flag-1<<endl;
	File1.close();
	}

} File.close();
 	return 0;
}
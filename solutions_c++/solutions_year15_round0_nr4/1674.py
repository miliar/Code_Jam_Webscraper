
#include<vector>
#include<fstream>
#include<iostream>
#include<string>
using namespace std;

int main(int argc, char* argv[])
{
	string inputfilename="input.txt";
	string outputfilename="output.txt";
	ifstream infile(inputfilename);
	ofstream OF(outputfilename);
	int T;
	infile>>T;

	for(int icase=0;icase<T;icase++){
		string answer;
		int x,r,c;
		int tmp;
		infile>>x>>r>>c;

		if(c>r) {  //make sure r>=c
			tmp=r;
			r=c;
			c=tmp;
		}

		//int iflag=-1;  //0 for richard, 1 for gabriel
		
		cout<<x<<" "<<r<<" "<<c<<endl;
		cout<<(r*c)%x<<endl;
			
		answer="GABRIEL";

		if((r*c)%x!=0||(x>r&&x>c)){
			answer="RICHARD";	
		}
		if(x%2==1){
			if((x/2)+1>r||(x/2)+1>c)
				answer="RICHARD";	
		}
		if(x%2==0){
			if((x/2)+1>r||(x/2)>c)
				answer="RICHARD";	
		}
		if(x==4&&r==4&&c==2) answer="RICHARD";

	
		OF<<"Case #"<<icase+1<<": "<<answer<<endl;
	}

		

	infile.close();
	OF.close();
	return 0;
}


#include <iostream>
//#include <map>  
//#include <vector>
#include <set>  
#include <string>
#include <string.h>
#include <fstream>

using namespace std;

int n,m,count1;

int map[201];

//4
//2 20 10
//2 10 0
//4 25 25 25 25
//3 24 30 21


void main() {
    int t=0,i1=0,flag,j,sum;
	float a;
	string word1,word2,filename;
	string lines;
	count1=0;
	ifstream in("D:\\Program Files\\Microsoft Visual Studio\\MyProjects\\poj\\A-small-attempt0.in");
	ofstream examplefile ("test.txt");//count/test.txt
	if(in && examplefile.is_open()){
		//getline (in, lines);
		in>>count1;
		cout<<count1<<endl;
		//getline (in, lines);
		for(int i4=0;i4<count1;i4++){
			
			examplefile<<"Case #"<<++t<<": ";
					
			in>>n>>m;
			cout<<"n:"<<n<<" m:"<<m<<endl;
			sum = 0;j=0;
			while(sum<=m){
				sum+=(n+1)*(n+1)-n*n;
				cout<<"sum:"<<sum<<endl;
				j++;
				n+=2;
			}
			cout<<"j:"<<--j<<endl;
			examplefile<<j<<endl;
		
		}
	/*	while(getline (in, lines)){  // have no '\n',
			
		
//			cout<<lines<<" "<<lines.size()<<endl;
//			examplefile<<"Case #"<<t++<<": ";
//			for(int i4=0;i4<lines.size();i4++){
//				
//			}
			examplefile<<endl;
	
			//break;
			 // ;
			// store the lines to a vector or list, use method insert
		}*/
		// ...
	}else{
		// open file fail....
	} 
	in.close();
	examplefile.close();

	/*ofstream examplefile ("count/±¾.txt");
	if(examplefile.is_open()) {
		examplefile << "This is a line.\n";
		examplefile << "This is another line.\n";
		examplefile.close();
	}*/
	
   // return 0;
}

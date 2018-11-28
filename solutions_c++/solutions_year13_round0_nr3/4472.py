#include <iostream>
//#include <map>  
//#include <vector>
#include <set>  
#include <string>
#include <string.h>
#include <fstream>
//#include <algorithm>  

using namespace std;

int n,m,count1;
char fn[26]="count/documents/1.txt";


char map[15];

int sqrt(int x){
	int a=0,b=x,mid;
	while(a<=b){
		mid=(a+b)/2;
		if(mid*mid>x){
			b=mid-1;
		}else if(mid*mid<x){
			a=mid+1;
		}else{
			return mid;
		}
	}
	if(a>=b)return 0;
}
int judge(int x){
	//cout<<"x:"<<x<<endl;
	int size=0;
	if(x==1000)return 0;
	if(x/100){
		if(sqrt(x)){
			if(x/100==x%10)return 1;			
		}
		return 0;
	}else if(x/10){
		if(sqrt(x)){
			if(x/10==x%10)return 1;			
		}
		return 0;
	}else{
		if(x==1||x==4||x==9)return 1;
	}
	return 0;
}


void main() {
    int t=0,i1=0,flag,j;
	int c=0;
	string word1,word2,filename;
	int a,b;
	string lines;
	count1=0;
	ifstream in("D:\\Program Files\\Microsoft Visual Studio\\MyProjects\\poj\\C-small-attempt0.in");
	ofstream examplefile ("test.txt");//count/test.txt
	if(in && examplefile.is_open()){
		//getline (in, lines);
		in>>count1;
		cout<<count1<<endl;
		//getline (in, lines);
		//cout<<sqrt(121)<<endl;
		for(int i4=0;i4<count1;i4++){
			
			examplefile<<"Case #"<<++t<<": ";
			c=0;		
			in>>a>>b;
			cout<<"a:"<<a<<" b:"<<b<<endl;
			if(a<=1&&b>=1)c++;
			if(a<=4&&b>=4)c++;
			if(a<=9&&b>=9)c++;
			if(a<=121&&b>=121)c++;
			if(a<=484&&b>=484)c++;
			/*for(i1=a;i1<=b;i1++){
				if(judge(i1)){
					c++;
					cout<<"::"<<i1<<endl;
				}
			}*/
			//cout<<"word1:"<<word1<<endl;
			//cout<<"word2:"<<word2<<endl;
			/*for(i1=0;i1<n;i1++){
				for(j=0;j<m;j++){
					in>>map[i1][j];
				}				
			}
			flag=1;
			for(i1=0;i1<n;i1++){
				for(j=0;j<m;j++){
					if(judge(i1,j)==0){
						flag=0;		
						break;
					}
					//cout<<map[i1][j]<<" ";
				}//cout<<endl;				
			}
			
			if(flag){
				cout<<"YES"<<endl;
				examplefile<<"YES"<<endl;
			}else{
				cout<<"NO"<<endl;
				examplefile<<"NO"<<endl;
			}*/
			cout<<c<<endl;
			examplefile<<c<<endl;
		//	cout<<endl;
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

 #include<iostream>
 #include<vector>
 #include<fstream>
 
 using namespace std;
 
 int main(){
 	ifstream inputfile;
 	inputfile.open("B-large.in");
 	ofstream outfile;
 	outfile.open("B-large.out");
 	int cases;
 	string s;
 	inputfile>>cases;
 	for(int i=0;i<cases;i++){
 		inputfile>>s;
 		outfile<<"Case #"<<(i+1)<<": ";
 		int signe=-1;
 		if(s[0]=='+')signe=-signe;
 		char c=s[0];
 		int count=0;
 		for(int x=1;x<s.length();x++){
 			if(c!=s[x]){
 				count++;
 				signe=-signe;
 				c=s[x];
 			}
 		}
 		if(signe<0)count++;
 		outfile<<count<<endl;
 	}
 	inputfile.close();
 	outfile.close();
}

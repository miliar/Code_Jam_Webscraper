 #include<iostream>
 #include<vector>
 #include<fstream>
 
 using namespace std;
 
 int main(){
 	ifstream inputFile;
 	inputFile.open("A-large.in");
 	ofstream outfile;
 	outfile.open("output-A-large.out");
 	int cases;
 	inputFile>>cases;
 	long long N;
 	for(int i=0;i<cases;i++){
 		inputFile>>N;
 		outfile<<"Case #"<<(i+1)<<": ";
 		if(N==0){
 				outfile<<"INSOMNIA"<<endl;
 				continue;
 		}
 		vector<bool> v(10,false);
 		long long aux;
 		int xx=0;
 		do{
		 	xx++;
 			aux=N*xx;
 			while(aux!=0){
 				v[aux%10]=true;
 				aux/=10;
 			}
 		}	
 		while(v[0]*v[1]*v[2]*v[3]*v[4]*v[5]*v[6]*v[7]*v[8]*v[9]==0);
 		outfile<<N*xx<<endl;
	 }
	 inputFile.close();
	 outfile.close();
 }

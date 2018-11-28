#include <bits/stdc++.h>
#include <fstream>

using namespace std;
ofstream out;
ifstream inp;


void openFile(){
//	inp.open("B-small-attempt1.in");
//  	out.open("B-small-attempt1.ou");
	inp.open("B-large.in");
  	out.open("B-large.ou");
}
void closeFile(){
  inp.close();
  out.close();
}
void swap(string& s,int d,int c){
	for(int i=d;i<=c;i++) {
		if(s[i]=='-'){
			s[i]='+';
		}else{
			s[i]='-';
		}
	}
	
	while(d<c){
		char tmp=s[d];
		s[d]=s[c];
		s[c]=tmp;
		d++;c--;
	}
}
void mainWork(){
	string s;
	int TC;
	
	inp>>TC;
	for(int t =0;t<TC;t++){
		out<<"Case #"<<t+1<<": ";
		inp>>s;
		int c,n=0;
		c=s.length()-1;
		while (c>=0){
			
			while (c>=0 && s[c]=='+')c--;
			if(c<0) break;
			//cout<<c<<endl;
			//chinh dau de swap
			int i=0;
			while(i<=c && s[i]=='+')i++;
			if(i>0){
				swap(s,0,i-1);
				n++;
			}
			//cout<<i-1<<endl;
			swap(s,0,c);
			n++;
		}
		out<<n<<endl;
	}
}
int main(){
	openFile();
	mainWork();
	closeFile();
	return 0;
}


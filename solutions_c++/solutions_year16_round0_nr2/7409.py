#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

bool check(string s){
	int l=s.length();
	for(int i=0;i<l;i++){
	 	if(s[i]!='+'){
	 		return false;
	 	}
	 }
	 return true;
}
int index(string str){
	int index;
	int l=str.length();
	index=l-1;
	for(int i=l-1;i>=0;i--){
		if(str[i]=='+'){
			index--;
		}
		else{
		  return index;
		}
	}

}
string flip(string str,int i){
	int l=str.length();
	string flipped;
	string flip=str.substr(0,i+1);
	reverse(flip.begin(),flip.end());
	for(int j=0;j<flip.length();j++){
		if(flip[j]=='+'){
			flip[j]='-';
		}
		else{ flip[j]='+'; }

	}
	flipped=flip+str.substr(i+1,l-(i+1));
	return flipped;

}

int main(){
	string input;
	int t,l,count;
	cin>>t;
	for(int f=1;f<=t;f++){
		count=0;
		cin>>input;
		l=input.length();
		while(true){
			if(count>10){break;}

			if(check(input)){break;}

			if(input[0]=='+'){

				int pp=0;
				for(int i=1;i<input.length();i++){
					if(input[i]=='+'){
						pp++;
					}
					else{ break; }
				}
				input=flip(input,pp);
			}

			else{
				int pp=0;
				for(int i=1;i<input.length();i++){
					if(input[i]=='-'){
						pp++;
					}
					else{break;}
				}
				int zz=index(input);
				input=flip(input,zz);
			}

		 count++;
		}
		cout<<"Case #"<<f<<": "<<count<<endl;

	}

}
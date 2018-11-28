#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

void rep(unsigned char *arr,int len){
	int i;
	unsigned char j;
	if(len==1) return;



	j = arr[len-1];
	for(i=len-2;i>=0;i--){
		arr[i+1]=arr[i];
	}
	arr[0] = j;
	
}

void solve(unsigned char *arr,int len){
	int i;
	int ind;
	unsigned char t;
	if(len<=1) return;
	//printf("sol: "); for(i=0;i<len;i++) printf("%c",arr[i]); printf("\n");
	t = arr[len-1]; ind = len-1;
	for(i=len-2;i>=0;i--){
		if(arr[i] > t ){
			ind = i;
			t = arr[i];
		}
	}
	//printf("t: %d %c\n",ind,t);
	//for(i=0;i<len;i++) printf("%c",arr[i]); printf("\n");
	rep(arr,ind+1);
	//for(i=0;i<len;i++) printf("%c",arr[i]); printf("\n");

	if(ind>0){
		solve(&(arr[1]),ind);
	}
	/*
	if(ind+1 < len){
		solve(&(arr[ind+1]),len-(ind+1));
	}
	*/
}

int main(int argc, char* argv[]){
	int T,nocase;
	int num,len;
	string str;
	int i,ind,t;
	unsigned char buf[1024];

	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
	std::getline (std::cin,str);

	for (nocase = 1; nocase <= T; ++nocase) {
		std::getline (std::cin,str);
		//printf("%s\n",str.c_str());
		for(i=0;i<str.length();i++) buf[i] = str[i];
		//for(i=0;i<str.length();i++) printf("%c",buf[i]); printf("\n");
		//printf("%s\n",str.c_str());
		/*
		t = str[0]; ind = 0;
		for(i=1;i<str.length();i++){
			if(str[i] > t ){
				ind = i;
				t = str[i];
			}
		}
		cout << ind <<" " << str[ind] << endl;
		*/
		
		//reverse(str.begin(),str.begin()+ind+1);
		//cout<< str << end;
		//printf("%s\n",str.c_str());

		solve(buf,str.length());
		//printf("%s\n",buf);
		printf("Case #%d: ",nocase);
		for(i=0;i<str.length();i++) printf("%c",buf[i]); printf("\n");

		//cout << "Case #" << nocase << ": " << num << endl;
	}

	return 0;
}
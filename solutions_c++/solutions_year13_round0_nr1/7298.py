#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
enum {ZWON,XWON,DRAW,INC};
int testr(char *a,int offset=1) { 
	string s="YYYY";
	for(int i=0;i<4;i++) { 
		if(*a=='T'){
			if(i==0)s[i]=*(a+offset);
			else s[i]=*(a-offset);
			a+=offset;
			continue;
		}
		if(*a=='.'){ 
			return INC;
			
		}
		s[i]=*a;
		a+=offset;
	}
	//cout<<endl<<s<<endl;
	//cout<<endl;
	if(s=="OOOO")
	 return ZWON;
	if(s=="XXXX")
	 return XWON;
	return DRAW;
}

int incvar(int ret,int &x,int &z,int &i) {
		if(ret==XWON)x++;
		if(ret==ZWON)z++;
		if(ret==INC)i++;
}
int ans(char *a) {
	char *s=a;
	char *r=a;
	int i,x,z;
	i=x=z=0;
	for(int k=0;k<4;k++) {
	  incvar(testr(r+k*4),x,z,i);
   	  incvar(testr(a+k,4),x,z,i);  
	}
	incvar(testr(r,5),x,z,i); 
	incvar(testr(r+3,3),x,z,i);
	if(x>0)return XWON;
	if(z>0)return ZWON; 
	if(i>0)return INC;
	return DRAW;
}
void print(char *c) { 
	for(int i=0;i<16;i++) {
		//cout<<c[i]<<" ";
		if(i%4==0) 
		cout<<endl;	
		cout<<c[i]<<" ";
	}
}
int main() { 
	int t; 
	cin>>t; 
	int iter=1;
	while(t--) {
		char tic[16];
		for(int i=0;i<16;i++) 
			cin>>tic[i];
		//print(tic);
		//cout<<endl;cout<<testr(tic,5);
		//continue;
		int ret = ans(tic); 
		cout<<"Case #"<<iter<<": ";
		switch(ret) { 
			case XWON:
				cout<<"X won";
				break;
			case ZWON:
				cout<<"O won";
				break;
			case INC:
				cout<<"Game has not completed";
				break;
			case DRAW:
				cout<<"Draw";
			break;
		}
		if(t!=0)
		cout<<endl;
		iter++;
	}
}

#include<iostream>
#include<cstdio>
using namespace std;
char b[4][4];
int c[90];
bool f;
bool arow(int r){
	c['O']=c['X']=c['T']=c['.']=0;
	c[b[r][0]]++;c[b[r][1]]++;c[b[r][2]]++;c[b[r][3]]++;
	if(c['.'])
	return f=false;
	if((c['O']+c['T'])==4){
		cout<<"O won"<<endl;
		return true;
	}
	else if((c['X']+c['T'])==4){
		cout<<"X won"<<endl;
		return true;
	}
	return false;
}
bool acol(int r){
	c['O']=c['X']=c['T']=c['.']=0;
	c[b[0][r]]++;c[b[1][r]]++;c[b[2][r]]++;c[b[3][r]]++;
	if(c['.'])
	return f=false;
	if((c['O']+c['T'])==4){
		cout<<"O won"<<endl;
		return true;
	}
	else if((c['X']+c['T'])==4){
		cout<<"X won"<<endl;
		return true;
	}
	return false;
}
bool adig1(){
	c['O']=c['X']=c['T']=c['.']=0;
	c[b[0][0]]++;c[b[1][1]]++;c[b[2][2]]++;c[b[3][3]]++;
	if(c['.'])
	return f=false;
	if((c['O']+c['T'])==4){
		cout<<"O won"<<endl;
		return true;
	}
	else if((c['X']+c['T'])==4){
		cout<<"X won"<<endl;
		return true;
	}
	return false;
}
bool adig2(){
	c['O']=c['X']=c['T']=c['.']=0;
	c[b[0][3]]++;c[b[1][2]]++;c[b[2][1]]++;c[b[3][0]]++;
	if(c['.'])
	return f=false;
	if((c['O']+c['T'])==4){
		cout<<"O won"<<endl;
		return true;
	}
	if((c['X']+c['T'])==4){
		cout<<"X won"<<endl;
		return true;
	}
	return false;
}

int main(){
	int t,i,j,cn;
	bool comp;
	cn=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cn++<<": ";
		comp=f=true;
		for(i=0;i<4;i++){
			scanf("%s",b[i]);			
		}
		for(i=0;comp&&(i<4);i++){
			comp=comp&&(!arow(i));
		}
		for(i=0;comp&&(i<4);i++){
			comp=comp&&(!acol(i));
		}
		if(comp&&(!adig1()))
			if(!adig2()){
				if(f)
					cout<<"Draw"<<endl;
				else
					cout<<"Game has not completed"<<endl;
			}
	}
	return 0;
}

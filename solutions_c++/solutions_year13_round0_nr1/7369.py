#include <iostream>
#include <string>
using namespace std;
int main(){
	int n;
	cin>>n;
	int x,o,t;
	bool xwin=false;
	bool owin=false;
	bool completed;
	string tab[4];
	for(int g=0;g<n;g++){
		completed=true;
		xwin=false;
		owin=false;
		cin>>tab[0];
		cin>>tab[1];
		cin>>tab[2];
		cin>>tab[3];

		for(int j=0;j<4;j++){
			
			x=0;o=0;t=0;
			
			for(int i=0;i<4;i++){
				if(tab[j][i]=='X')x++;
				if(tab[j][i]=='O')o++;
				if(tab[j][i]=='T')t++;
				if(tab[j][i]=='.')completed=false;
			}
			if((x==3 && t==1) || x==4)xwin=true;
			if((o==3 && t==1) || o==4)owin=true;


		}
		
		for(int j=0;j<4;j++){
			
			x=0;o=0;t=0;
			
			for(int i=0;i<4;i++){
				if(tab[i][j]=='X')x++;
				if(tab[i][j]=='O')o++;
				if(tab[i][j]=='T')t++;
				if(tab[i][j]=='.')completed=false;
			}
			if((x==3 && t==1) || x==4)xwin=true;
			if((o==3 && t==1) || o==4)owin=true;


		}
		//na skos
		
		x=0;o=0;t=0;
		
		for(int j=0;j<4;j++){
			if(tab[j][j]=='X')x++;
			if(tab[j][j]=='O')o++;
			if(tab[j][j]=='T')t++;
			if(tab[j][j]=='.')completed=false;
		}
		if((x==3 && t==1) || x==4)xwin=true;
		if((o==3 && t==1) || o==4)owin=true;

		//na skos 2
		
		x=0;o=0;t=0;
		
		for(int j=0;j<4;j++){
			if(tab[j][3-j]=='X')x++;
			if(tab[j][3-j]=='O')o++;
			if(tab[j][3-j]=='T')t++;
			if(tab[j][3-j]=='.')completed=false;
		}
		if((x==3 && t==1) || x==4)xwin=true;
		if((o==3 && t==1) || o==4)owin=true;

		
		
		cout<<"Case #"<<g+1<<": ";
		if(xwin && !owin)cout<<"X won"<<endl;
		else
		if(!xwin && owin)cout<<"O won"<<endl;
		else
		if(!xwin && !owin && completed)cout<<"Draw"<<endl;
		else 
		if(!completed)cout<<"Game has not completed"<<endl;
	}
	return 0;
}

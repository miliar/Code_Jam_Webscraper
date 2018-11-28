#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

char gam[4][4]={'\0'};

void checkStatus(int caseNum){
	
	int c_x=0;
	int c_o=0;
	int c_t=0;
	int c_dot=0;
	
	//check for principal diagonal
	for(int i=0,j=0;i<4&&j<4;i++,j++){
		if(gam[i][j]=='X')
			c_x++;
		if(gam[i][j]=='O')
			c_o++;
		if(gam[i][j]=='T'){
			c_o++;
			c_x++;
		}
	}
	
	if(c_x==4){
		cout<<"Case #"<<caseNum<<": X won"<<endl;
		return;
	}
	
	if(c_o==4){
		cout<<"Case #"<<caseNum<<": O won"<<endl;
		return;
	}		
	
	//check the other diagonal
	
	c_x=0;
	c_o=0;
	c_t=0;
	
	for(int i=0,j=3;i<4&&j>=0;i++,j--){
		if(gam[i][j]=='X')
			c_x++;
		if(gam[i][j]=='O')
			c_o++;
		if(gam[i][j]=='T'){
			c_o++;
			c_x++;
		}
	}
	
	if(c_x==4){
		cout<<"Case #"<<caseNum<<": X won"<<endl;
		return;
	}
	
	if(c_o==4){
		cout<<"Case #"<<caseNum<<": O won"<<endl;
		return;
	}
	
	//check the rows
	c_x=0;
	c_o=0;
	c_t=0;
	
	for(int i=0;i<4;i++){
		c_x=0;
		c_o=0;
		c_t=0;

		for(int j=0;j<4;j++){
			if(gam[i][j]=='X')
				c_x++;
			if(gam[i][j]=='O')
				c_o++;
			if(gam[i][j]=='T'){
				c_o++;
				c_x++;
			}
			if(gam[i][j]=='.')
				c_dot++;
		}
		if(c_o==4||c_x==4)
			break;
	}
	
	if(c_x==4){
		cout<<"Case #"<<caseNum<<": X won"<<endl;
		return;
	}
	
	if(c_o==4){
		cout<<"Case #"<<caseNum<<": O won"<<endl;
		return;
	}
	
	//check for the cols
	c_x=0;
	c_o=0;
	c_t=0;
	c_dot=0;
	
	for(int i=0;i<4;i++){
		c_x=0;
		c_o=0;
		c_t=0;

		for(int j=0;j<4;j++){
			if(gam[j][i]=='X')
				c_x++;
			if(gam[j][i]=='O')
				c_o++;
			if(gam[j][i]=='T'){
				c_o++;
				c_x++;
			}
			if(gam[i][j]=='.')
				c_dot++;
		}
		if(c_o==4||c_x==4)
			break;
	}
	
	if(c_x==4){
		cout<<"Case #"<<caseNum<<": X won"<<endl;
		return;
	}
	
	if(c_o==4){
		cout<<"Case #"<<caseNum<<": O won"<<endl;
		return;
	}
	
	if(c_dot==0){
		cout<<"Case #"<<caseNum<<": Draw"<<endl;
		return;
	}
				
	cout<<"Case #"<<caseNum<<": Game has not completed"<<endl;
}

int main(){
	int tc;
	cin>>tc;
 	for(int count=1;count<=tc*5;count++){
 		
 		if(count%5==0){
 			checkStatus(count/5);
 			continue;
 		}
 		fscanf(stdin,"%s",gam[count%5-1]);
 	}

 	return 0;
}

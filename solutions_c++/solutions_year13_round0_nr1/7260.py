#include<iostream>
#include<string>
using namespace std;
int main(){
    int t;
    cin >>t;
    for(int m=0;m<t;m++){
	string tic1,tic2,tic3,tic4;
	cin >>tic1;
	cin>>tic2;
	cin>>tic3;
	cin>>tic4;
	string col1,col2,col3,col4;
	col1="";
	col2="";
	col3="";
	col4="";
	col1 += tic1[0]; 
	col1 += tic2[0]; 
	col1 += tic3[0]; 
	col1 +=tic4[0];	
	col2+= tic1[1]; 
	col2+= tic2[1]; 
	col2+= tic3[1]; 
	col2 +=tic4[1];	
	col3+= tic1[2]; 
	col3+= tic2[2]; 
	col3+= tic3[2]; 
	col3 +=tic4[2];	
	col4+= tic1[3]; 
	col4+= tic2[3]; 
	col4+= tic3[3]; 
	col4 +=tic4[3];	
	int st,st2;
    	st =0;
    	st2=0;
	string d1, d2;
	d1+= tic1[0]; 
	d1+= tic2[1]; 
	d1+= tic3[2]; 
	d1+= tic4[3];
	d2+= tic1[3]; 
	d2+= tic2[2]; 
	d2+= tic3[1]; 
	d2+= tic4[0];
	bool comp= true;
	int x=0;
	int y =0;	
	for (int i=0;i<4;i++) if (tic1[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=tic1.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (tic2[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=tic2.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (tic3[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=tic3.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (tic4[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=tic4.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (col1[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=col1.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (col2[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=col2.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (col3[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=col3.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (col4[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=col4.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (tic1[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=tic1.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (tic2[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=tic2.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (tic3[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=tic3.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (tic4[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=tic4.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (col1[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=col1.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (col2[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=col2.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (col3[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=col3.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (col4[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=col4.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (d1[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=d1.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (d2[i]=='X') x++; if (x==4 || (x==3 && std::string::npos !=d2.find("T"))){ st =1;goto statusx;}x=0;
	for (int i=0;i<4;i++) if (d1[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=d1.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if (d2[i]=='O') y++; if (y==4 || (y==3 && std::string::npos !=d2.find("T"))){ st2 =1;goto statusx;}y=0;
	for (int i=0;i<4;i++) if(tic1[i]=='.'||tic2[i]=='.'||tic3[i]=='.'||tic4[i]=='.'){comp = false ;break;}
	if (comp == false){cout <<"Case #"<<(m+1)<<": Game has not completed"<<"\n";continue;}	
	statusx :
		if (st==1) cout <<"Case #"<<(m+1)<<": X won"<<"\n";
		else if (st2==1) cout <<"Case #"<<(m+1)<<": O won"<<"\n";
		else cout <<"Case #"<<(m+1)<<": Draw"<<"\n";
	}
	return 0;
	}

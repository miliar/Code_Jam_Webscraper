#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

string str(5,'-');
vector<string> v(5,str);


bool checkstring(int i,int x,int y,int dx,int dy,char c,bool t_done){
	if(x>0 && x<5 && y>0 && y<5){
		if((v[x][y]== c) || (v[x][y] == 'T' && !t_done)){
			if(v[x][y]=='T')
				t_done = true;
			if(i==4)
				return true;
			else{
				x += dx;	y += dy;	i++;
				checkstring(i,x,y,dx,dy,c,t_done);
			}
		}else
			return false;
	}else
		return false;
}

int main(){
	int i,j,ncses,c_n=1,l,k;
	bool O_win,X_win,complete;

	cin>>ncses;

	while(ncses-->0){
		O_win=false;	X_win=false; complete=true;
			for(i=1;i<=4;i++)
				for(j=1;j<=4;j++)
					cin>>v[i][j];
			for(i=1;i<=4;i++)
				for(j=1;j<=4;j++){
					if(v[i][j]=='.')
						complete=false;
					if(v[i][j]=='X'){
						for(l=-1;l<=1;l++)
							for(k=-1;k<=1;k++){
								if(!(l==0&&k==0))
									if(checkstring(1,i,j,l,k,'X',false))
										X_win=true;
							}
					}
					if(v[i][j]=='O'){
						for(l=-1;l<=1;l++)
							for(k=-1;k<=1;k++){
								if(!(l==0&&k==0))
									if(checkstring(1,i,j,l,k,'O',false))
										O_win=true;
							}
					}
				}
			cout<<"Case #"<<c_n<<": ";
			if(complete && !X_win && !O_win)
				cout<<"Draw"<<endl;
			else if(O_win && !X_win)
				cout<<"O won"<<endl;
			else if(!O_win && X_win)
				cout<<"X won"<<endl;
			else if(!O_win && !X_win && !complete)
				cout<<"Game has not completed"<<endl;
			c_n++;	
	}
	return 0;
}


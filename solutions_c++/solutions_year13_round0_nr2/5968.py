#include<iostream>
using namespace std;

void takeinput();
bool possible(int);
bool possible_help(int,int,int,int);

int t;
int nm_array[100][2];
int input[100][10][10]={0,0,0};

int main()
{
takeinput();
	for(int i=0;i<t;i++){
		if(possible(i)){
			cout<<"Case #" <<i+1 <<": YES" <<endl;
		}
		else cout<<"Case #" <<i+1 <<": NO" <<endl;
	}
return 0;
}

bool possible_help(int cas,int no,int i,int j)
{
int cancel=0;
int cancel_final=0;
	for(int x=0;x<nm_array[cas][0];x++){
		if( !(input[cas][i][x]<=no) )
			cancel=1;	
	}
	for(int y=0;y<nm_array[cas][1];y++){
		if( !(input[cas][y][j]<=no) )
			cancel_final=1;
	}
	if(cancel==1 && cancel_final==1){	
		return false;
	}
return true;
}

bool possible(int cas)
{
int n;
	if(nm_array[cas][0]==1 || nm_array[cas][1]==1)
		return true;

	for(int i=0;i<nm_array[cas][0];i++){
		for(int j=0;j<nm_array[cas][1];j++){
			n=input[cas][i][j];			
			if(!possible_help(cas,n,i,j))
				return false;
		}
	}
return true;
}

void takeinput()
{
cin>>t;
	for(int i=0;i<t;i++){
	cin>>nm_array[i][0];
	cin>>nm_array[i][1];
		for(int j=0;j<nm_array[i][0];j++){
			for(int k=0;k<nm_array[i][1];k++){
				cin>>input[i][j][k];
			}
		}
	}
}

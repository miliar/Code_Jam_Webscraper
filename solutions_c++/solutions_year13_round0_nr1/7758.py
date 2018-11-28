#include "iostream"
#include "stdio.h"

using namespace std;
/*
char X[4][4]={{'X','X','X','X'},{'X','X','X','X'},{'X','X','X','X'},{'X','X','X','X'}};
char O[4][4]={{'O','O','O','O'},{'O','O','O','O'},{'O','O','O','O'},{'O','O','O','O'}};
*/
int comp(char A[4][4])
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(A[i][j]=='.')
				return 0;
	return 1;
}

main()
{
	int flag=0;
	int t=0;
	cin>>t;
	char A[4][4];
	for(int k=1;k<=t;k++){
            for(int i=0;i<4;)
		for(int j=0;j<4;)
		{   char ch=getchar();
		    if(ch=='X'||ch=='O'||ch=='.'||ch=='T')
		    { //cout<<"\nIn"<<ch<<i<<" "<<j; 
		      A[i][j]=ch;
		      j++;
		      if(j==4)
			 i++;
		  
		    }
		}
	int xwin1='X'+'X'+'X'+'T';
	int xwin2='X'+'X'+'X'+'X';
	int ywin1='O'+'O'+'O'+'T';
	int ywin2='O'+'O'+'O'+'O';
	int W[10]={0,0,0,0,0,0,0,0,0,0};
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			W[i]+=A[i][j];
			W[j+4]+=A[i][j];
			if(i==j)
				W[8]+=A[i][j];
			if(i+j==3)
				W[9]+=A[i][j];
		}
	}
	flag=3;
	for(int i=0;i<10;i++){
		if(W[i]==xwin1 || W[i]==xwin2)
			flag=1;
		else if(W[i]==ywin1 || W[i]==ywin2)
			flag=2;

	}
	cout<<"\nCase #"<<k<<": ";	
	if(flag==1)
		cout<<"X won";
	else if(flag==2)
		cout<<"O won";
	else {
		if(comp(A)==0)
		cout<<"Game has not completed";
		else
			cout<<"Draw";
	}
	}
}

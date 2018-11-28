#include<iostream>
#include<string.h>
#include<stdio.h>
#include<fstream>
using namespace std;

int main()
{
	int t;
	ifstream in;
	in.open("input.txt");
	in>>t;
	//scanf("%d",&t);
	string s;;
	getline(in,s);
	string str[4];
	int countX[t],countO[t],countT[t],countdot[t],flagX,flagO,countdx[t],countdo[t],countdt[t];
	string st[t];
	for(int i=0;i<t;i++)
	{
		countdot[i]=0,countdx[i]=0,countdo[i]=0,countdt[i]=0;
		flagX=0,flagO=0;
		getline(in,str[0]);
		//getline(cin,str[0]);
		//cout<<str[0]<<"\n";
		getline(in,str[1]);
		//getline(cin,str[1]);
		//cout<<str[1]<<"\n";
		getline(in,str[2]);
		//getline(cin,str[2]);
		//cout<<str[2]<<"\n";
		getline(in,str[3]);
		//getline(cin,str[3]);
		//cout<<str[3]<<"\n";
		for(int j=0;j<4;j++)
		{
		  countX[i]=0,countO[i]=0,countT[i]=0;
		  for(int k=0;k<4;k++)
		  {
		  	if(str[j][k]=='X')
		  	countX[i]++;
		  	else if(str[j][k]=='O')
		  	countO[i]++;
		  	else if(str[j][k]=='T')
		  	countT[i]++;
		  	else
		  	countdot[i]++;
		  }
		  
		  if(countX[i]==4 || (countX[i]==3 && countT[i]==1))
		  flagX=1;
		  if(countO[i]==4 || (countO[i]==3 && countT[i]==1))
		  flagO=1;
		  
		  countX[i]=0,countO[i]=0,countT[i]=0;
		  for(int m=0;m<4;m++)
		  {
		  	if(str[m][j]=='X')
		  	countX[i]++;
		  	else if(str[m][j]=='O')
		  	countO[i]++;
		  	else if(str[m][j]=='T')
		  	countT[i]++;
		  	else
		  	countdot[i]++;
		  }
		  if(countX[i]==4 || (countX[i]==3 && countT[i]==1))
		  flagX=1;
		  if(countO[i]==4 || (countO[i]==3 && countT[i]==1))
		  flagO=1;
	    }
	    for(int j=0;j<4;j++)
	    {
	    	if(str[j][j]=='X')
	    	countdx[i]++;
	    	else if(str[j][j]=='O')
	    	countdo[i]++;
	    	else if(str[j][j]=='T')
	    	countdt[i]++;
	    }
	    if(countdx[i]== 4 ||(countdx[i]==3 && countdt[i]==1))
	    flagX=1;
	    if(countdo[i]== 4 ||(countdo[i]==3 && countdt[i]==1))
	    flagO=1;
	    
	    countdx[i]=0,countdo[i]=0,countdt[i]=0;
	    for(int j=3;j>=0;j--)
	    {
	    	if(str[3-j][j]=='X')
	    	countdx[i]++;
	    	else if(str[3-j][j]=='O')
	    	countdo[i]++;
	    	else if(str[3-j][j]=='T')
	    	countdt[i]++;
	    }
	    
	    if(countdx[i]== 4 ||(countdx[i]==3 && countdt[i]==1))
	    flagX=1;
	    if(countdo[i]== 4 ||(countdo[i]==3 && countdt[i]==1))
	    flagO=1;
	    
	    //cout<<flagX<<" "<<flagO<<"\n";
	    if(flagX==1 && flagO==0)
	    st[i]="X won";
	    else if(flagO==1 && flagX==0)
	    st[i]="O won";
	    else if(flagX==1 && flagO==1)
	    st[i]="X won";
	    else if(countdot[i]==0 && flagX==0 && flagO==0)
	    st[i]="Draw";
	    else if(countdot[i]>0  && flagX==0 && flagO==0 )
	    st[i]="Game has not completed";
	    getline(in,s);
	    //gets(s);
	}
	in.close();
	ofstream out;
	out.open("output.txt");
	for(int i=0;i<t;i++)
	{
		out<<"Case #"<<i+1<<": "<<st[i]<<"\n";
		//cout<<"Case #"<<i+1<<": "<<st[i]<<"\n";
	}
	
	out.close();
	return 0;
}

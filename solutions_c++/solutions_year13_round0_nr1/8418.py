#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

bool cond1(char input[][4])
{
	for(int i=0;i<4;i++)
	{
		int countr=0;
		int countc=0;
		int counttr=0;
		int counttc=0;
		for(int j=0;j<4;j++)
		{
			if(input[i][j]=='X')
			countr++;
			if(input[i][j]=='T')
			counttr++;
			if(input[j][i]=='X')
			countc++;
			if(input[j][i]=='T')
			counttc++;
			
		}
		if(countr==4)
		return true;
		else if((countr==3)&&(counttr==1))
		return true;
		else if(countc==4)
		return true;
		else if((countc==3)&&(counttc==1))
		return true;
		
		
	}
	///////////////
		int count=0;
		int countt=0;
		for(int i=0;i<4;i++)
		{
			
			
			if(input[i][i]=='X')
			count++;
			if(input[i][i]=='T')
			countt++;
			
		}
		if(count==4)
		return true;
		else if((count==3)&&(countt==1))
		return true;
		////////////////
		 count=0;
		 countt=0;
		for(int i=0;i<4;i++)
		{
			
			
			if(input[i][4-i-1]=='X')
			count++;
			if(input[i][4-i-1]=='T')
			countt++;
			
		}
		if(count==4)
		return true;
		else if((count==3)&&(countt==1))
		return true;
		////////////
		
		
	
		
	
		return false;
}

///////////////cond2//////////////
bool cond2(char input[][4])
{
	for(int i=0;i<4;i++)
	{
		int countr=0;
		int countc=0;
		int counttr=0;
		int counttc=0;
		for(int j=0;j<4;j++)
		{
			if(input[i][j]=='O')
			countr++;
			if(input[i][j]=='T')
			counttr++;
			if(input[j][i]=='O')
			countc++;
			if(input[j][i]=='T')
			counttc++;
			
		}
		if(countr==4)
		return true;
		else if((countr==3)&&(counttr==1))
		return true;
		else if(countc==4)
		return true;
		else if((countc==3)&&(counttc==1))
		return true;
		
		
	}
	///////////////
		int count=0;
		int countt=0;
		for(int i=0;i<4;i++)
		{
			
			
			if(input[i][i]=='O')
			count++;
			if(input[i][i]=='T')
			countt++;
			
		}
		if(count==4)
		return true;
		else if((count==3)&&(countt==1))
		return true;
		////////////////
		 count=0;
		 countt=0;
		for(int i=0;i<4;i++)
		{
			
			
			if(input[i][4-i-1]=='O')
			count++;
			if(input[i][4-i-1]=='T')
			countt++;
			
		}
		if(count==4)
		return true;
		else if((count==3)&&(countt==1))
		return true;
		////////////
		
		
	
		
	
		return false;
}
////////////////cond2///////

////////for . //////
bool isdot(char input[][4])
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(input[i][j]=='.')
			return true;
			break;
		}
	}
	return false;
}
/////////////////////////
int main()
{
	//freopen("C.in","r",stdin);
	//freopen("outputC.in","w",stdout);
	int t;
	cin>>t;
	int test=1;
	while(t--)
	{
		
		char input[4][4];
		for(int i=0;i<4;i++)
		{for(int j=0;j<4;j++)
		cin>>input[i][j];
		}
		
		if(cond1(input))
		cout<<"Case #"<<test<<": X won"<<endl;
		
		else if(cond2(input))
		cout<<"Case #"<<test<<": O won"<<endl;
		
		else if(((!cond1(input))&&(!cond2(input)))&&(isdot(input)))
		cout<<"Case #"<<test<<": Game has not completed"<<endl;
		else if((!cond1(input))&&(!cond2(input)))
		cout<<"Case #"<<test<<": Draw"<<endl;
		test++;
	}
	
	return 0;
}

#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

char ch[4][4];

bool win(char c)
{
	int i,j,cnt,x,y,t;
	
	for(i=0;i<4;i++)
	{
		t=0;
		cnt=0;
		for(j=0;j<4;j++)
			if(ch[i][j]==c)
				cnt++;
			else if(ch[i][j]=='T')
				t=1;
		
		if(cnt==4 || (cnt==3 && t))
			return true;		
	}
	
	for(j=0;j<4;j++)
	{
		t=0;
		cnt=0;
		for(i=0;i<4;i++)
			if(ch[i][j]==c)
				cnt++;
			else if(ch[i][j]=='T')
				t=1;
		
		if(cnt==4 || (cnt==3 && t))
			return true;		
	}
	
	t=cnt=0;
	
	for(i=0,j=0;i<4 & j<4;i++,j++)
		if(ch[i][j]==c)
			cnt++;
		else if(ch[i][j]=='T')
			t=1;
	
	if(cnt==4 || (cnt==3 && t))
		return true;
		
	
	t=cnt=0;
	
	for(i=0,j=3;j>=0;i++,j--)
		if(ch[i][j]==c)
			cnt++;
		else if(ch[i][j]=='T')
			t=1;
	
	if(cnt==4 || (cnt==3 && t))
		return true;
	
	return false;	
}

int main()
{
	int i,j,t,x,y;	
	
	cin>>t;
	
	for(int tt=1;tt<=t;tt++)
	{
		for(i=0;i<4;i++)
			cin>>ch[i];
		
		
		cout<<"Case #"<<tt<<": ";
		
		if(win('X'))
			cout<<"X won";
		else if(win('O'))
			cout<<"O won";
		else
		{
			for(i=0;i<4;i++)
			{				
				for(j=0;j<4;j++)
					if(ch[i][j]=='.')
						break;
				if(j!=4)
					break;
			}
			
			if(i==4)
				cout<<"Draw";
			else
				cout<<"Game has not completed";			
		}
		
		cout<<endl;	
	}
	
	return 0;
}
//Nakul Krishna
//Computer Science Engineering
//Amrita Vishwa Vidyapeetham

#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>

#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

#define pb push_back
#define mp make_pair

using namespace std;

unsigned long long mod=1000000007;

int main()
{
	int t=1,tc;
	scanf("%d",&tc);
	while(t<=tc)
	{
		string str;
		int f=0,chk=0;
		vector<string> v;
		for(int i=0;i<4;i++)
			cin>>str,v.pb(str);
			
		/*for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				cout<<v[i][j]<<" ";
			cout<<"\n";
		}*/
			
		for(int i=0;i<4;i++)
		{
			int x=0,o=0,tt=0,TT=0;
			for(int j=0;j<4;j++)
			{
				if(v[i][j]=='X' or v[i][j]=='T')
				{
					if(v[i][j]=='T')
						tt++;
					else
						x++;
				}
				if(v[i][j]=='O' or v[i][j]=='T')
				{
					if(v[i][j]=='T')
						TT++;
					else
						o++;
				}
				if(v[i][j]=='.')
					f=1;
			}
			if(o==4 or (o==3 and TT==1))
			{
				chk=1;
				break;
			}
			else if(x==4 or (x==3 and tt==1))
			{
				chk=2;
				break;
			}
		}
		for(int i=0;i<4;i++)
		{
			int x=0,o=0,tt=0,TT=0;
			for(int j=0;j<4;j++)
			{
				if(v[j][i]=='X' or v[j][i]=='T')
				{
					if(v[j][i]=='T')
						tt++;
					else
						x++;
				}
				if(v[j][i]=='O' or v[j][i]=='T')
				{
					if(v[j][i]=='T')
						TT++;
					else
						o++;
				}
				if(v[j][i]=='.')
					f=1;
			}
			if(o==4 or (o==3 and TT==1))
			{
				chk=1;
				break;
			}
			else if(x==4 or (x==3 and tt==1))
			{
				chk=2;
				break;
			}
		}
		
		int x=0,o=0,tt=0,TT=0;
		for(int j=0;j<4;j++)
		{
			if(v[j][j]=='X' or v[j][j]=='T')
			{
				if(v[j][j]=='T')
					tt++;
				else
					x++;
			}
			if(v[j][j]=='O' or v[j][j]=='T')
			{
				if(v[j][j]=='T')
					TT++;
					
				else
					o++;
			}
			if(v[j][j]=='.')
				f=1;
		}
		if(o==4 or (o==3 and TT==1))
		{
			chk=1;
			//break;
		}
		else if(x==4 or (x==3 and tt==1))
		{
			chk=2;
			//break;
		}
		
		x=0,o=0,tt=0,TT=0;
		for(int j=0;j<4;j++)
		{
			if(v[j][abs(j-3)]=='X' or v[j][abs(j-3)]=='T')
			{
				if(v[j][abs(j-3)]=='T')
					tt++;
				else
					x++;
			}
			if(v[j][abs(j-3)]=='O' or v[j][abs(j-3)]=='T')
			{
				if(v[j][abs(j-3)]=='T')
					TT++;//cout<<"nak";
				else
					o++;
			}
			if(v[j][abs(j-3)]=='.')
				f=1;
			//cout<<j<<" "<<abs(j-3)<<"    "<<o<<" "<<TT<<" "<<f<<"\n";;
			//cout<<(v[j][abs(j-3)]=='T')<<"\n";
		}
		//cout<<o<<" "<<TT<<"\n";
		if(o==4 or (o==3 and TT==1))
		{
			chk=1;
			//break;
		}
		else if(x==4 or (x==3 and tt==1))
		{
			chk=2;
			//break;
		}
		
		if(chk==1)
			printf("Case #%d: O won\n",t);
		else if(chk==2)
			printf("Case #%d: X won\n",t);
		else if(f==1)
			printf("Case #%d: Game has not completed\n",t);
		else
			printf("Case #%d: Draw\n",t);
		t++;
	}
    scanf("\n");
    return 0;
}

//Nakul © Copyright 2012 - All Rights Reserved


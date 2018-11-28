#include<stdio.h>
#include<iostream>
#include<string.h>
#include<sstream>
#include<vector>
using namespace std;
int convert(char a)
{
	if(a=='i')
		return 2;
	else if(a=='j')
		return 3;
	else if(a=='k')
		return 4;
	else
		return 1;	
}
int convertpositive(int a)
{
	if(a==-1)
		return 5;
	else if(a==-2)
		return 6;
	else if(a==-3)
		return 7;
	else if(a==-4)
		return 8;
}
int main()
{
	freopen("C-small-attempt7 (1).in","rt",stdin);
	freopen("try.out","wt",stdout);
	int quart[8][8]= {{ 1,2,3,4,-1,-2,-3,-4},
			  { 2,-1,4,-3,-2,1,-4,3},
			  { 3,-4,-1,2,-3,4,1,-2},
			  { 4,3,-2,-1,-4,-3,2,1},
			  { -1,-2,-3,-4,1,2,3,4},
			  { -2,1,-4,3,2,-1,4,-3},
			  { -3,4,1,-2,3,-4,-1,2},
			  { -4,-3,2,1,4,3,-2,-1}};
	int n,i,len,cnt=0,times,l,j,num,p,q=0,tmp3,tmp1,tmp2,s,flagi=0,flagj=0,flagk=0;
	string inp;
	char in[25535],cha,ch; 
	int ary[25535];
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		flagi=0;flagj=0;flagk=0;q=0;cnt=0;num=0;len=0;times=0;
		cha='0';ch='0';
		scanf("%d",&len);
		scanf("%d",&times);
		/*getline(cin, inp);
		while (cha != '\n' ) {
		    cha = fgetc(stdin);
		    in[cnt] = cha;
    			cnt++;
		}*/
		scanf (" %[^\n]s",in);
		//strncpy(in,inp.c_str(),len);	
		s=0;
		for(l=0;l<times;l++)
		{
			for(p=0;p<len;p++)
			{
				ch=in[p];
				num=convert(ch);
				ary[s]=num;
				s++;
			}
		}
		//cout<<endl<<":"<<ary[9832]<<endl;
		tmp1=ary[0];
		if(tmp1==2)
		{
			flagi=1;
			goto jsolve;
			
		}
		for(q=1;q<s;q++)
		{
			tmp2=ary[q];
			tmp3=quart[tmp1-1][tmp2-1];
			if(tmp3==2)
			{
				flagi=1;
				//cout<<" :: "<<q;
				goto jsolve;
			}	
			else
				tmp1=tmp3;
			if(tmp1<0)
				tmp1=convertpositive(tmp1);
		}
		jsolve:
		q=q+1;
		if(q<s)
		{
			tmp1=ary[q];
			if(tmp1==3)
			{
				flagj=1;
				//cout<<" :: "<<q;
				goto ksolve;
			}
			for(q=q+1;q<s;q++)
		{
			tmp2=ary[q];
			tmp3=quart[tmp1-1][tmp2-1];
			if(tmp3==3)
			{
				flagj=1;
				//cout<<" :: "<<q;
				goto ksolve;
			}
			else
				tmp1=tmp3;
			if(tmp1<0)
				tmp1=convertpositive(tmp1);
		}
		}
		ksolve:
		q=q+1;
		if(q<s)
		{
			tmp1=ary[q];
			for(q=q+1;q<s;q++)
		{
			tmp2=ary[q];
			tmp3=quart[tmp1-1][tmp2-1];
			tmp1=tmp3;
			if(tmp1<0)
				tmp1=convertpositive(tmp1);
		}
		if(tmp1==4)
		{
			flagk=1;
			//cout<<" :: "<<q;
			goto END;
		}
		}
		END:
		if(flagi==1 && flagj==1 && flagk==1 )
			printf("Case #%d: YES\n",i+1);
		else
			printf("Case #%d: NO\n",i+1);
		
	}
}

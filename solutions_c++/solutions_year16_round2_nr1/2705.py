#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int t,i,x;
	freopen("ccjam.txt","w",stdout);
	freopen("ccjamq.txt","r",stdin);
	cin>>t;
	int mark[100],ans,val,ar[100];
	for(x=1;x<=t;x++)
	{
		for(i=0;i<100;i++)
		{
			mark[i]=0;
			ar[i]=0;
		}
		char c[4000];
		scanf("%s",&c);
		for(i=0;c[i]!='\0';i++)
		{
			mark[c[i]]++;
		}
//		ar[0]=min(mark['O'],min(mark['Z'],min(mark['E'],mark['R'])));
//		ar[1]=min(mark['O'],min(mark['N'],mark['E']));
//		ar[2]=min(mark['T'],min(mark['W'],mark['O']));
//			ar[3]=min(mark['T'],min(mark['H'],min(mark['R'],mark['E']/2)));
//			ar[4]==min(mark['F'],min(mark['O'],min(mark['U'],mark['R'])));
//				ar[5]==min(mark['F'],min(mark['I'],min(mark['V'],mark['E'])));
//				ar[6]=min(mark['S'],min(mark['I'],mark['X']));
////					ar[4]==min(mark['F'],min(mark['O'],min(mark['U'],mark['R'])));
//			ar[7]=min(mark['S'],min(mark['V'],min(mark['N'],mark['E']/2)));
//			ar[8]=min(mark['T'],min(mark['H'],min(mark['I'],min(mark['E'],mark['G']))));
//		    ar[9]=min(mark['I'],min(mark['N'],mark['E']/2));
//		    
//		recs(0);
   ans=0;
		val=mark['Z'];
		ar[0]=val;
		ans+=val;
		mark['O']-=val;
		mark['Z']-=val;mark['E']-=val;mark['R']-=val;
		val=mark['G'];
		ans+=val;
				ar[8]=val;
		mark['E']-=val;
		mark['I']-=val;
		mark['G']-=val;
		mark['H']-=val;
		mark['T']-=val;
		val=mark['X'];
				ar[6]=val;
		ans+=val;
		mark['S']-=val;
		mark['I']-=val;
		mark['X']-=val;
		val=min(mark['S'],mark['V']);
		ans+=val;
				ar[7]=val;
		mark['S']-=val;
		mark['E']-=val;
		mark['V']-=val;
			mark['E']-=val;
				mark['N']-=val;
				val=mark['V'];
		ans+=val;
				ar[5]=val;
		mark['F']-=val;
		mark['I']-=val;
		mark['V']-=val;
		mark['E']-=val;
		val=mark['F'];
		ans+=val;
				ar[4]=val;
		mark['F']-=val;
		mark['O']-=val;
		mark['U']-=val;
		mark['R']-=val;
		val=mark['I'];
		ans+=val;
				ar[9]=val;
		mark['N']-=val;
		mark['I']-=val;
		mark['N']-=val;
		mark['E']-=val;
		val=mark['H'];
		ans+=val;
				ar[3]=val;
		mark['T']-=val;
		mark['H']-=val;
		mark['R']-=val;
		mark['E']-=val;
		mark['E']-=val;
		val=mark['T'];
		ans+=val;
				ar[2]=val;
		mark['T']-=val;
		mark['W']-=val;
		mark['O']-=val;
//		mark['R']-=val;
	val=mark['O'];
		ans+=val;
				ar[1]=val;
		mark['E']-=val;
		mark['N']-=val;
		mark['O']-=val;
        int j;
		cout<<"Case #"<<x<<": ";		
		for(i=0;i<10;i++)
		{
			for(j=0;j<ar[i];j++)
			{
				cout<<i;
			}
		}
		cout<<endl;
		
	}
	
}
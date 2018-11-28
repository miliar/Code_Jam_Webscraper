#include<stdio.h>
#include<fstream>
using namespace std;
int store[4][4][4]={{ {2,1,1,1},{2,2,1,1},{2,1,1,1},{2,2,1,1} },{{2,2,1,1},{2,2,1,1},{2,2,2,1},{2,2,1,1}},{{2,1,1,1},{2,2,2,1},{2,1,2,1},{2,2,2,2}},
	{{2,2,1,1},{2,2,1,1},{2,2,2,2},{2,2,1,2}}};
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("D-small-attempt0.in");
	fout.open("resd.in");
	int t,tno,x,r,c,res,val;
	//scanf("%d",&t);
	fin>>t;
	for(tno=1;tno<=t;tno++)
	{
		//scanf("%d",&x);
		//scanf("%d",&r);
		//scanf("%d",&c);
		fin>>x;
		fin>>r;
		fin>>c;
		if(x<=4 && r<=4 && c<=4)
		{
			res=store[r-1][c-1][x-1];
			if(res==1)
			fout<<"Case #"<<tno<<": RICHARD\n";
			else
			fout<<"Case #"<<tno<<": GABRIEL\n";
		}
		else
		{
		val=r*c-x;
		if(val%x!=0)
		res=1;
		else
		{
		
			if(x>r && x>c)
			res=1;
			else if(x<=r && x<=c)
			res=2;
			else
			{
				if(x>r && x<c)
				{
					val=r+1;
					val=val<1;
					val--;
				}
				else if(x<r && x>c)
				{
					val=c+1;
					val=val<1;
					val--;		
				}
				if(x>=val)
				res=1;
				else
				{
					if(r<c)
					{
						val=r<1;
					    if(x>=val)	
					    res=1;
					    else
					    res=2;
					}
					if(r>c)
					{
						val=c<1;
					    if(x>=val)	
					    res=1;
					    else
					    res=2;
					}
					if(r==c)
					{
						val=(c-1)<1;
						if(x>=val)
						res=1;
						else
						res=2;
					}
				}
			}
		}
			if(res==1)
			fout<<"Case #"<<tno<<": RICHARD\n";
			else
			fout<<"Case #"<<tno<<": GABRIEL\n";
	    }
	}
}


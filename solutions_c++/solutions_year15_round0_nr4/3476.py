#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
	int t;	
	fstream fin("D-small-attempt2.in",ios::in);
	fstream fout("output.txt",ios::out);
	fin>>t;
	for(int i=0;i<t;i++)
	{
		int x,r,c;
		fin>>x>>r>>c;
		if(x>=6)
			fout<<"Case #"<<i+1<<": RICHARD"<<endl;
		else if((r*c)%x != 0)
			fout<<"Case #"<<i+1<<": RICHARD"<<endl;
		else if(x==2 || x==1)
			fout<<"Case #"<<i+1<<": GABRIEL"<<endl;
		else if(x==3 && r*c==3)
			fout<<"Case #"<<i+1<<": RICHARD"<<endl;
		else if(x==3 && r*c!=3)
			fout<<"Case #"<<i+1<<": GABRIEL"<<endl;
		else if(x==4 && (r*c==4 || r*c==8))
			fout<<"Case #"<<i+1<<": RICHARD"<<endl;
		else if(x==4 && (r*c!=4 && r*c!=8))
			fout<<"Case #"<<i+1<<": GABRIEL"<<endl;
			
}
}
			

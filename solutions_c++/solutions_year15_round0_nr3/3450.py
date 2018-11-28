#include <iostream>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
 int negative=1;
 bool i=false,j=false,k=false;
 void splitItI(string kij);
 void splitItJ(string kij);
 void splitItK(string kij);
 char mul(char x,char y);

 string operator*(const string& s, unsigned int n) {
    stringstream out;
    while (n--)
        out << s;
    return out.str();
}

string operator*(unsigned int n, const string& s) { return s * n; }


int main() {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
		int casesNum,count=0;
		cin>>casesNum;
		while(casesNum!=0)
		{
			int t1,t2;	
			string rep;	
			cin>>t1>>t2;
			cin>>rep;
			negative=1;
			i=false;j=false;k=false;
			rep=rep*(t2);
            //cout<<rep<<endl;
			splitItI(rep);
			count++;
			if( i && j && k && negative==1)
				 cout<<"Case #"<<count<<": "<<"YES"<<endl;
			else
				 cout<<"Case #"<<count<<": "<<"NO"<<endl;

	    
			casesNum--;
		}
}
void splitItI(string kij)
{
		char m='1';
		for(int x=0;x<kij.size();x++)
			{
				m=mul(m,kij[x]);	
				
				if(m=='i' && i==false)
				{
					i=true;
					if(x!=kij.size()-1)
					{

						//cout<<negative<<endl;
						splitItJ(kij.substr(x+1,kij.size()-(x+1)));
						x=kij.size();
					}
					
				}
			}

}

void splitItJ(string kij)
{
		char m='1';
		for(int x=0;x<kij.size();x++)
			{
				m=mul(m,kij[x]);			
				if(m=='j' && j==false)
				{
					j=true;
					if(x!=kij.size()-1){
					
						splitItK(kij.substr(x+1,kij.size()-(x+1)));
						x=kij.size();
					}
					
				}
				

			}
}
void splitItK(string kij)
{
		char m='1';
		for(int x=0;x<kij.size();x++)
			{
				m=mul(m,kij[x]);
			    if(m=='k' && k==false && x==kij.size()-1)
				{
					
					k=true;
					break;
				}
			}
}

char mul(char x,char y)
{
if(x=='i' && y=='i')
{
	negative*=-1;
	return '1';
}
else if(x=='i' && y=='j')
	return 'k';
else if(x=='i' && y=='k')
{
	negative*=-1;
	return 'j';
}
else if(x=='j' && y=='i')
	{
	negative*=-1;
	return 'k';
}
else if(x=='j' && y=='j')
{
	negative*=-1;
	return '1';
}
else if(x=='j' && y=='k')
	return 'i';

else if(x=='k' && y=='i')
	return 'j';

else if(x=='k' && y=='j')
{
	negative*=-1;
	return 'i';
}

else if(x=='k' && y=='k')
{
	negative*=-1;
	return '1';
}
else if((x=='1' && y=='i') || (x=='i' && y=='1'))
	return 'i';
else if((x=='1' && y=='j') || (x=='j' && y=='1'))
	return 'j';
else if((x=='1' && y=='k') || (x=='k' && y=='1'))
	return 'k';
else
	return '1';

}
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;
string s;


int main ()
{
	char mymap['z' + 1];
mymap['a']='1';
mymap['b']='0';
mymap['c']='0';
mymap['d']='0';
mymap['e']='1';
mymap['f']='0';
mymap['g']='0';
mymap['h']='0';
mymap['i']='1';
mymap['j']='0';
mymap['k']='0';
mymap['l']='0';
mymap['m']='0';
mymap['n']='0';
mymap['o']='1';
mymap['p']='0';
mymap['q']='0';
mymap['r']='0';
mymap['s']='0';
mymap['t']='0';
mymap['u']='1';
mymap['v']='0';
mymap['w']='0';
mymap['x']='0';
mymap['y']='0';
mymap['z']='0';
	ifstream R("A-small-attempt0.in");
    ofstream W("A-small-attempt0.out");
     
    int t;
    R>>t;
    int n;
    for (int ti=1;ti<=t;++ti)
    {
		R>>s;
		R>>n;
		int stat=0;
		int count=0;
		int last=0;
		int length=s.length();
		//W<<length<<endl;
		for(int i=0;s[i]!='\0';i++)
 			s[i]=mymap[s[i]];
		for(int i=0;s[i]!='\0';i++)
		{
			stat=0;
			for(int j=i;j<i+n;j++)
			{
				if(s[j]=='0')
					continue;
				else
					stat=1;
			}
			if(stat==1)
				continue;
			else
			{
				count=count+(i-last+1)*(length-(i+n)+1);
				//W<<"YYY"<<(i-last+1)<<"  "<<(length-(i+n))<<endl;
				last=i+1;
			}
			//W<<count<<endl;
		}
		W<<"Case #"<<ti<<": "<<count<<endl;
    		//W<<"Case #"<<ti<<": O won"<<endl;
   
    		//W<<"Case #"<<ti<<": Game has not completed"<<endl;
	}
}

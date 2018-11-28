#include<iostream>
#include<fstream>
#include<stdlib.h>


using namespace std;
 

int main()
{
ofstream fo;
fo.open("out.txt");
ifstream fi;
fi.open("input.in");
//input
int t,k,standp,outputi;
char *c;
fi>>t;
for(int i=0;i<t;i++)
{
fi>>k;
//cout<<k<<endl;
c=(char*)malloc((k+2)*sizeof(char));
fi>>c;
standp=0;
outputi=0;
for(int j=0;j<=k;j++)
{
	
	if(j==0)
		standp=(c[j]-'0');
	
	else if(j>standp)
		{
			outputi+=j-standp;
			standp=(c[j]-'0')+j;
		}
	else
		{
			standp+=(c[j]-'0');
		}
}
fo<<"Case #"<<i+1<<": "<<outputi<<endl;

free(c);
}
fo.close();
fi.close();
return 0;
}
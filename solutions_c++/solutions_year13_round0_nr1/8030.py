#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;
string str[4];
unsigned int dot=0;
char ch[2]={'O','X'};

int isvalid(char c,char e,char f,char g,char h)
{
	if((e==c || e=='T') && f==c && g==c && (h=='T' || h==c))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
void hasDot(char e,char f,char g,char h)
{
	if(e=='.')
		dot++;
	if(f=='.')
		dot++;
	if(g=='.')
		dot++;
	if(h=='.')
		dot++;
}

void result(int test)
{
int i,k;
char c,e,f,g,h;


//check horizontal
for(k=0;k<2;k++)
{
	c=ch[k];
	dot=0;
	for(i=0;i<4;i++)
	{
		e=str[i].at(0);
		f=str[i].at(1);
		g=str[i].at(2);
		h=str[i].at(3);
		if(isvalid(c,e,f,g,h))
		{
			cout<<"Case #"<<test<<": "<<c<<" won"<<"\n";
			return;
		}
		else
		{
			hasDot(e,f,g,h);
		}
	}

}
if(dot > 9)
{
        cout<<"Case #"<<test<<": "<<"Game has not completed"<<"\n";
        return;
}

		
for(k=0;k<2;k++)
{
        c=ch[k];
        for(i=0;i<4;i++)
        {
                e=str[0].at(i);
                f=str[1].at(i);
                g=str[2].at(i);
                h=str[3].at(i);
                if(isvalid(c,e,f,g,h))
                {
			cout<<"Case #"<<test<<": "<<c<<" won"<<"\n";
                        return;
                }

        }
	
}

for(k=0;k<2;k++)
{
	
        c=ch[k];
       
                e=str[0].at(0);
                f=str[1].at(1);
                g=str[2].at(2);
                h=str[3].at(3);
                if(isvalid(c,e,f,g,h))
                {
			cout<<"Case #"<<test<<": "<<c<<" won"<<"\n";
                        return;
                }
        
}
for(k=0;k<2;k++)
{
        c=ch[k];
        
                e=str[0].at(3);
                f=str[1].at(2);
                g=str[2].at(1);
                h=str[3].at(0);
                if(isvalid(c,e,f,g,h))
                {
			cout<<"Case #"<<test<<": "<<c<<" won"<<"\n";
                        return;
               }

}
	if(dot==0)
	{
		cout<<"Case #"<<test<<": "<<"Draw"<<"\n";
	}
	else
	{
		cout<<"Case #"<<test<<": "<<"Game has not completed"<<"\n";
	}

}

int main()
{
unsigned long long t,tt,i;
freopen( "input.txt", "r", stdin );
freopen( "output.txt", "w", stdout );
cin>>tt;
string emp;
getchar();

for(t=1;t<=tt;t++)
{
	dot=0;
		for(i=0;i<4;i++)
			getline(cin,str[i]);

	result(t);
	for(i=0;i<4;i++)
		str[i].clear();

	getline(cin,emp);
	
}

return 0;
}

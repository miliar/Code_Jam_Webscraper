#include<bits/stdc++.h>
using namespace std;

char buf[(int)1e6 + 100];
#define ll long long
int main(){

    ifstream cin ("in.txt");
	ofstream cout("out.txt");

ll T= 0,i=1,c=0, len=0;
cin>>T;
for(int j=1;j<=T;j++)
{
		c=0;
	cin>>buf;
		len = strlen(buf);
		while(1)
        {
			i=0;
			if(buf[i]=='+')
			{
				while( buf[i] == '+' && i < len)
                {
					i++;
				}
				if( i == len ){
					break;
				}
				else{
					memset(buf,'-',sizeof(char)*(i+1));
					c++;
				}
			}
			else if(buf[i]=='-')

                {
                    while(buf[i]=='-' && i < len)
                    {
                        i++;
                    }
                    if( i   ==  len)
                    {
                        c++;
                        break;
				}
				else
                {
					memset(buf,'+',sizeof(char)*(i+1));
					c++;
				}

			}
		}
		cout<<"Case #"<<j<<": "<<c<<'\n';
	}
	return 0;
}

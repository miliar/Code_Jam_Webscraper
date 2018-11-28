using namespace std;

 #include <iostream>
 #include <cstdlib>
 #include <fstream>
 #include <cstring>

int main()
{

fstream in, out;

in.open("B-large.in", ios::in);
out.open("B-large.out", ios::out);

char v[1000][1000], v1[1000];
int s_lenght[1000];

int t;
in>>t;

int f=0;
int e=0;

while(in.get(v[f][e]))
{
	f++;
	if(v[f-1][e]=='\n')
	{
		e++;
		f=0;
	}
}

for(int i=0; i<101; i++)
 for(int j=0; j<101; j++)
{
if(v[j][i]=='\n')s_lenght[i]=j;

}

int s_red=0;		//misura la lunghezza della stringa ridotta ricorsivamente
char c_prec='a';		//memorizza il carattere precedente

for(int c=1; c<t+1; c++)
{
////////////////////////////////////////////////////////////////////////////////

for(int i=0; i<s_lenght[c]; i++)
{
if(v[i][c] != c_prec)s_red++;
c_prec = v[i][c];
}

if(s_red%2 == 0)
{
 if(v[0][c]=='+')out<<"Case #"<<c<<": "<<s_red<<endl;
 if(v[0][c]=='-')out<<"Case #"<<c<<": "<<s_red-1<<endl;
}

if(s_red%2 != 0)
{
 if(v[0][c]=='+')out<<"Case #"<<c<<": "<<s_red-1<<endl;
 if(v[0][c]=='-')out<<"Case #"<<c<<": "<<s_red<<endl;
}

s_red=0;
c_prec='a';

////////////////////////////////////////////////////////////////////////////////
}

out<<endl;

in.close();
out.close();

return 0;
}


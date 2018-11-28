using namespace std;

 #include <iostream>
 #include <cstdlib>
 #include <fstream>

int main()
{

fstream in, out;

bool d[10];
for(int i=0; i<10; i++)
 d[i] = false;

int end = 0;

in.open("A-large.in", ios::in);
out.open("A-large.out", ios::out);

int t;
 in>>t;

long digit, digitc = 0;
int digitm = 0;

for(int i=0; i<t; i++)	//verifica di ogni numero
{

for(int j=0; j<10; j++)	//ripristina i valori booleani dell'array d[]
 d[j] = false;
end = 0;
digitm = 0;

in>>digit;
if(digit == 0)
{
out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
end = 11;
}

while(end < 10)
{
	digitm++;
	digitc = digit * digitm;
	
	for(int j=0; j<10; j++)
	 if(digitc%10 == j && d[j] == false)
	  d[j] = true;
	
	while(digitc >= 10)	//isola le cifre con il modulo
	{
		digitc /= 10;
		
		for(int j=0; j<10; j++)
		 if(digitc%10 == j && d[j] == false)
		  d[j] = true;	
	}
	end = 0;
	for(int j=0; j<10; j++) end += d[j];
	
}

if(digit != 0)
 out<<"Case #"<<i+1<<": "<<digit*digitm<<endl;

}

 out << endl;

in.close();
out.close();

return 0;
}


#include<iostream>
#include<fstream>
using namespace std;

int count=0, a[10];

void flush()
{
	count=0;
	for(int i=0;i<10;i++) a[i]=0;
}

void cal(long int n)
{
	int tmp;
	while(n>0){
		tmp = n%10;
		n /= 10;
		if(a[tmp]==0) a[tmp]++, count++;
	}
}

int main()
{
	int j=1, t;
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("outl.txt");
	in>>t;
	while(j<=t){
		long int n, i=1;
		in>>n;
		while(i<=100){
			cal(i*n);
			if(count==10) break;
			i++;
		}
		if(count==10) out<<"Case #"<<j<<": "<<i*n<<endl;
		else out<<"Case #"<<j<<": INSOMNIA\n";
		flush();
		j++;
	}
	in.close();
	out.close();
	return 0;
}

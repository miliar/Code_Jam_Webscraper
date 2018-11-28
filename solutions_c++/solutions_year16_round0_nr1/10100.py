#include <fstream>
using namespace std;

int check(int n, int x[]) {
	int i, j=n;
}

int main()
{
	int t, n, i, j, k, l;
	fstream  file, fin;
	fin.open("input.txt", ios::in);
	file.open("output.txt", ios::out);
	fin>>t;
for(i=1; i<=t; i++)
{
	fin>>n;
	if(n==0) {
	   file<<"Case #"<<i<<": INSOMNIA"<<endl;
	   continue;
	}
	int x[10]={0};
	j=n;
	while(1)
	{
		k=j;			
		while(k) {
			l=k%10;
			x[l]=1;
			k/=10;
		}
		k=0;
		for(l=0; l<10; l++)
		   k+=x[l];
		if(k==10) break;
		j+=n;
	}
   file<<"Case #"<<i<<": "<<j<<endl;
}
		fin.close();
		file.close();
  return 0;
}

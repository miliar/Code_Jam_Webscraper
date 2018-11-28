#include<iostream>
#include<vector>
#include<fstream>
int ht[3000];
int ans[100];
using namespace std;
	ofstream fout("D:/q.txt");
    ifstream fin("B-large.in");
void test(int l );
int main()
{
	
int n,l,cs=0;
fin>> n;
while(n--)
{   cs++;
	for(int i=1;i<=2500;i++) ht[i]=0;
	fin>> l;
	test(l);
	fout <<"Case #"<<cs<<":";
	for(int i=0;i<l;i++)
	fout <<" "<<ans[i];
	fout <<endl;
	
	
}


fout.close();
fin.close();
return 0;
}




void test(int l)
{
	
int i,j=0;
int q=(2*l-1)*l;
while(q--)
{
fin >> i;
ht[i]++;
	
	
}

for(int i=1;i<=2500;i++)
if(ht[i]%2==1) ans[j++]=i;

	
}

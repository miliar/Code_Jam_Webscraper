#include<bits/stdc++.h>
#include<conio.h>
using namespace std;
ifstream file1("A-large.in");
ofstream file2("file2.txt");
int max2(int a[],int &n,int m)
{
	int max=0;
	for(int i=0;i<m;i++) if(a[max]<a[i]) max=i;
	a[max]--;
	file2<<(char)(max+97);
	if(a[max]==0) n--;
	for(int i=0;i<m;i++) if(a[max]<a[i]) max=i;
	a[max]--;
	file2<<(char)(max+97)<<" ";
	if(a[max]==0) n--;
}
int max(int a[],int &n,int m)
{
	int max=0;
	for(int i=0;i<m;i++) if(a[max]<a[i]) max=i;
	a[max]--;
	file2<<(char)(max+97)<<" ";
	if(a[max]==0) n--;
}
void display(int a[],int m,int n)
{
	cout<<"n->"<<n<<"\n";
	for(int i=0;i<m;i++) cout<<a[i]<<" ";
	cout<<endl;
	getch();
}
int main()
{
	int t;
	file1>>t;
	for(int j=0;j<t;j++)
	{
		int n;
		file1>>n;
		int a[n];
		int m=n;
		for(int i=0;i<n;i++) file1>>a[i];
		file2<<"Case #"<<j+1<<": ";
		while(n!=0)
		{
			//display(a,m,n);
			if(n%2==0) max2(a,n,m);
			else max(a,n,m);
		}
		file2<<endl;	
	}
}

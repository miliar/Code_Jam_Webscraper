#include<iostream>
#include<vector>
#include<fstream>

using namespace std;
	ofstream fout("D:\q3.txt");
int n=32;
int j=500;
vector< vector<int> > a(11);
vector<int> residue(11);
int prm[]={2,3,5,7,11,13,17,19,23,29};
//int r[11][33];
int test=1; 
int check1(int b);
int check();
int ress(vector<int> & q, int b);
void display(vector<int> aa);
int next();
int main()
{

fout <<"Case #1:"<<endl;
a[10].push_back(1);
for(int i=1;i<n-1;i++) a[10].push_back(0);
a[10].push_back(1);

//display();


//	display();
//	ress(a[10],7);
//	display();
next();
while(j)
{
	if(check()==1) { display(a[10]);j--;
	for(int b=2;b<=10;b++) fout << " "<<residue[b];
	fout <<endl;
	}
   	next();
}

//next();
//display(a[2]);
fout.close();
	return 0;
 } 
 
 
 
 int next()
 {  int carry=1;
    int carryn=0;
 	int b=2;
	vector<int> quot;//
	
	 for(int i=1;i<a[10].size()-1;i++)
 	{   //vector(int) tmp=a[10];
 		if(carry==1) carryn=i;
		
		 a[10][i]+=carry;
 		carry=a[10][i]/2, a[10][i]=a[10][i]%2;
 	
	   // quot=a[10];
		
		    
	 
	 	
	 }
	 
//	 display(a[10]);

 
 
 
	 if(carry==0) return 1; else return -1;
 }
 
 
 
 
 
 
 int check1(int b)
 {
 	int r=0;
 	for(int i=0;i<10;i++)
 	{  r=0;
 		for(int k=n-1;k>=0;k--)
 		r=(r*b+a[10][k])%prm[i];
 		if(r==0) return prm[i];
	 }
	 
	 return -1;
 	
 }
 
 
 int check()
 { int temp;
 residue.clear();
for(int b=2;b<=10;b++){
temp=check1(b);
if(temp==-1) return -1;
else residue[b]=check1(b); 	
 }
 	return 1;
 	
 }
 
 
 void display(vector<int> aa)
 {
 	
 	for(int i=aa.size()-1;i>=0;i--)
 	fout << aa[i];
 //	cout <<endl;
 }
 
 
 int ress(vector<int> & q, int b)
 {
 	
 	vector<int> qo;
	 int n=q.size()-1;
 	int r=0;
	 //if(q[n]<b) r=q[n],n--;
	 
	while(n>=0)
	{
		qo.insert(qo.begin(),(r*10+q[n])/b);
		
		r=(10*r+q[n])%b;
	//	display(qo);
		n--;
		
	}
	 
	 
	q=qo;  
 	while(q.size()>0 && q[q.size()-1]==0) q.erase(q.end()-1);
	 
	 return r;
 	
 	
 	
 }

#include<iostream>
#include<stdio.h>

using namespace std;

int ans,m,n,t,b;
int i,j,k,p,q,z;//iteratr
int c1,c2,f,f1,f2;//counter
char ch;
int sol;
int a[100][100];
int rowmax[100];
int colmax[100];

int check(int i,int j)
{
	if((a[i][j] < rowmax[i]) && (a[i][j] < colmax[j]))
		return 1;
	return 0;
}

int calc()
{
	   for(i=0;i<n;i++)
		   rowmax[i] = -1;
	   
	   for(i=0;i<m;i++)
		   colmax[i] = -1;

	   for(i=0;i<n;i++)
		   for(j=0;j<m;j++)
		   {
			   if(rowmax[i] < a[i][j])
				   rowmax[i] = a[i][j];
			   if(colmax[j] < a[i][j])
				   colmax[j] = a[i][j];
		   }
	   for(i=0;i<n;i++)
		   for(j=0;j<m;j++)
		   {
			   sol = check(i,j);
			   if(sol == 1)
			   {
				   //cout << "\ni:"<<i<<" j:"<<j<<endl;
				   return 1;
			   }
		   }
	return 0;
}

int main(){
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;	
    k = 1;
    while(k<=t)
    {
		cin >> n >> m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin >> a[i][j];
		ans = calc();
		cout << "Case #"<<k<<": ";
        if(ans == 1)
            cout<<"NO"<<endl;
        else
            cout<<"YES"<<endl;
        k++;		
    }
	cin >> p;
    return 0;
}
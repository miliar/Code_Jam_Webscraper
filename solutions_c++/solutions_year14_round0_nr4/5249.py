#include<iostream>
#include <fstream>
using namespace std;
void mergesort(float *,int,int);
void merge(float *,int,int,int);

void mergesort(float *a,int p,int r)
{
     if( p < r)
    {
         int q=(p+r)/2;
         mergesort(a,p,q);
         mergesort(a,q+1,r) ;
         merge(a,p,q,r);
     }
}
void merge(float *a,int p,int q,int r)
{
 float *c = new float[25];
int i=p;
int j=q+1;

int k=p;
while((i<=q)&&(j<=r))
{
if(a[i]<a[j])
{
     c[k]=a[i];
      i=i+1;
     k=k+1;
}
else
{
     c[k]=a[j];
      j=j+1;
      k=k+1;
}
}
while(i<=q)
{
     c[k] =a[i];
     i=i+1;
     k=k+1;
}
while(j<=r)
{
     c[k]=a[j];
     j=j+1;
     k=k+1;
}
int l=p;
while(l<=r)
{
a[l]=c[l];
l=l+1;
}

}

int main()
{
	int test,n,z,ken,y,x,k,p,q;
	float first_n ,first_k ,last_n , last_k ;
	cin >> test;
	ofstream myfile;
	myfile.open ("ex5.txt");
	//x = n;
	x = test;
	while(test)
	{	
		cin >> n;
		ken=0,z=0,y=0;
		float *a = new float[n];
		float *b = new float[n];
		for(int i=0;i<n;i++)
		{
			cin >> a[i];
		}
		for(int i=0;i<n;i++)
		{
			cin >> b[i];
		}
		
		mergesort(a,0,n-1);
		/*for(int i=0;i<n;i++)
		{
     		cout<<"\n"<<a[i];
		}*/
		//cout << "Ankitd32";
		mergesort(b,0,n-1);
		/*for(int i=0;i<n;i++)
{
     cout<<"\n"<<b[i];
}*/
		int i=0,j=0;
		while(i<n && j<n)
		{
			if(a[i]<b[j])
			{
				i++;
				j++;
				//cout << "Hello";
			}
			else if(a[i] > b[j])
			{
				j++;
				z++;
			}
		}
	//for()	
		
		k=n-1,p=n-1,q=0;
		while((ken+y) < n)
		{
			first_n = a[q];
			first_k = b[q];
			last_n = a[k];
			last_k = b[p];
			if(last_n < last_k)
			{
				ken++;
				if(p != 0)
				p--;
				if(q != n-1)
				q++;
				//cout << ; 
		
			}
			else if(last_n > last_k)
			{
				y++;
				if(k != 0)
				k--;
				if(p != 0)
				p--;
			
			}
		}
		myfile << "Case #"<<x-(test-1)<<": "<<y <<" " << z <<"\n";
		test--;
	}
	return 0;
}

#include <iostream>
#include<fstream>


using namespace std;

int partition(double *a,int p,int r)
{
	int i=p-1,j;
	double x=a[r];  //last element
	double t,te;
	
	for(j=p;j<=r-1;j++)
	{
	   if(a[j]<=x)
	     {
	     	i=i+1;
	     	t=a[i];
	     	a[i]=a[j];
	     	a[j]=t;
	     	
	     }
   }
   
   te=a[i+1];
   a[i+1]=a[r];
   a[r]=te;
   
   return (i+1);
   
   
}


void quicksort(double a[],int p,int r)
{
	if(p<r)
	  { int q,i;
	      q=partition(a,p,r);
	      //cout<<q<<"partition"<<endl;
	        quicksort(a,p,q-1);
	       
	        //cout<<"sublist"<<endl;
	        quicksort(a,q+1,r);
	        
		
	        //cout<<"sublist"<<endl;
      }
	
}


int main()
{
		freopen("D-large.in","r",stdin); 
	freopen("Problem_d_large.txt","w",stdout);
	int t,x,c;
	cin>>t;
	for(x=0;x<t;x++)
	{   
		cout<<"Case #"<<x+1<<": ";
		//a->niomi b->boy
	  int n,i,j,k;
	  cin>>n;	
	  double *a=new double[n];
	  double *b=new double[n];
	
	  
	  for(i=0;i<n;i++)
	  cin>>a[i];
	  for(i=0;i<n;i++)
	  cin>>b[i];
	
	
	  quicksort(a,0,n-1);
	  quicksort(b,0,n-1);
	   
	//   for(i=0;i<n;i++)
	  //cout<<a[i]<<" ";
	  //cout<<endl;
	  //for(i=0;i<n;i++)
	 // cout<<b[i]<<" ";
	  //cout<<endl<<endl;
	  
	 
	
	
	 //cout<<"d war"<<endl;
	  i=0;
	  j=0;
	  
	  c=0;
	
	while(i<n && j<n)
	  {
	  	if(a[i]>b[j])
	  	  {
			//cout<<a[i]<<" destroyed with "<<b[k]<<endl;
		  	//destroy max of boy with least of gal
		  	i++;
		  	j++;
		  	c++;
		
	      }
			
			
	  	  
	  	else
		  {
		  	//cout<<a[i]<<"<"<<b[j]<<endl;
			i++;//girl
	  	     //boy
	  	    
		  }  
	//	  cout<<i<<" i "<<j<<" j "<<endl;
	  }
	  cout<<c<<" ";
	  
	   i=0;
	  j=0;
	  
	  c=0;
	  
	  //cout<<"o war"<<endl;
	
	  while(i<n && j<n)
	  {
	  	if(a[i]<b[j])
	  	  {//cout<<a[i]<<">"<<b[j]<<endl;
			i++;//girl
	  	    j++; //boy
	  	    
	  	  }
	  	else
		  {//cout<<a[k]<<" destroyed with "<<b[j]<<endl;
		  	j++;
		  	c++;
		  }  
		//  cout<<i<<" i "<<j<<" j "<<endl;
	  }
	  cout<<c<<endl;
	
	
		
    }
	
	return 0;
}

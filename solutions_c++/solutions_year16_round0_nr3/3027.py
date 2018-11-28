// C++ program to generate n-bit Gray codes
#include <bits/stdc++.h>
#define ll long long int
using namespace std;
 
// This function generates all n bit Gray codes and prints the

// generated codes

long long int powr (long long int a, long long int b)
{
    if (b == 0)
        return 1;
    long long int x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x);
    else
        return (((x*x))*a);
}

int isPrime(ll n){
    ll i;

    if (n==2)
        return 1;

    if (n%2==0)
        return 0;

    for (i=2;i<=sqrt(n);i++)
        if (n%i==0)
            return 0;

    return 1;
}

void generateGrayarr(int n,ll b)
{
    // base case
    if (n <= 0)
        return;
 
    // 'arr' will store all generated codes
    vector<string> arr;
 
    // start with one-bit pattern
    arr.push_back("0");
    arr.push_back("1");
 
    // Every iteration of this loop generates 2*i codes from previously
    // generated i codes.
    ll i, j;
    string br[75000];
    for (i = 2; i < (1<<n); i = i<<1)
    {
        // Enter the prviously generated codes again in arr[] in reverse
        // order. Nor arr[] has double number of codes.
        for (j = i-1 ; j >= 0 ; j--)
            arr.push_back(arr[j]);
 
        // append 0 to the first half
        for (j = 0 ; j < i ; j++)
            arr[j] = "0" + arr[j];
 
        // append 1 to the second half
        for (j = i ; j < 2*i ; j++)
            arr[j] = "1" + arr[j];
    }
    
  //cout<<arr.size();
    // print contents of arr[]
    //for (i = 0 ; i < arr.size() ; i++ )
        //cout << arr[i] << endl<<"\n";
        
    int first=0;
    int sec,c,flag=0;
    ll k,sum,t;
    ll ar[10000][10];
    j=0;
    for (i = 0 ; i < arr.size() ; i++ )
    {
        if(arr[i][0]==arr[i][n-1] && arr[i][0]=='1')
        {
        //	cout<<arr[i]<<"\n";
        	c=1;
        	sec=0;
        	for(int p=2;p<=10;p++)
        	{
        	sum=0;
        	//j1=0;
        	k=1;
        	for(int x=n-1;x>=0;x--)
        	{
        		if(arr[i][x]=='1')
        		{
        		sum+=k;
        	    }
        		else
        		sum+=0;
        		k=k*p;
        	//	j++;
			}
		
			if(isPrime(sum)==1)
			{
			flag=1;
		
			break;
		    }
			else
			{
			//cout<<sum<<"\n";
			//cout<<"-";
			 	c++; 
			for(t=2;t<=sum;t++)
			{
			   
				if(sum%t==0)
				{
				 /* if(p==10)
				  cout<<"!!"<<t<<'\n';*/
				ar[first][sec++]=t;
					//cout<<t<<" "<<c<<"\n";
				break;
			    }
			}
					if(c==10)
	{
		//cout<<"Hello ";
	//	cout<<arr[i]<<"\n";
	//cout<<sec<<"\n";
	j++;
	
	br[first]=arr[i];
	first++;
	if(j==b)
	break;
    }
		}
	
			
		}
		//cout<<" \n ROUND1   \n......";
		if(j==b)
		break;
		}
	
    }
	for(i=0;i<b;i++)
	{
		cout<<br[i]<<" ";
		for(j=0;j<9;j++)
		cout<<ar[i][j]<<" ";
		cout<<"\n";
	}
	//cout<<"\n";
	}
 
// Driver program to test above function
int main()
{
    int n,t;ll b;
    cin>>t;
    cin>>n>>b;
    cout<<"Case #1:\n";
    generateGrayarr(n,b);
    return 0;
}
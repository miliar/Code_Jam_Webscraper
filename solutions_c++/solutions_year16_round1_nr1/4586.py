#include<fstream>
#include<iostream>
#include <string.h>
void quicksort (char [],int,int);

using namespace std;

int main()
{
	//ofstream jv("input.txt");
	ofstream jv1("output.txt");
//	freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
	//string s;
	//char p[1001];
///	char xx[001];
//	char s[1001];
	int  t;
	string s;
	cin >> t;
	//jv >> t;
	for(int k=1; k<=t; ++k)
	{
		cin >> s;
		//char xx=s[0];
		string x;
		x[0]='s[0]';
		x[1]='\0';
		//xx[1]='\0';
		char xx=s[0];
		string q=x;
		for(int i=0;i<s.length();i++)
		{
			if(q[0]-s[i] <= 0)
			{
				q=string (s[i]+q);
				//strcat(q,x);
			}
			else
			{
				q=string(q+s[i]);
				//strcat();
			}
		}
	//	quicksort(s,0,strlen(s)-1);
	//	cout << "Case #" << k << ": "<< q << endl;
		jv1 << "Case #" << k << ": "<< q << endl;
	}
	jv1.close();
	return 0;
}

void quicksort(char a[],int first,int last)
{
	int i,j;
	int pivot;
	int temp;
	if(first<last)
	{
		pivot=first;
		i=first;
		j=last;
		while(i<j)
		{
	    	while(a[i]<=a[pivot] && i<j)
			{  
				if(a[i]==a[pivot])
				pivot=i;
				i++;
		    }
	    	while(a[j]>a[pivot] )   
		    j--;
		    if(i<j)                                      
	    	{
			     temp=a[i];
				a[i]=a[j];
			   	a[j]=temp;
			   	i++;j--;
			}
		}                  
		temp=a[pivot];
		a[pivot]=a[j];
		a[j]=temp;
		quicksort(a,first,j-1);     
		quicksort(a,j+1,last);	   
	}
}

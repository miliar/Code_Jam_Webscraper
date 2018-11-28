#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <string>
#include <stdlib.h>
using namespace std;

struct node{
	int freq;
	char ch;
};
bool f1(struct node &i, struct node &j) { return i.freq > j.freq; }

void find(int arr[], int test, int n)
{
	ofstream outfile;

  	outfile.open("output.txt", std::ios_base::app);
	outfile << "Case #"<<test<<":";
	struct node b[n];
	for(int i=0; i<n; i++)
	{
		b[i].freq=arr[i];
		b[i].ch='A'+i;
	}
	sort(b,b+n,f1);
	while(b[0].freq>0)
	{
		if(n==3 && b[0].freq==b[1].freq && b[1].freq==b[2].freq)
		{
			outfile <<" "<<b[0].ch;
			b[0].freq--;
		}	

		else if(b[0].freq > b[1].freq)
		{
			outfile <<" "<<b[0].ch<<b[0].ch;
			b[0].freq--;
			b[0].freq--;
		}

		else if(b[0].freq == b[1].freq)
		{
			outfile <<" "<<b[0].ch<<b[1].ch;
			b[0].freq--;
			b[1].freq--;
		}
		else if(b[1].freq==0)
		{
			outfile <<" "<<b[0].ch;
			b[0].freq--;
		}

		sort(b,b+n,f1);
		int size=0;
		for(int i=0;i<n;i++)
		{
			if(b[i].freq>0)
				size++;
		}
		n=size;
	}
	outfile << endl;
}
int main()
{
	long long int test, i=1;
	ifstream myfile ("b.txt");
	if (myfile.is_open())
  	{
  		myfile >> test;
  		int n;
  		int arr[27];
	    while ( myfile>>n )
	    {
	      memset(arr,0,27);
	      for(int j =0;j<n;j++)
	      {
	      	myfile>>arr[j];
	      }
	      find(arr,i,n);
	      i = i+1;
	    }
	    myfile.close();
  	}
	return 0;
}
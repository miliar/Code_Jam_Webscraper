#include<stdio.h>
#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int T;


  freopen ("A-large.in","r",stdin);
  freopen("A_large_output.out", "w", stdout);

//Getting number of times
	scanf("%d", &T);


//For each number
for(int t=1;t<=T;t++){
	string str;
	cin>>str;
	
	
	int count[26] = {0};
	int digit[10] = {0};
	for(int i=0;i<str.length();i++)
	{
		count[str[i]-65]++;
	}
	
	
	// for(int i=0;i<26;i++)
// 	{
// 		cout<<char(i+65)<<": "<< count[i] << "  ";
// 	}
// 	cout<<'\n';
// 	
	
	//1 Z -- 0
	digit[0]= count[25];
	// Reduce R, O
	count[82-65] -= count[25];
	count[79-65] -= count[25];
	
	//2 G--8
	digit[8] = count[71-65];
	//Reduce H
	count[72-65] -= count[71-65];
	
	//3 X--6
	digit[6] = count[88-65];
	// Reduce S
	count[83-65] -= count[88-65];
	
	//4 H--3
	digit[3] = count[72-65];
	// Reduce R
	count[82-65] -= count[72-65];
	
	//5 W--2
	digit[2] = count[87-65];
	// Reduce O
	count[79-65] -= count[87-65];
	
	//6 S--7
	digit[7] = count[83-65]; 
	//Reduce V, N
	count[86-65] -= count[83-65];
	count[78-65] -= count[83-65];
	
	//7 V--5
	digit[5] = count[86-65];

	//8 R--4
	digit[4] = count[82-65];
	// Reduce O
	count[79-65] -= count[82-65];
	
	//9 O--1
	digit[1] = count[79-65];
	//Reduce N
	count[78-65] -= count[79-65];
	
	//10 N/2--9
	digit[9] = count[78-65]/2; 
	
// 	for(int i=0;i<26;i++)
// 	{
// 		cout<< count[i] << "  ";
// 	}
// 	cout<<'\n';
	
	cout<<"Case #"<<t<<": ";
	for(int i=0;i<10;i++)
	{
		for(int j=0;j<digit[i];j++)
			cout<<i;
	}
	cout<<'\n';
	
	/*
	vector<int> nstr(str.length(),0);
	vector<int> output;
	vector<int>::iterator mid, temp;

	for(int i=0;i<str.length();i++)
	{
		nstr[i]=str[i];
		//cout<<nstr[i]<<' ';
	}
	int bestcount=1, best=0;
	for(int i=0;i<nstr.size();i++)
	{
		if(nstr[i]>=bestcount)
		{
			best=i;
			bestcount=nstr[i];
		}	
	}
	output.push_back(nstr[best]);
	for(int j=best+1;j<nstr.size();j++)
	{
		output.push_back(nstr[j]);
	}
	nstr.erase(nstr.begin()+best,nstr.end());
	mid= output.begin()+1;
 
 	
	
	int itr=1;
	
	while(!nstr.empty())
 	{
 		bestcount=1, best=0;
 		for(int i=0;i<nstr.size();i++)
 		{
 			if(nstr[i]>=bestcount)
 			{
 				best=i;
 				bestcount=nstr[i];
 			}	
 		}
 		output.insert(output.begin()+itr,nstr.begin()+best, nstr.end());
 		itr++;
 		//mid=mid+1;
 		//cout<<mid-output.begin()<<" Inc\n";
		nstr.erase(nstr.begin()+best,nstr.end()); 	
	
 	}
 	printf("Case #%d: ", t);
	for(int ii=0;ii<output.size();ii++) 
		printf("%c", (char)output[ii]);
	printf("\n");
			
	*/
 		
 	
}

return 0;
}
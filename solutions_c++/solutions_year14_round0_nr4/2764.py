#include <cstdio>
#include <iostream>
using namespace std;

int main() {
/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
int t, total;
cin>>t;
total=t;
while(t-- && t<=50){
int totalBlocks;
cin>>totalBlocks;
double ken[totalBlocks],naomi[totalBlocks];

for(int i=0;i<totalBlocks;i++)
cin>>naomi[i];
for(int i=0;i<totalBlocks;i++)
cin>>ken[i];

//arrange blocks in ascending order
bool flag = true;
double temp;
int naomiCount,kenCount;
while(flag)
{
kenCount=0;
naomiCount=0;
for(int i=0;i<(totalBlocks-1);i++)
{
	if(ken[i] > ken[i+1])
	{
		temp=ken[i];
		ken[i]=ken[i+1];
		ken[i+1]=temp;
		kenCount++;
	}

	if(naomi[i] > naomi[i+1])
	{
		temp=naomi[i];
		naomi[i]=naomi[i+1];
		naomi[i+1]=temp;
		naomiCount++;
	}
}
if(!kenCount && !naomiCount)
flag=false;
}

double naomi2[totalBlocks],ken2[totalBlocks];
for(int k=0; k < totalBlocks; k++)
{
naomi2[k]=naomi[k];
ken2[k]=ken[k];
}

//for(int k=0; k < totalBlocks; k++)
//{
//cout<<naomi2[k]<<"    "<<ken2[k]<<endl;
//}

//when Naomi doesn't cheat
int kenScore=0, naomiScore=0;
for(int i=0;i<totalBlocks;i++)
{
double naomiChose, kenChose;
naomiChose = naomi[totalBlocks-i-1];
int j;
for(j=0; j<totalBlocks ; j++)
{
	kenChose = ken[j];
	if(kenChose > naomiChose)
		break;
}

//ken wins 
	if(j < totalBlocks)
	{
	kenScore++;
	ken[j]=0;
	}
	else
	{
	naomiScore++;
	for(int k=0; k < totalBlocks; k++)
		if(ken[k]!=0)	
			{	
			ken[k]=0;
			break;
			}
	}

naomi[totalBlocks-i-1]=0;
}

//when naomi bluffs
int kenBluffScore=0, naomiBluffScore=0,eli=0;
for(int i=0;(i+eli)<totalBlocks;i++)
{
if(naomi2[totalBlocks-i-1] < ken2[totalBlocks-i-1-eli])
while(naomi2[totalBlocks-i-1] < ken2[totalBlocks-i-1-eli])
eli++;
}
naomiBluffScore=totalBlocks-eli;

cout<<"Case #"<<total-t<<": "<<naomiBluffScore<<" "<<naomiScore<<endl;
}
    return 0;
}

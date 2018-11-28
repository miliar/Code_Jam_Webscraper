#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#define re
using namespace std;


int t;
int a1,b1;
int a[4];
int b[4];

void solve(int case_no){

	bool isFound = false;
	bool isMultiple = false;
	int card_no = -1;

	

	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++){
			if(a[i]==b[j]){
				if(card_no != -1){
					isMultiple = true;
				}
				isFound = true;
				card_no = a[i];
			}
		}

		cout<<"Case #"<<case_no<<": ";

	if(isMultiple)
		cout<<"Bad magician!";
	else if(!isFound)
		cout<<"Volunteer cheated!";
	else
		cout<<card_no;
	cout<<endl;

}


int main(int argc, char const *argv[])
{
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif

cin>>t;
int temp;
for(int j=1;j<=t;j++){
cin>>a1;

for(int i=0;i<4;i++)
{
	for(int j=0;j<4;j++)
	{
		if(i==a1-1)
			cin>>a[j];
		else
			cin>>temp;
	}
}
cin>>b1;
for(int i=0;i<4;i++)
{
	for(int j=0;j<4;j++)
	{
		if(i==b1-1)
			cin>>b[j];
		else
			cin>>temp;
	}
}
solve(j);
}
    	
/*#ifdef re
printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif*/
return 0;
}

#include<iostream>
using namespace std;
int main(){
	int t,caseno;
	cin>>t;
	caseno = 0;
	while(t-->0)
	{
		caseno++;
	int a[4][4];
	int b[4][4];
	
	int choice1,choice2;
	cin>>choice1;
	choice1--;
	for(int i=0;i<4;i++)
	{ for(int j=0;j<4;j++)
	  {
		cin>>a[i][j];
	  }
	}
	cin>>choice2;
	choice2--;
		for(int i=0;i<4;i++)
	{ for(int j=0;j<4;j++)
	  {
		cin>>b[i][j];
	  }
	}
    
	/////////////////////////***********************////////////////////////
    int counter=0,value=0;
	for(int i=0;i<4;i++)
	{ for(int j=0;j<4;j++)
	  {
       if(a[choice1][i]==b[choice2][j])
	     {counter++;  
		 value=a[choice1][i];
		 }
	  }
	}
	if(counter>1)
	 cout<<"Case #"<<caseno<<": Bad magician!"<<endl;
	else{
	if(counter==1)
	 cout<<"Case #"<<caseno<<": "<<value<<endl;
	else
	 cout<<"Case #"<<caseno<<": Volunteer cheated!"<<endl;
	 }
	}
	cin.get();
	cin.get();
	return 0;
	}

#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(){
char ans[105][100];
int row1[5],T,card,i,rowno,j,k,x,l,flag;


cin>>T;
for(i=0;i<T;i++)
{card=-1;
flag=0;
	cin>>rowno;
	for(j=0;j<4;j++)
	{
		for(k=0;k<4;k++)
		{
			cin>>x;
			if((j+1)==rowno)
			{
				row1[k]=x;
			}
		}	
	}	


	cin>>rowno;
	for(j=0;j<4;j++)
	{
		for(k=0;k<4;k++)
		{
			cin>>x;
			if((j+1)==rowno)
			{
				for(l=0;l<4;l++)
				{
					if(x==row1[l])
					{
						if(card==-1)
						{card=x; }
						else{flag=1;}
					}
				}
			}
		}	
	}	


if(card==-1)
strcpy(ans[i],"Volunteer cheated!");
else
if(flag==1)
strcpy(ans[i],"Bad magician!");
else{
sprintf(ans[i],"%d",card);
}
}

for(i=1;i<=T;i++){
cout<<"Case #"<<i<<": "<<ans[i-1]<<endl;
}
return 0;}

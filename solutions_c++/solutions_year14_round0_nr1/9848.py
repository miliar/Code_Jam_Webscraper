#include<iostream>
using namespace std;
int main()
{ int t, a[4][4],b[4][4],i,j,f,s,m,flag,op; 
cin>>t;
for(int k=0;k<t;k++)
{	
	cin>>f;
	for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
        cin>>a[i][j];
     cin>>s;    
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
        cin>>b[i][j];
    flag=0;    
    for(int m=1;m<=4;m++)
    for(int n=1;n<=4;n++)
    if(a[f][m]==b[s][n])
    {
    	flag++;
    	op=a[f][m];
    }

	if(flag==1)
	cout<<"Case #"<<k+1<<": "<<op<<endl;
	else if(flag>1)
    cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
    else
    cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;	
} 
    return 0;
    
}
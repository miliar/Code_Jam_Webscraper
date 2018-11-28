#include<iostream>
using namespace std;
int main()
{
	int T,p,i=0,j=0,k=0,ans1,ans2,mat1[4][4],mat2[4][4],ans[4],card,count=0;
	cin>>T;
	for(p=0;p<T;p++)
	{cin>>ans1;
	 count=0;
	 for(i=0;i<4;i++)
	 { 
	 	for(j=0;j<4;j++)
		{
		 cin>>mat1[i][j];
		 if(ans1==(i+1))
		  ans[j]=mat1[i][j];
	    }
	 }
	
	 cin>>ans2;
	 for(i=0;i<4;i++)
	 {  
	 	for(j=0;j<4;j++)
		{
		 cin>>mat2[i][j];
		 if(ans2==(i+1))
		 {
			for(k=0;k<4;k++)
			{
				if(mat2[i][j]==ans[k])
				{
				 card=ans[k];
				 count++;
				 break;
			    } 
			}
		 }
	    }
	 }
	 cout<<"Case #"<<p+1<<": ";
	 if(count>0)
	 {
		if(count==1)
		 cout<<card<<endl;
		else
		 cout<<"Bad magician!"<<endl;
	 }
	 else
	  cout<<"Volunteer cheated!"<<endl;
   }
}

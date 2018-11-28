#include<iostream>
#include<fstream>>

using namespace std;

int main()
{
	int t,i,j,t1,t2,flag,num,temp,count;
	fstream fout;
	fout.open("Op.txt",ios::out);
	cin>>t;
	int r1[4][4],r2[4][4],row1,row2,r1t[4],r2t[4];
	count=1;
	
	while(count<=t)
	{
		cin>>row1;
		for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
		        cin>>r1[i][j];
		    
		    
		cin>>row2;
		for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
		        cin>>r2[i][j];
		        
		for(i=0;i<4;i++)
		{
			r1t[i]=r1[row1-1][i];
			r2t[i]=r2[row2-1][i];
		}
		
		for(i=0;i<3;i++)
		    for(j=i+1;j<4;j++)
		    {
		    	if(r1t[i]>r1t[j])
		    	{
		    		temp=r1t[i];
		    		r1t[i]=r1t[j];
		    		r1t[j]=temp;
		    	}
		    }
		    
		for(i=0;i<3;i++)
		    for(j=i+1;j<4;j++)
		    {
		    	if(r2t[i]>r2t[j])
		    	{
		    		temp=r2t[i];
		    		r2t[i]=r2t[j];
		    		r2t[j]=temp;
		    	}
		    }
		
		t1=0;t2=0;flag=0;
		while(t1<4 &&t2<4)
		{
			if(r1t[t1]<r2t[t2])
			    t1++;
			else if(r2t[t2]<r1t[t1])
			    t2++;
			else
			{
				num=r2t[t2];t1++;t2++;flag++;
			}
		}
		
		if(flag>1)
			fout<<"Case #"<<count<<": Bad magician!\n";
		else if(flag==0)
		    fout<<"Case #"<<count<<": Volunteer cheated!\n";
		else
		    fout<<"Case #"<<count<<": "<<num<<endl;
		    
		count++;
	}
	
	
fout.close();
return 0;	
	
}
















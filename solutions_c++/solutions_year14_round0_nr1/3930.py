#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,x[4][4],y[4][4],arr[4],ans[4],cnt=0,a,b,count=1,j=0,i,k,l,temp;
	string s;
	fstream fin;
	fin.open("A-small-attempt0.in",ios::in);
    fstream fout;
    fout.open("output_codejam.out",ios::out);
	if(fin.is_open())
	{
    	i=0;
    	while(getline(fin,s))
    	{
    		istringstream iss(s);
    		k=0,l=0;
    		while(iss>>temp)
    		{
    			if(j==0)
    			{
    				t=temp;
    				j=1;
    			}
    			else if(j==1)
    			{
    				a=temp;
    				j=2;
    			}
    			else if(j==2)
    			{
    				x[i][k++]=temp;
    			}
    			else if(j==3)
    			{
    				b=temp;
    				j=4;
    			}
    			else if(j==4)
    			{
    				y[i][l++]=temp;
    			}
    		}
    		if(i==3 && l==4)
    		{
    			/*for(i=0;i<4;i++)
    			{
    				for(j=0;j<4;j++)
    					printf("%d ",x[i][j]);
    				printf("\n");
    			}
    			for(i=0;i<4;i++)
    			{
    				for(j=0;j<4;j++)
    					printf("%d ",y[i][j]);
    				printf("\n");
    			}*/
    			for(i=0;i<4;i++)
    			{
    				ans[i]=0;
    				arr[i]=x[a-1][i];
    			}
    			for(i=0;i<4;i++)
    			{
    				for(j=0;j<4;j++)
    				{
    					if(arr[i]==y[b-1][j])
    					{
    						ans[cnt++]=arr[i];
    					}
    				}
    			}
    			if(cnt==1)
    				fout<<"Case #"<<count++<<": "<<ans[0]<<endl;
    			else if(cnt==0)
    				fout<<"Case #"<<count++<<": Volunteer cheated!"<<endl;
    			else
    				fout<<"Case #"<<count++<<": Bad magician!\n";
    			j=1;cnt=0;i=0;
    		}
            if((j==2 && k==4) || (j==4 && l==4))
                i=(i+1)%4;
            if(i==0 && k==4)
                j=3;
    	}
  	}
    fin.close();
    fout.close();
    return 0;
}
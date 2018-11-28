# include <iostream>
using namespace std;
int main()
{
	int noc;
	
	int ele[1010];
	cin>>noc;
//	cout<<noc<<"iuewhihfiew\n";
	for(int k=1;k<=noc;k++)
	{
		int nof=0,nos=0,Smax=0;
		//cout<<"in while\n";
		cin>>Smax;
		//cout<<Smax<<"dfsrefser";
		for(int i=0;i<=Smax;i++)
        {
          char c;
    	  cin>>c;
    	  ele[i]=(int)c-48;
        }
        
        for(int j=0;j<=Smax;j++)
        {
        	if(ele[j]>0&&nos>=j)
        	{
     //   		cout<<"in if "<<ele[j]<<" "<<nos<<"\n";
        		nos+=ele[j];
        	}
        	else if(ele[j]>0&&nos<=j)
        	{
       // 		cout<<"in else "<<ele[j]<<" "<<nos<<'\n';
                 nof+=(j-nos);
                 nos+=(ele[j]+(j-nos));
        	}

        }  
        cout<<"Case #"<<k<<": "<<nof<<"\n";
	//	noc--;
	}
    
	return 0;
}
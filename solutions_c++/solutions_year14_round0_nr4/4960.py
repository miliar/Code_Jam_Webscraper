#include <iostream>
#include<iomanip>
#include<algorithm>
#include<stdlib.h>
using namespace std;

int main() {
	int T,N,i,j,k,noc;
	cin>>T;
	for(noc=1;noc<=T;noc++)
	{
		cin>>N;
		double NA[N],dNA[N],wNA[N],vdNA[N],vwNA[N],x;
		double KE[N],dKE[N],wKE[N],vdKE[N],vwKE[N],next_val;
		for(i=0;i<N;i++)
		{
			cin>>x;
			NA[i]=x;
			dNA[i]=NA[i];
			wNA[i]=NA[i];
			vdNA[i]=0;
			vwNA[i]=0;
		}
		for(i=0;i<N;i++)
		{
			cin>>x;
			KE[i]=x;
			dKE[i]=KE[i];
			wKE[i]=	KE[i];
			vdKE[i]=0;
			vwKE[i]=0;
		}
		// for war game
		sort(wNA,wNA+N,greater<double>());
		sort(wKE,wKE+N,greater<double>());
		int flag=0,index=-1;
		int wwin=0,dwin=0,rem=0;
		for(i=0;i<N;i++)
		{
			next_val=wNA[i];
			flag=0;
			for(j=0;j<N;j++)
			 {
			 	if(next_val < wKE[j] && (vwKE[j]==0))
			 	{  // smallest number greater than next_val
			 		flag=1;
			 		index=j;
			 	}
			 	if((next_val > wKE[j]) && (flag==1))
			 	{
			 		break;
			 	}
			 }
			 if(flag==0)
			 {
			 	for(j=N-1;j>=0;j--)
			 	{
			 		if(vwKE[j]==0)
			 		{
			 			vwKE[j]=1;
			 			break;
			 		}
			 	}
			 	wwin++;
			 }
			 else
			 {
			 	vwKE[index]=1;
			 	flag=0;
			 }
			 // make vwKE[index] visited && flag==1
			 
		}
		//for Decitful game
		sort(dNA,dNA+N);
		sort(dKE,dKE+N);
		rem=N;
		for(i=0;i<N;i++)
		{
			next_val=dNA[i];
			flag=0;
			for(j=0;j<N;j++)
			{
				if(next_val > dKE[j] && (vdKE[j]==0))
				{
					flag=1;
					index=j;
					break;
				}
				if(next_val < dKE[j] && vdKE[j]==0 )
				 break;
			}
			if(flag==0)
			{
				for(j=N-1;j>=0;j--)
				{
					if(vdKE[j]==0)
					{
						vdKE[j]=1;
						break;
					}
				}
			}
			else
			{
				vdKE[index]=1;
				dwin++;
			}
			
		}
		/*for(i=0;i<N;i++)
		{
			cout<<wNA[i]<<" ";
		}*/
		cout<<"Case #"<<noc<<":"<<" "<<dwin<<" "<<wwin<<endl;
	}
	
	return 0;
}
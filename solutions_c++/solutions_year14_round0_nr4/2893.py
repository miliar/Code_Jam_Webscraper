//============================================================================
// Name        : codeforces.cpp
// Author      : xiao chang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
double Naomi[1003],Ken[1003],Naomi2[1003],Ken2[1003];
int main() {
  int t,i,j,l,flag,k;
  int N,war,dwar;
  cin>>t;
  l=t;
  while(t--)
  {
	  war=0;
	  dwar=0;
	  for(i=0;i<1003;i++)
	  {
		  Naomi[i]=-1;
		  Ken[i]=-1;
	  }
	  cin>>N;
	  for(i=0;i<N;i++)
		  scanf("%lf",&Naomi[i]);
	  for(i=0;i<N;i++)
		  scanf("%lf",&Ken[i]);
	  sort(Naomi,Naomi+N);
	  sort(Ken,Ken+N);
	 // for(i=0;i<N;i++)
		//  cout<<Naomi[i]<<" "<<Ken[i]<<endl;
	  for(i=0;i<N;i++)
	  {
		  Naomi2[i]=Naomi[i];
		  Ken2[i]=Ken[i];
	  }
      for(j=0;j<N;j++)        //calculate score of war
      {
    	  for(i=0;i<N;i++)
    	  {
    		  flag=0;
    		  if((Ken[i]>Naomi[j]))
    		  {
    			  Ken[i]=-1;
    			  flag=1;
    			  break;
    		  }
    	  }
    	  if(!flag)
    	  {
    		  war++;
    		  for(i=0;i<N;i++)
    		  {
    			  if(Ken[i]!=-1)
    			  {
    				  Ken[i]=-1;
    				  break;
    			  }
    		  }
    	  }


      }
      //calculate dwar
        for(i=0;i<N;i++)
        {
        	for(j=0;j<N;j++)
        	{
        		if(Ken2[j]!=-1)
        		{
        			if(Naomi2[i]>Ken2[j])
        			{
        				dwar++;
        				Ken2[j]=-1;
        				break;
        			}
        			else
        			{
        				for(k=N-1;k>=0;k--)
        				{
        					if(Ken2[k]!=0)
        					{
        						Ken2[k]=-1;
        						break;
        					}
        				}
        				break;
        			}
        		}
        	}
        }


     cout<<"Case #"<<l-t<<": "<<dwar<<" "<<war<<endl;


  }
  return 0;

}

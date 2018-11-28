#include<iostream>
#include<string.h>
#include <stdio.h>
#include<cstdio>
using namespace std;

long long int a[26];
int main()
{

	freopen ("ans2016-a.txt","w",stdout);
	freopen ("A-large (1).in","r",stdin);
	
	long long int t,i,j,k,temp,c,mx,n,threshold,testcase;
    cin>>t;
    for(testcase=0;testcase<t;testcase++)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
           cin>>a[i];
        }
        
      mx=-1;
      	cout<<"Case #"<<testcase+1<<": ";
      //Check if is mx==0 last condition
      while(mx!=0)
      {
            mx=-1;
            //Find maximum
            for(j=0;j<n;j++)
            {
                mx=max(a[j],mx);
            }
            //Set Thresold
            threshold=2;
            
            //For Last Case
            if(mx==1)
            {
                 c=0;
                  for(i=0;i<n;i++)
                    c=c+a[i];
                  
                  if(c%2)
                     threshold=1;
            }
            
            //If max is 0.
            if(mx==0)
            {
                break;
            }
    
            //Remove 2 or 1 based on threshold
            c=0;
            for(i=0;i<n;i++)
            {
                if(a[i]==mx)
                {
                    a[i]--;
                    c++;
                    cout<<(char)(65+i);
                }
                if(c==threshold)
                    break;
                
            }
         
            cout<<" ";
      }
      cout<<endl;
    }

  	fclose (stdout);
	fclose(stdin);
	return 0;
}

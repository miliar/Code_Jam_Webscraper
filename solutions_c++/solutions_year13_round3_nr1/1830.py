/*author :saurabh3240
	problem: consonents
	com=ntest codejam
	*/
# include<iostream>
# include<cstdio>
# include<cstring>
using namespace std;
int main()
{
    int t,n,x,ans,counter,len;
	int testcount=1;
    string str;	
    scanf("%d",&t);
    while(t--)
    {	cin>>str;			
        ans=0;
        len=str.length();
        scanf("%d",&n);
		
		for(int i=0;i<len;++i)
        {
              counter=0;
              x=len;
              for(int j=i;j<len;++j)
              { 
                  if(str[j]!='a' && str[j]!='e' && str[j]!='i' && str[j]!='o' && str[j]!='u')
                  		counter++;
                  else
                  		counter=0;
				  if(counter==n)
                	{
                	    	x=j;
                         break;
                 	}
             }
    		 ans+=(len-x);
        }
    	printf("Case #%d: %d\n",testcount,ans);
    	testcount++;
	}
    return 0;
}

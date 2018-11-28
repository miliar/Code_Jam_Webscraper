#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

int main()
{     
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out","w",stdout);
    
    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        int n;
        cin>>n;
        
        //n=0
        if(n==0)
        {printf("Case #%d: INSOMNIA\n",cas);continue;}
        
        //n!=0
        int ans;
        
        bool exist[10];
        for(int j=0;j<10;j++)
            exist[j]=false;
            
        int x=n;
        while(1)
        {
            //calculate
            int y=x;
            while(y!=0)
            {
                exist[y%10]=true;
                y/=10;       
            }//
            
            //judge
            if(exist[0]&&exist[1]&&exist[2]&&exist[3]&&exist[4]&&
               exist[5]&&exist[6]&&exist[7]&&exist[8]&&exist[9])
            {ans=x;break;}
            
            //continue
            x+=n;    
        }//
            
        printf("Case #%d: %d\n",cas,ans);      
          
    }//
    
  //system("pause");
}

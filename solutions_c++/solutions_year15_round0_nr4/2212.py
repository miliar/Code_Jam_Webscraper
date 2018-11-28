#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
#define ll long long int

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    //freopen("B.txt","r",stdin);
    //freopen("Bout1.txt","w",stdout);
    int t;
    cin>>t;
    for(int q=1;q<=t;++q) 
    {
        int x,r,c;
        cin>>x>>r>>c;
        if(x==1)
        {
            printf("Case #%d: GABRIEL\n",q);   
        }
        else if(x==2)
        {
            int p=r*c;
            if(p%2!=0)
            {
               printf("Case #%d: RICHARD\n",q); 
            }
            else
            {
               printf("Case #%d: GABRIEL\n",q); 
            }
        }
        else if(x==3)
        {
            int p=r*c;
            if(min(r,c)==1)
            {
               printf("Case #%d: RICHARD\n",q); 
            }
            else if(p%3==0)
            {
               printf("Case #%d: GABRIEL\n",q); 
            }
            else
            {
               printf("Case #%d: RICHARD\n",q);
            }    
        }
        else
        {
            if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
            {
               printf("Case #%d: GABRIEL\n",q);  
            }
            else
            {
               printf("Case #%d: RICHARD\n",q);
            }
        }
        
    } 
    return 0;
}
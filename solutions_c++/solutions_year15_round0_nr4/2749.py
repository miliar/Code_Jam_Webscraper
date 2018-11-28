#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include<stdio.h>
using namespace std;
int x,r,c;

int main()
{
    int t;
    scanf("%d",&t);
    for(int w=1;w<=t;w++)
    {
        string ans="";
        scanf("%d%d%d",&x,&r,&c);
        if(r>c) { r=r+c;c=r-c;r=r-c;}
        int area = r*c;
        if(x==1) ans="GABRIEL";
        else if(x==2)
        {
            if((r>1||c>1))
				if(area%x==0) ans="GABRIEL";
				else ans="RICHARD";
            else ans="RICHARD";    
        }
		else if(x>r && x>c) ans="RICHARD";
        else if(area%x!=0) ans="RICHARD";
		else if(x>=(2*r+1)) ans="RICHARD"; 
		else if(x>=(c+r-2) && x>3) ans="RICHARD";
        
        else ans="GABRIEL";
		printf("Case #%d: ",w);
		cout<<ans<<endl;
    }
    return 0;
}


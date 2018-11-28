#include <bits/stdc++.h>

using namespace std;
 

 
int main() 
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n,r,c;
    int t;
    string s;

    scanf("%d",&t);
    for(int z=1;z<=t;z++) 
	{
        scanf("%d %d %d",&n,&r,&c);
        if(r>c) 
		swap(r,c);
 
        if(n==1) 
		s="GABRIEL";
        else if(n==2) 
		{
            if(r%2&&c%2)
			s="RICHARD";
            else s="GABRIEL";
        }
        else if(n==3) 
		{
            if(r==1||r*c%3)
			s="RICHARD";
            else s="GABRIEL";
        }
        else if(n==4) 
		{
            if((r<=2&&c<=4)||(r==3&&c==3)) 
			s="RICHARD";
            else 
			s="GABRIEL";
        }
        else if(n==5) 
		{
            if(r<=3||c<=4) 
			s="RICHARD";
            else s="GABRIEL";        	
        }
        else if(n== 6) 
		{
            if(r<=3||c<=5) 
			s="RICHARD";
            else s="GABRIEL";        	
        }
		else s="RICHARD";
        printf("Case #%d: %s\n", z, s.c_str());
    }
}

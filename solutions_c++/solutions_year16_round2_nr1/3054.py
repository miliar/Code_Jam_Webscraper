#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(){

    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );

    int t,z;
    scanf("%d",&t);
    for(z=1;z<=t;z++){
    	char s[2005];
    	scanf("%s",s);
    	int l=strlen(s);
    //	printf("%s\n",s);
    	int h[100]={0};
    	for(int i=0;i<l;i++)
    		h[s[i]]++;
    	for(int i=0;i<l;i++){
    		if(h['Z']>0){
    			s[i]='$';
    			h['Z']--;
    			h['E']--;
    			h['R']--;
    			h['O']--;
    			h[0]++;
    		}
    		else if(h['W']>0){
    			s[i]='$';
    			h['W']--;
    			h['T']--;
    			h['O']--;
    			h[2]++;
    		}
    		else if(h['U']>0){
    			s[i]='$';
    			h['F']--;
    			h['U']--;
    			h['O']--;
    			h['R']--;
    			h[4]++;
    		}
    		else if(h['X']>0){
    			s[i]='$';
    			h['S']--;
    			h['I']--;
    			h['X']--;
    			h[6]++;
    		}
    		else if(h['G']>0){
    			s[i]='$';
    			h['G']--;
    			h['I']--;
    			h['E']--;
    			h['H']--;
    			h['T']--;
    			h[8]++;
    		}
    	}
    	for(int i=0;i<l;i++)
    	{
    		if(h['O']>0)
    		{
    			s[i]='$';
    			h['E']--;
    			h['N']--;
    			h['O']--;
    			h[1]++;
    		}
    		else if(h['T']>0)
    		{
    			s[i]='$';
    			h['T']--;
    			h['E']--;
    			h['E']--;
    			h['R']--;
    			h['H']--;
    			h[3]++;
    		}
    		else if(h['F']>0)
    		{
    			s[i]='$';
    			h['F']--;
    			h['E']--;
    			h['I']--;
    			h['V']--;
    			h[5]++;
    		}
    	}
    	for(int i=0;i<l;i++)
    	{
    		if(h['V']>0)
    		{
    			s[i]='$';
    			h['S']--;
    			h['E']--;
    			h['V']--;
    			h['E']--;
    			h['N']--;
    			h[7]++;
    		}
    	}

    	for(int i=0;i<l;i++){
    		if(h['N']>0){
    			s[i]='$';
    			h['N']--;
    			h['I']--;
    			h['N']--;
    			h['E']--;
    			h[9]++;
    		}
    	}
    	int i,j;
    	printf("Case #%d: ",z);
    	for(i=0;i<10;i++){
    		for(j=h[i];j>0;j--)
    			printf("%d",i);
    	}
    	printf("\n");

    }

    return 0;
}

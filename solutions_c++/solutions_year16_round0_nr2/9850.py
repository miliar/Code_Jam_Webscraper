#include <stdio.h>
int main() {
    int t;
    char sp;
    scanf("%d",&t);
    scanf("%c",&sp);
    for(int k=0;k<=t;k++){
        char s[100];
        int i=0;
        char ch;
        scanf("%c",&ch);
    	int count=((ch=='-')?1:0);
        s[i]=ch;
        while(ch!='\n' && scanf("%c",&ch)){
            if(s[i]!=ch)
        	{
            	s[++i]=ch;
                if(s[i]=='-')
            	{
                	count+=2;
                }
            }
        }
        printf("Case #%d: %d\n",k,count);
	}
    return 0;
}

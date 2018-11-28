#include<iostream>
#include<cstdio>
using namespace std;
char s[1005];
int main(){

	int t_case,s_max,sum=0,j,total;
	scanf("%d",&t_case);
	total=t_case;
	while(t_case){
        t_case--;
        scanf("%d %s",&s_max,s);
        j=0;
        sum=s[0]-'0';
        for(int i=1;i<=s_max;i++){
            if(i>sum && s[i]-'0'!=0){
                j=j+i-sum;
                sum=i+s[i]-'0';
            }
            else{
                sum=sum+s[i]-'0';
            }

        }
        printf("Case #%d: %d\n",total-t_case,j);

	
	    
	}

}
